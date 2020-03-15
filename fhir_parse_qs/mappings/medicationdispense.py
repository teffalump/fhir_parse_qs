__all__ = ["medicationdispense_mapping", "medicationdispense_references"]

medicationdispense_mapping = {
    "code": "token",
    "identifier": "token",
    "patient": "reference",
    "medication": "reference",
    "status": "token",
    "context": "reference",
    "destination": "reference",
    "performer": "reference",
    "prescription": "reference",
    "receiver": "reference",
    "responsibleparty": "reference",
    "subject": "reference",
    "type": "token",
    "whenhandedover": "date",
    "whenprepared": "date",
}

medicationdispense_references = {
    "patient": ["Patient"],
    "medication": ["Medication"],
    "context": ["EpisodeOfCare", "Encounter"],
    "destination": ["Location"],
    "performer": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "prescription": ["MedicationRequest"],
    "receiver": ["Practitioner", "Patient"],
    "responsibleparty": ["Practitioner", "PractitionerRole"],
    "subject": ["Group", "Patient"],
}
