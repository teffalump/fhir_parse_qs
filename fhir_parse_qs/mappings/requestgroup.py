__all__ = ["requestgroup_mapping", "requestgroup_references"]

requestgroup_mapping = {
    "author": "reference",
    "authored": "date",
    "code": "token",
    "encounter": "reference",
    "group-identifier": "token",
    "identifier": "token",
    "instantiates-canonical": "reference",
    "instantiates-uri": "uri",
    "intent": "token",
    "participant": "reference",
    "patient": "reference",
    "priority": "token",
    "status": "token",
    "subject": "reference",
}

requestgroup_references = {
    "author": ["Practitioner", "Device", "PractitionerRole"],
    "encounter": ["Encounter"],
    "participant": [
        "Practitioner",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "patient": ["Patient"],
    "subject": ["Group", "Patient"],
}
