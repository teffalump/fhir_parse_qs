__all__ = ["chargeitem_mapping", "chargeitem_references"]

chargeitem_mapping = {
    "account": "reference",
    "code": "token",
    "context": "reference",
    "entered-date": "date",
    "enterer": "reference",
    "factor-override": "number",
    "identifier": "token",
    "occurrence": "date",
    "patient": "reference",
    "performer-actor": "reference",
    "performer-function": "token",
    "performing-organization": "reference",
    "price-override": "quantity",
    "quantity": "quantity",
    "requesting-organization": "reference",
    "service": "reference",
    "subject": "reference",
}

chargeitem_references = {
    "account": ["Account"],
    "context": ["EpisodeOfCare", "Encounter"],
    "enterer": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "patient": ["Patient"],
    "performer-actor": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "performing-organization": ["Organization"],
    "requesting-organization": ["Organization"],
    "service": [
        "Immunization",
        "MedicationDispense",
        "SupplyDelivery",
        "Observation",
        "DiagnosticReport",
        "ImagingStudy",
        "MedicationAdministration",
        "Procedure",
    ],
    "subject": ["Group", "Patient"],
}
