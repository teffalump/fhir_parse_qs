__all__ = ["diagnosticreport_mapping", "diagnosticreport_references"]

diagnosticreport_mapping = {
    "code": "token",
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "encounter": "reference",
    "based-on": "reference",
    "category": "token",
    "conclusion": "token",
    "issued": "date",
    "media": "reference",
    "performer": "reference",
    "result": "reference",
    "results-interpreter": "reference",
    "specimen": "reference",
    "status": "token",
    "subject": "reference",
}

diagnosticreport_references = {
    "patient": ["Patient"],
    "encounter": ["Encounter"],
    "based-on": [
        "CarePlan",
        "MedicationRequest",
        "NutritionOrder",
        "ServiceRequest",
        "ImmunizationRecommendation",
    ],
    "media": ["Media"],
    "performer": ["Practitioner", "Organization", "CareTeam", "PractitionerRole"],
    "result": ["Observation"],
    "results-interpreter": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "PractitionerRole",
    ],
    "specimen": ["Specimen"],
    "subject": ["Group", "Device", "Patient", "Location"],
}
