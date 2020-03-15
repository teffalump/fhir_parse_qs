__all__ = ["bodystructure_mapping", "bodystructure_references"]

bodystructure_mapping = {
    "identifier": "token",
    "location": "token",
    "morphology": "token",
    "patient": "reference",
}

bodystructure_references = {
    "patient": ["Patient"],
}
