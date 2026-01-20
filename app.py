# app.py
import streamlit as st
from datetime import datetime

from logic import global_risk, calculate_range
from data import estimate_base_price
from messages import risk_explanation, field_advice, legal_warning

CURRENT_YEAR = datetime.now().year

st.set_page_config(page_title="IA Douane Togo – Estimation", layout="centered")

st.title("🚗 Estimation indicative – Import véhicule d’occasion")
st.write("Outil d’aide à la décision **AVANT importation** (non officiel).")

st.info("Basé sur expériences terrain, estimation indicative")

with st.form("estimation_form"):
    vehicle_year = st.number_input("Année du véhicule", min_value=1990, max_value=CURRENT_YEAR, step=1)
    cv = st.number_input("Puissance fiscale (CV)", min_value=1, max_value=30, step=1)

    submitted = st.form_submit_button("Obtenir une estimation")

if submitted:
    risk_data = global_risk(vehicle_year, cv)
    base_estimate = estimate_base_price(vehicle_year, cv, CURRENT_YEAR)

    min_price, max_price = calculate_range(base_estimate, risk_data["final_risk"])

    st.subheader("📊 Résultat")
    st.write(f"**Fourchette estimée :** {min_price:,} – {max_price:,} FCFA")
    st.write(f"**Niveau de risque :** {risk_data['final_risk']}")

    st.write("**Pourquoi ce risque ?**")
    st.write(risk_explanation(risk_data["final_risk"]))

    st.write("**Conseil terrain :**")
    st.write(field_advice(risk_data["final_risk"]))

    st.warning(legal_warning())