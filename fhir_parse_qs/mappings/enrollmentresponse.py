__all__ = ["enrollmentresponse_mapping", "enrollmentresponse_references"]

enrollmentresponse_mapping = {
    "identifier": "token",
    "request": "reference",
    "status": "token",
}

enrollmentresponse_references = {
    "request": ["EnrollmentRequest"],
}
