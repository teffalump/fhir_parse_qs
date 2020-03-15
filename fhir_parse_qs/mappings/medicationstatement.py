__all__ = ["medicationstatement_mapping", "medicationstatement_references"]

medicationstatement_mapping = {
    "code": "token",
    "identifier": "token",
    "patient": "reference",
    "medication": "reference",
    "status": "token",
    "category": "token",
    "context": "reference",
    "effective": "date",
    "part-of": "reference",
    "source": "reference",
    "subject": "reference",
}

medicationstatement_references = {
    "patient": ["Patient"],
    "medication": ["Medication"],
    "context": ["EpisodeOfCare", "Encounter"],
    "part-of": [
        "MedicationDispense",
        "Observation",
        "MedicationAdministration",
        "Procedure",
        "MedicationStatement",
    ],
    "source": [
        "Practitioner",
        "Organization",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "subject": ["Group", "Patient"],
}
