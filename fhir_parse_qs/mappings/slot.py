__all__ = ["slot_mapping", "slot_references"]

slot_mapping = {
    "appointment-type": "token",
    "identifier": "token",
    "schedule": "reference",
    "service-category": "token",
    "service-type": "token",
    "specialty": "token",
    "start": "date",
    "status": "token",
}

slot_references = {
    "schedule": ["Schedule"],
}
