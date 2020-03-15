__all__ = ["careteam_mapping", "careteam_references"]

careteam_mapping = {
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "category": "token",
    "encounter": "reference",
    "participant": "reference",
    "status": "token",
    "subject": "reference",
}

careteam_references = {
    "patient": ["Patient"],
    "encounter": ["Encounter"],
    "participant": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "subject": ["Group", "Patient"],
}
