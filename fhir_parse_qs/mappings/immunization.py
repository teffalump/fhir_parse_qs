__all__ = ["immunization_mapping", "immunization_references"]

immunization_mapping = {
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "location": "reference",
    "lot-number": "string",
    "manufacturer": "reference",
    "performer": "reference",
    "reaction": "reference",
    "reaction-date": "date",
    "reason-code": "token",
    "reason-reference": "reference",
    "series": "string",
    "status": "token",
    "status-reason": "token",
    "target-disease": "token",
    "vaccine-code": "token",
}

immunization_references = {
    "patient": ["Patient"],
    "location": ["Location"],
    "manufacturer": ["Organization"],
    "performer": ["Practitioner", "Organization", "PractitionerRole"],
    "reaction": ["Observation"],
    "reason-reference": ["Condition", "Observation", "DiagnosticReport"],
}
