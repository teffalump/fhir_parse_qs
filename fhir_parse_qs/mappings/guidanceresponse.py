__all__ = ["guidanceresponse_mapping", "guidanceresponse_references"]

guidanceresponse_mapping = {
    "identifier": "token",
    "patient": "reference",
    "request": "token",
    "subject": "reference",
}

guidanceresponse_references = {
    "patient": ["Patient"],
    "subject": ["Group", "Patient"],
}
