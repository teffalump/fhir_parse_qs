__all__ = ["enrollmentrequest_mapping", "enrollmentrequest_references"]

enrollmentrequest_mapping = {
    "identifier": "token",
    "patient": "reference",
    "status": "token",
    "subject": "reference",
}

enrollmentrequest_references = {
    "patient": ["Patient"],
    "subject": ["Patient"],
}
