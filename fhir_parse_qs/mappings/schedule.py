__all__ = ["schedule_mapping", "schedule_references"]

schedule_mapping = {
    "active": "token",
    "actor": "reference",
    "date": "date",
    "identifier": "token",
    "service-category": "token",
    "service-type": "token",
    "specialty": "token",
}

schedule_references = {
    "actor": [
        "Practitioner",
        "Device",
        "Patient",
        "HealthcareService",
        "PractitionerRole",
        "RelatedPerson",
        "Location",
    ],
}
