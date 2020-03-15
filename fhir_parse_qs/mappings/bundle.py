__all__ = ["bundle_mapping", "bundle_references"]

bundle_mapping = {
    "composition": "reference",
    "identifier": "token",
    "message": "reference",
    "timestamp": "date",
    "type": "token",
}

bundle_references = {
    "composition": ["Composition"],
    "message": ["MessageHeader"],
}
