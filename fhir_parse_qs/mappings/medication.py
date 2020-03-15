__all__ = ["medication_mapping", "medication_references"]

medication_mapping = {
    "code": "token",
    "expiration-date": "date",
    "form": "token",
    "identifier": "token",
    "ingredient": "reference",
    "ingredient-code": "token",
    "lot-number": "token",
    "manufacturer": "reference",
    "status": "token",
}

medication_references = {
    "ingredient": ["Medication", "Substance"],
    "manufacturer": ["Organization"],
}
