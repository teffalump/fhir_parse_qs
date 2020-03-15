__all__ = [
    "coverageeligibilityrequest_mapping",
    "coverageeligibilityrequest_references",
]

coverageeligibilityrequest_mapping = {
    "created": "date",
    "enterer": "reference",
    "facility": "reference",
    "identifier": "token",
    "patient": "reference",
    "provider": "reference",
    "status": "token",
}

coverageeligibilityrequest_references = {
    "enterer": ["Practitioner", "PractitionerRole"],
    "facility": ["Location"],
    "patient": ["Patient"],
    "provider": ["Practitioner", "Organization", "PractitionerRole"],
}
