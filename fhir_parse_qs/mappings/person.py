__all__ = ["person_mapping", "person_references"]

person_mapping = {
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
    "identifier": "token",
    "link": "reference",
    "name": "string",
    "organization": "reference",
    "patient": "reference",
    "practitioner": "reference",
    "relatedperson": "reference",
}

person_references = {
    "link": ["Practitioner", "Patient", "Person", "RelatedPerson"],
    "organization": ["Organization"],
    "patient": ["Patient"],
    "practitioner": ["Practitioner"],
    "relatedperson": ["RelatedPerson"],
}
