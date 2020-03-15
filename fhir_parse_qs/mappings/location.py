__all__ = ["location_mapping", "location_references"]

location_mapping = {
    "address": "string",
    "address-city": "string",
    "address-country": "string",
    "address-postalcode": "string",
    "address-state": "string",
    "address-use": "token",
    "endpoint": "reference",
    "identifier": "token",
    "name": "string",
    "near": "special",
    "operational-status": "token",
    "organization": "reference",
    "partof": "reference",
    "status": "token",
    "type": "token",
}

location_references = {
    "endpoint": ["Endpoint"],
    "organization": ["Organization"],
    "partof": ["Location"],
}
