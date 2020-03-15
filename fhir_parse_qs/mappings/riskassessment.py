__all__ = ["riskassessment_mapping", "riskassessment_references"]

riskassessment_mapping = {
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "encounter": "reference",
    "condition": "reference",
    "method": "token",
    "performer": "reference",
    "probability": "number",
    "risk": "token",
    "subject": "reference",
}

riskassessment_references = {
    "patient": ["Patient"],
    "encounter": ["Encounter"],
    "condition": ["Condition"],
    "performer": ["Practitioner", "Device", "PractitionerRole"],
    "subject": ["Group", "Patient"],
}
