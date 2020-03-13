__all__ = ["organization_mapping", "organization_references"]

organization_mapping = {
    "active": "token",
    "address": "string",
    "address-city": "string",
    "address-country": "string",
    "address-postalcode": "string",
    "address-state": "string",
    "address-use": "token",
    "endpoint": "reference",
    "identifier": "token",
    "name": "string",
    "partof": "reference",
    "phonetic": "string",
    "type": "token",
}

organization_references = {
    "endpoint": ["Endpoint"],
    "partof": ["Organization"],
}
