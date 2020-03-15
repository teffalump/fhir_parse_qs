__all__ = ["account_mapping", "account_references"]

account_mapping = {
    "identifier": "token",
    "name": "string",
    "owner": "reference",
    "patient": "reference",
    "period": "date",
    "status": "token",
    "subject": "reference",
    "type": "token",
}

account_references = {
    "owner": ["Organization"],
    "patient": ["Patient"],
    "subject": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "HealthcareService",
        "PractitionerRole",
        "Location",
    ],
}
