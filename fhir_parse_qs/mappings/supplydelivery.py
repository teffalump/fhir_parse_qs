__all__ = ["supplydelivery_mapping", "supplydelivery_references"]

supplydelivery_mapping = {
    "identifier": "token",
    "patient": "reference",
    "receiver": "reference",
    "status": "token",
    "supplier": "reference",
}

supplydelivery_references = {
    "patient": ["Patient"],
    "receiver": ["Practitioner", "PractitionerRole"],
    "supplier": ["Practitioner", "Organization", "PractitionerRole"],
}
