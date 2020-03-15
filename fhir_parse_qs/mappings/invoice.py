__all__ = ["invoice_mapping", "invoice_references"]

invoice_mapping = {
    "account": "reference",
    "date": "date",
    "identifier": "token",
    "issuer": "reference",
    "participant": "reference",
    "participant-role": "token",
    "patient": "reference",
    "recipient": "reference",
    "status": "token",
    "subject": "reference",
    "totalgross": "quantity",
    "totalnet": "quantity",
    "type": "token",
}

invoice_references = {
    "account": ["Account"],
    "issuer": ["Organization"],
    "participant": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "patient": ["Patient"],
    "recipient": ["Organization", "Patient", "RelatedPerson"],
    "subject": ["Group", "Patient"],
}
