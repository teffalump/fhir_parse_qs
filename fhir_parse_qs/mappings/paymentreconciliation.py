__all__ = ["paymentreconciliation_mapping", "paymentreconciliation_references"]

paymentreconciliation_mapping = {
    "created": "date",
    "disposition": "string",
    "identifier": "token",
    "outcome": "token",
    "payment-issuer": "reference",
    "request": "reference",
    "requestor": "reference",
    "status": "token",
}

paymentreconciliation_references = {
    "payment-issuer": ["Organization"],
    "request": ["Task"],
    "requestor": ["Practitioner", "Organization", "PractitionerRole"],
}
