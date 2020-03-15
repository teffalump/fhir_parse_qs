__all__ = [
    "coverageeligibilityresponse_mapping",
    "coverageeligibilityresponse_references",
]

coverageeligibilityresponse_mapping = {
    "created": "date",
    "disposition": "string",
    "identifier": "token",
    "insurer": "reference",
    "outcome": "token",
    "patient": "reference",
    "request": "reference",
    "requestor": "reference",
    "status": "token",
}

coverageeligibilityresponse_references = {
    "insurer": ["Organization"],
    "patient": ["Patient"],
    "request": ["CoverageEligibilityRequest"],
    "requestor": ["Practitioner", "Organization", "PractitionerRole"],
}
