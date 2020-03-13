__all__ = ["deviceusestatement_mapping", "deviceusestatement_references"]

deviceusestatement_mapping = {
    "patient": "reference",
    "device": "reference",
    "identifier": "token",
    "subject": "reference",
}

deviceusestatement_references = {
    "patient": ["Patient"],
    "device": ["Device"],
    "subject": ["Group", "Patient"],
}
