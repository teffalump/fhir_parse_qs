__all__ = ["claim_mapping", "claim_references"]

claim_mapping = {
    "care-team": "reference",
    "created": "date",
    "detail-udi": "reference",
    "encounter": "reference",
    "enterer": "reference",
    "facility": "reference",
    "identifier": "token",
    "insurer": "reference",
    "item-udi": "reference",
    "patient": "reference",
    "payee": "reference",
    "priority": "token",
    "procedure-udi": "reference",
    "provider": "reference",
    "status": "token",
    "subdetail-udi": "reference",
    "use": "token",
}

claim_references = {
    "care-team": ["Practitioner", "Organization", "PractitionerRole"],
    "detail-udi": ["Device"],
    "encounter": ["Encounter"],
    "enterer": ["Practitioner", "PractitionerRole"],
    "facility": ["Location"],
    "insurer": ["Organization"],
    "item-udi": ["Device"],
    "patient": ["Patient"],
    "payee": [
        "Practitioner",
        "Organization",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "procedure-udi": ["Device"],
    "provider": ["Practitioner", "Organization", "PractitionerRole"],
    "subdetail-udi": ["Device"],
}
