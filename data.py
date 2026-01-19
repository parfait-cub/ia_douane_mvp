# data.py
# Données fictives expertes – NON officielles

INTERNAL_REFERENCE_PRICE = 650_000  # Valeur de référence interne (NON affichée, NON officielle)

AGE_COEFFICIENT = {
    "recent": 1.0,      # ≤ 5 ans
    "middle": 1.2,      # 6–10 ans
    "old": 1.4          # > 10 ans
}

POWER_COEFFICIENT = {
    "low": 1.0,         # ≤ 6 CV
    "medium": 1.15,     # 7–10 CV
    "high": 1.3         # > 10 CV
}


def estimate_base_price(vehicle_year: int, cv: int, current_year: int) -> float:
    age = current_year - vehicle_year

    if age <= 5:
        age_factor = AGE_COEFFICIENT["recent"]
    elif age <= 10:
        age_factor = AGE_COEFFICIENT["middle"]
    else:
        age_factor = AGE_COEFFICIENT["old"]

    if cv <= 6:
        power_factor = POWER_COEFFICIENT["low"]
    elif cv <= 10:
        power_factor = POWER_COEFFICIENT["medium"]
    else:
        power_factor = POWER_COEFFICIENT["high"]

    return INTERNAL_REFERENCE_PRICE * age_factor * power_factor
