__all__ = ["medicationknowledge_mapping", "medicationknowledge_references"]

medicationknowledge_mapping = {
    "classification": "token",
    "classification-type": "token",
    "code": "token",
    "doseform": "token",
    "ingredient": "reference",
    "ingredient-code": "token",
    "manufacturer": "reference",
    "monitoring-program-name": "token",
    "monitoring-program-type": "token",
    "monograph": "reference",
    "monograph-type": "token",
    "source-cost": "token",
    "status": "token",
}

medicationknowledge_references = {
    "ingredient": ["Substance"],
    "manufacturer": ["Organization"],
    "monograph": ["Media", "DocumentReference"],
}
