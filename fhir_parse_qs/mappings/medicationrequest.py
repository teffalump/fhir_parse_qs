__all__ = ["medicationrequest_mapping", "medicationrequest_references"]

medicationrequest_mapping = {
    "code": "token",
    "identifier": "token",
    "patient": "reference",
    "medication": "reference",
    "status": "token",
    "authoredon": "date",
    "category": "token",
    "date": "date",
    "encounter": "reference",
    "intended-dispenser": "reference",
    "intended-performer": "reference",
    "intended-performertype": "token",
    "intent": "token",
    "priority": "token",
    "requester": "reference",
    "subject": "reference",
}

medicationrequest_references = {
    "patient": ["Patient"],
    "medication": ["Medication"],
    "encounter": ["Encounter"],
    "intended-dispenser": ["Organization"],
    "intended-performer": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "requester": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "subject": ["Group", "Patient"],
}
