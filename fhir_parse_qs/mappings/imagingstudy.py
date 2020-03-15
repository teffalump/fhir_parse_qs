__all__ = ["imagingstudy_mapping", "imagingstudy_references"]

imagingstudy_mapping = {
    "identifier": "token",
    "patient": "reference",
    "basedon": "reference",
    "bodysite": "token",
    "dicom-class": "token",
    "encounter": "reference",
    "endpoint": "reference",
    "instance": "token",
    "interpreter": "reference",
    "modality": "token",
    "performer": "reference",
    "reason": "token",
    "referrer": "reference",
    "series": "token",
    "started": "date",
    "status": "token",
    "subject": "reference",
}

imagingstudy_references = {
    "patient": ["Patient"],
    "basedon": [
        "Appointment",
        "AppointmentResponse",
        "CarePlan",
        "Task",
        "ServiceRequest",
    ],
    "encounter": ["Encounter"],
    "endpoint": ["Endpoint"],
    "interpreter": ["Practitioner", "PractitionerRole"],
    "performer": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "referrer": ["Practitioner", "PractitionerRole"],
    "subject": ["Group", "Device", "Patient"],
}
