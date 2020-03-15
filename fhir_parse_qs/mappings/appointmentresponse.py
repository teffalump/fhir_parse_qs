__all__ = ["appointmentresponse_mapping", "appointmentresponse_references"]

appointmentresponse_mapping = {
    "actor": "reference",
    "appointment": "reference",
    "identifier": "token",
    "location": "reference",
    "part-status": "token",
    "patient": "reference",
    "practitioner": "reference",
}

appointmentresponse_references = {
    "actor": [
        "Practitioner",
        "Device",
        "Patient",
        "HealthcareService",
        "PractitionerRole",
        "RelatedPerson",
        "Location",
    ],
    "appointment": ["Appointment"],
    "location": ["Location"],
    "patient": ["Patient"],
    "practitioner": ["Practitioner"],
}
