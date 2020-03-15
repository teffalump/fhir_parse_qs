__all__ = ["supplyrequest_mapping", "supplyrequest_references"]

supplyrequest_mapping = {
    "date": "date",
    "identifier": "token",
    "category": "token",
    "requester": "reference",
    "status": "token",
    "subject": "reference",
    "supplier": "reference",
}

supplyrequest_references = {
    "requester": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "subject": ["Organization", "Patient", "Location"],
    "supplier": ["Organization", "HealthcareService"],
}
