__all__ = ["allergyintolerance_mapping", "allergyintolerance_references"]

allergyintolerance_mapping = {
    "asserter": "reference",
    "category": "token",
    "clinical-status": "token",
    "code": "token",
    "criticality": "token",
    "date": "date",
    "identifier": "token",
    "last-date": "date",
    "manifestation": "token",
    "onset": "date",
    "patient": "reference",
    "recorder": "reference",
    "route": "token",
    "severity": "token",
    "type": "token",
    "verification-status": "token",
}

allergyintolerance_references = {
    "asserter": ["Practitioner", "Patient", "PractitionerRole", "RelatedPerson"],
    "patient": ["Patient"],
    "recorder": ["Practitioner", "Patient", "PractitionerRole", "RelatedPerson"],
}
