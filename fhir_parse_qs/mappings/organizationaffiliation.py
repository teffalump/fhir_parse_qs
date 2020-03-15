__all__ = ["organizationaffiliation_mapping", "organizationaffiliation_references"]

organizationaffiliation_mapping = {
    "active": "token",
    "date": "date",
    "email": "token",
    "endpoint": "reference",
    "identifier": "token",
    "location": "reference",
    "network": "reference",
    "participating-organization": "reference",
    "phone": "token",
    "primary-organization": "reference",
    "role": "token",
    "service": "reference",
    "specialty": "token",
    "telecom": "token",
}

organizationaffiliation_references = {
    "endpoint": ["Endpoint"],
    "location": ["Location"],
    "network": ["Organization"],
    "participating-organization": ["Organization"],
    "primary-organization": ["Organization"],
    "service": ["HealthcareService"],
}
