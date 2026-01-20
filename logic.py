# logic.py
from datetime import datetime

CURRENT_YEAR = datetime.now().year
MIN_SECURITY_FLOOR = 450_000  # FCFA (OBLIGATOIRE)

RISK_ORDER = ["Faible", "Moyen", "Élevé"]

RISK_MARGIN = {
    "Faible": 0.15,
    "Moyen": 0.25,
    "Élevé": 0.40  # Ajusté pour terrain réel
}


def risk_from_age(vehicle_year: int) -> str:
    age = CURRENT_YEAR - vehicle_year
    if age <= 5:
        return "Faible"
    elif age <= 10:
        return "Moyen"
    else:
        return "Élevé"


def risk_from_power(cv: int) -> str:
    if cv <= 6:
        return "Faible"
    elif cv <= 10:
        return "Moyen"
    else:
        return "Élevé"


def global_risk(vehicle_year: int, cv: int) -> dict:
    age_risk = risk_from_age(vehicle_year)
    power_risk = risk_from_power(cv)
    final_risk = max(age_risk, power_risk, key=lambda r: RISK_ORDER.index(r))

    return {
        "age_risk": age_risk,
        "power_risk": power_risk,
        "final_risk": final_risk
    }


def calculate_range(base_estimate: float, risk_level: str) -> tuple:
    margin = RISK_MARGIN[risk_level]

    min_estimate = max(base_estimate * (1 - margin), MIN_SECURITY_FLOOR)
    max_estimate = base_estimate * (1 + margin)

    # Arrondi terrain (milliers)
    min_estimate = round(min_estimate, -3)
    max_estimate = round(max_estimate, -3)

    return int(min_estimate), int(max_estimate)