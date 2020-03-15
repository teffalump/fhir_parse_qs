__all__ = ["adverseevent_mapping", "adverseevent_references"]

adverseevent_mapping = {
    "actuality": "token",
    "category": "token",
    "date": "date",
    "event": "token",
    "location": "reference",
    "recorder": "reference",
    "resultingcondition": "reference",
    "seriousness": "token",
    "severity": "token",
    "study": "reference",
    "subject": "reference",
    "substance": "reference",
}

adverseevent_references = {
    "location": ["Location"],
    "recorder": ["Practitioner", "Patient", "PractitionerRole", "RelatedPerson"],
    "resultingcondition": ["Condition"],
    "study": ["ResearchStudy"],
    "subject": ["Practitioner", "Group", "Patient", "RelatedPerson"],
    "substance": [
        "Immunization",
        "Device",
        "Medication",
        "Procedure",
        "Substance",
        "MedicationAdministration",
        "MedicationStatement",
    ],
}
