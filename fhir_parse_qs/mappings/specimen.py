__all__ = ["specimen_mapping", "specimen_references"]

specimen_mapping = {
    "accession": "token",
    "bodysite": "token",
    "collected": "date",
    "collector": "reference",
    "container": "token",
    "container-id": "token",
    "identifier": "token",
    "parent": "reference",
    "patient": "reference",
    "status": "token",
    "subject": "reference",
    "type": "token",
}

specimen_references = {
    "collector": ["Practitioner", "PractitionerRole"],
    "parent": ["Specimen"],
    "patient": ["Patient"],
    "subject": ["Group", "Device", "Patient", "Substance", "Location"],
}
