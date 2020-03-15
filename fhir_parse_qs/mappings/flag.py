__all__ = ["flag_mapping", "flag_references"]

flag_mapping = {
    "date": "date",
    "patient": "reference",
    "encounter": "reference",
    "author": "reference",
    "identifier": "token",
    "subject": "reference",
}

flag_references = {
    "patient": ["Patient"],
    "encounter": ["Encounter"],
    "author": ["Practitioner", "Organization", "Device", "Patient", "PractitionerRole"],
    "subject": [
        "Practitioner",
        "Group",
        "Organization",
        "Medication",
        "Patient",
        "PlanDefinition",
        "Procedure",
        "Location",
    ],
}
