__all__ = ["procedure_mapping", "procedure_references"]

procedure_mapping = {
    "code": "token",
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "encounter": "reference",
    "based-on": "reference",
    "category": "token",
    "instantiates-canonical": "reference",
    "instantiates-uri": "uri",
    "location": "reference",
    "part-of": "reference",
    "performer": "reference",
    "reason-code": "token",
    "reason-reference": "reference",
    "status": "token",
    "subject": "reference",
}

procedure_references = {
    "patient": ["Patient"],
    "encounter": ["Encounter"],
    "based-on": ["CarePlan", "ServiceRequest"],
    "instantiates-canonical": [
        "Questionnaire",
        "Measure",
        "PlanDefinition",
        "OperationDefinition",
        "ActivityDefinition",
    ],
    "location": ["Location"],
    "part-of": ["Observation", "Procedure", "MedicationAdministration"],
    "performer": [
        "Practitioner",
        "Organization",
        "Device",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "reason-reference": [
        "Condition",
        "Observation",
        "Procedure",
        "DiagnosticReport",
        "DocumentReference",
    ],
    "subject": ["Group", "Patient"],
}
