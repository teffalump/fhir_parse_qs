__all__ = ["media_mapping", "media_references"]

media_mapping = {
    "based-on": "reference",
    "created": "date",
    "device": "reference",
    "encounter": "reference",
    "identifier": "token",
    "modality": "token",
    "operator": "reference",
    "patient": "reference",
    "site": "token",
    "status": "token",
    "subject": "reference",
    "type": "token",
    "view": "token",
}

media_references = {
    "based-on": ["CarePlan", "ServiceRequest"],
    "device": ["Device", "DeviceMetric"],
    "encounter": ["Encounter"],
    "operator": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "patient": ["Patient"],
    "subject": [
        "Practitioner",
        "Group",
        "Specimen",
        "Device",
        "Patient",
        "PractitionerRole",
        "Location",
    ],
}
