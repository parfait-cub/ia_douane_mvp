# messages.py

def risk_explanation(risk_level: str) -> str:
    if risk_level == "Faible":
        return "Profil généralement stable, variations limitées observées."
    elif risk_level == "Moyen":
        return "Profil sensible : des écarts sont souvent constatés à l’arrivée."
    else:
        return "Profil à forte incertitude : variations importantes fréquentes."


def field_advice(risk_level: str) -> str:
    if risk_level == "Faible":
        return "Prévoir une petite marge de sécurité avant l’importation. 💡 Astuce terrain : toujours prévoir 10–15 % de marge supplémentaire."
    elif risk_level == "Moyen":
        return "Éviter les budgets trop serrés. Prévoir une réserve. 💡 Astuce terrain : toujours prévoir 10–15 % de marge supplémentaire."
    else:
        return "Importer uniquement avec une marge financière confortable. 💡 Astuce terrain : toujours prévoir 10–15 % de marge supplémentaire."


def legal_warning() -> str:
    return (
        "⚠️ Avertissement important\n"
        "Cette estimation est une AIDE À LA DÉCISION avant importation.\n"
        "Elle est basée sur des observations terrain NON officielles.\n"
        "Elle ne remplace en aucun cas un calcul douanier réel.\n"
        "Les montants finaux dépendent des services douaniers et contrôles."
    )