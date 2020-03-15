__all__ = ["healthcareservice_mapping", "healthcareservice_references"]

healthcareservice_mapping = {
    "active": "token",
    "characteristic": "token",
    "coverage-area": "reference",
    "endpoint": "reference",
    "identifier": "token",
    "location": "reference",
    "name": "string",
    "organization": "reference",
    "program": "token",
    "service-category": "token",
    "service-type": "token",
    "specialty": "token",
}

healthcareservice_references = {
    "coverage-area": ["Location"],
    "endpoint": ["Endpoint"],
    "location": ["Location"],
    "organization": ["Organization"],
}
