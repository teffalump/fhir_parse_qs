__all__ = ["medicationadministration_mapping", "medicationadministration_references"]

medicationadministration_mapping = {
    "code": "token",
    "identifier": "token",
    "patient": "reference",
    "context": "reference",
    "device": "reference",
    "effective-time": "date",
    "medication": "reference",
    "performer": "reference",
    "reason-given": "token",
    "reason-not-given": "token",
    "request": "reference",
    "status": "token",
    "subject": "reference",
}

medicationadministration_references = {
    "patient": ["Patient"],
    "context": ["EpisodeOfCare", "Encounter"],
    "device": ["Device"],
    "medication": ["Medication"],
    "performer": [
        "Practitioner",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "request": ["MedicationRequest"],
    "subject": ["Group", "Patient"],
}
