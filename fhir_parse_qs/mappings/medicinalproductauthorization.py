__all__ = [
    "medicinalproductauthorization_mapping",
    "medicinalproductauthorization_references",
]

medicinalproductauthorization_mapping = {
    "country": "token",
    "holder": "reference",
    "identifier": "token",
    "status": "token",
    "subject": "reference",
}

medicinalproductauthorization_references = {
    "holder": ["Organization"],
    "subject": ["MedicinalProductPackaged", "MedicinalProduct"],
}
