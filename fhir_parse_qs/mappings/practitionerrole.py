__all__ = ["practitionerrole_mapping", "practitionerrole_references"]

practitionerrole_mapping = {
    "email": "token",
    "phone": "token",
    "telecom": "token",
    "active": "token",
    "date": "date",
    "endpoint": "reference",
    "identifier": "token",
    "location": "reference",
    "organization": "reference",
    "practitioner": "reference",
    "role": "token",
    "service": "reference",
    "specialty": "token",
}

practitionerrole_references = {
    "endpoint": ["Endpoint"],
    "location": ["Location"],
    "organization": ["Organization"],
    "practitioner": ["Practitioner"],
    "service": ["HealthcareService"],
}
