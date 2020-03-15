__all__ = ["relatedperson_mapping", "relatedperson_references"]

relatedperson_mapping = {
    "address": "string",
    "address-city": "string",
    "address-country": "string",
    "address-postalcode": "string",
    "address-state": "string",
    "address-use": "token",
    "birthdate": "date",
    "email": "token",
    "gender": "token",
    "phone": "token",
    "phonetic": "string",
    "telecom": "token",
    "active": "token",
    "identifier": "token",
    "name": "string",
    "patient": "reference",
    "relationship": "token",
}

relatedperson_references = {
    "patient": ["Patient"],
}
