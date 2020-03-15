__all__ = ["immunizationevaluation_mapping", "immunizationevaluation_references"]

immunizationevaluation_mapping = {
    "date": "date",
    "dose-status": "token",
    "identifier": "token",
    "immunization-event": "reference",
    "patient": "reference",
    "status": "token",
    "target-disease": "token",
}

immunizationevaluation_references = {
    "immunization-event": ["Immunization"],
    "patient": ["Patient"],
}
