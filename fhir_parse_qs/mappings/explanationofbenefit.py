__all__ = ["explanationofbenefit_mapping", "explanationofbenefit_references"]

explanationofbenefit_mapping = {
    "care-team": "reference",
    "claim": "reference",
    "coverage": "reference",
    "created": "date",
    "detail-udi": "reference",
    "disposition": "string",
    "encounter": "reference",
    "enterer": "reference",
    "facility": "reference",
    "identifier": "token",
    "item-udi": "reference",
    "patient": "reference",
    "payee": "reference",
    "procedure-udi": "reference",
    "provider": "reference",
    "status": "token",
    "subdetail-udi": "reference",
}

explanationofbenefit_references = {
    "care-team": ["Practitioner", "Organization", "PractitionerRole"],
    "claim": ["Claim"],
    "coverage": ["Coverage"],
    "detail-udi": ["Device"],
    "encounter": ["Encounter"],
    "enterer": ["Practitioner", "PractitionerRole"],
    "facility": ["Location"],
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
