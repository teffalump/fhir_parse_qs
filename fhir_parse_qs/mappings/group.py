__all__ = ["group_mapping", "group_references"]

group_mapping = {
    "actual": "token",
    "characteristic": "token",
    "code": "token",
    "exclude": "token",
    "identifier": "token",
    "managing-entity": "reference",
    "member": "reference",
    "type": "token",
    "value": "token",
    "characteristic-value": "composite",
}

group_references = {
    "managing-entity": [
        "Practitioner",
        "Organization",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "member": [
        "Practitioner",
        "Group",
        "Device",
        "Medication",
        "Patient",
        "Substance",
        "PractitionerRole",
    ],
}
