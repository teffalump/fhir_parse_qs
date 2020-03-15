__all__ = ["patient_mapping", "patient_references"]

patient_mapping = {
    "active": "token",
    "address": "string",
    "address-city": "string",
    "address-country": "string",
    "address-postalcode": "string",
    "address-state": "string",
    "address-use": "token",
    "birthdate": "date",
    "death-date": "date",
    "deceased": "token",
    "email": "token",
    "family": "string",
    "gender": "token",
    "general-practitioner": "reference",
    "given": "string",
    "identifier": "token",
    "language": "token",
    "link": "reference",
    "name": "string",
    "organization": "reference",
    "phone": "token",
    "phonetic": "string",
    "telecom": "token",
}

patient_references = {
    "general-practitioner": ["Practitioner", "Organization", "PractitionerRole"],
    "link": ["Patient", "RelatedPerson"],
    "organization": ["Organization"],
}
