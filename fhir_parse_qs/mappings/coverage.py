__all__ = ["coverage_mapping", "coverage_references"]

coverage_mapping = {
    "beneficiary": "reference",
    "class-type": "token",
    "class-value": "string",
    "dependent": "string",
    "identifier": "token",
    "patient": "reference",
    "payor": "reference",
    "policy-holder": "reference",
    "status": "token",
    "subscriber": "reference",
    "type": "token",
}

coverage_references = {
    "beneficiary": ["Patient"],
    "patient": ["Patient"],
    "payor": ["Organization", "Patient", "RelatedPerson"],
    "policy-holder": ["Organization", "Patient", "RelatedPerson"],
    "subscriber": ["Patient", "RelatedPerson"],
}
