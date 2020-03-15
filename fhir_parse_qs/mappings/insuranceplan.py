__all__ = ["insuranceplan_mapping", "insuranceplan_references"]

insuranceplan_mapping = {
    "address": "string",
    "address-city": "string",
    "address-country": "string",
    "address-postalcode": "string",
    "address-state": "string",
    "address-use": "token",
    "administered-by": "reference",
    "endpoint": "reference",
    "identifier": "token",
    "name": "string",
    "owned-by": "reference",
    "phonetic": "string",
    "status": "token",
    "type": "token",
}

insuranceplan_references = {
    "administered-by": ["Organization"],
    "endpoint": ["Endpoint"],
    "owned-by": ["Organization"],
}
