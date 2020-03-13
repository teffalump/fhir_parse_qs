__all__ = ["paymentnotice_mapping", "paymentnotice_references"]

paymentnotice_mapping = {
    "created": "date",
    "identifier": "token",
    "organization": "reference",
    "payment-status": "token",
    "provider": "reference",
    "request": "reference",
    "response": "reference",
    "statusdate": "date",
}

paymentnotice_references = {
    "organization": ["Organization"],
    "provider": ["Practitioner"],
    "request": [
        "Account",
        "ActivityDefinition",
        "AdverseEvent",
        "AllergyIntolerance",
        "Appointment",
        "AppointmentResponse",
        "AuditEvent",
        "Basic",
        "Binary",
        "BodySite",
        "Bundle",
        "CapabilityStatement",
        "CarePlan",
        "CareTeam",
        "ChargeItem",
        "Claim",
        "ClaimResponse",
        "ClinicalImpression",
        "CodeSystem",
        "Communication",
        "CommunicationRequest",
        "CompartmentDefinition",
        "Composition",
        "ConceptMap",
        "Condition",
        "Consent",
        "Contract",
        "Coverage",
        "DataElement",
        "DetectedIssue",
        "Device",
        "DeviceComponent",
        "DeviceMetric",
        "DeviceRequest",
        "DeviceUseStatement",
        "DiagnosticReport",
        "DocumentManifest",
        "DocumentReference",
        "EligibilityRequest",
        "EligibilityResponse",
        "Encounter",
        "Endpoint",
        "EnrollmentRequest",
        "EnrollmentResponse",
        "EpisodeOfCare",
        "ExpansionProfile",
        "ExplanationOfBenefit",
        "FamilyMemberHistory",
        "Flag",
        "Goal",
        "GraphDefinition",
        "Group",
        "GuidanceResponse",
        "HealthcareService",
        "ImagingManifest",
        "ImagingStudy",
        "Immunization",
        "ImmunizationRecommendation",
        "ImplementationGuide",
        "Library",
        "Linkage",
        "List",
        "Location",
        "Measure",
        "MeasureReport",
        "Media",
        "Medication",
        "MedicationAdministration",
        "MedicationDispense",
        "MedicationRequest",
        "MedicationStatement",
        "MessageDefinition",
        "MessageHeader",
        "NamingSystem",
        "NutritionOrder",
        "Observation",
        "OperationDefinition",
        "OperationOutcome",
        "Organization",
        "Patient",
        "PaymentNotice",
        "PaymentReconciliation",
        "Person",
        "PlanDefinition",
        "Practitioner",
        "PractitionerRole",
        "Procedure",
        "ProcedureRequest",
        "ProcessRequest",
        "ProcessResponse",
        "Provenance",
        "Questionnaire",
        "QuestionnaireResponse",
        "ReferralRequest",
        "RelatedPerson",
        "RequestGroup",
        "ResearchStudy",
        "ResearchSubject",
        "RiskAssessment",
        "Schedule",
        "SearchParameter",
        "Sequence",
        "ServiceDefinition",
        "Slot",
        "Specimen",
        "StructureDefinition",
        "StructureMap",
        "Subscription",
        "Substance",
        "SupplyDelivery",
        "SupplyRequest",
        "Task",
        "TestReport",
        "TestScript",
        "ValueSet",
        "VisionPrescription",
    ],
    "response": [
        "Account",
        "ActivityDefinition",
        "AdverseEvent",
        "AllergyIntolerance",
        "Appointment",
        "AppointmentResponse",
        "AuditEvent",
        "Basic",
        "Binary",
        "BodySite",
        "Bundle",
        "CapabilityStatement",
        "CarePlan",
        "CareTeam",
        "ChargeItem",
        "Claim",
        "ClaimResponse",
        "ClinicalImpression",
        "CodeSystem",
        "Communication",
        "CommunicationRequest",
        "CompartmentDefinition",
        "Composition",
        "ConceptMap",
        "Condition",
        "Consent",
        "Contract",
        "Coverage",
        "DataElement",
        "DetectedIssue",
        "Device",
        "DeviceComponent",
        "DeviceMetric",
        "DeviceRequest",
        "DeviceUseStatement",
        "DiagnosticReport",
        "DocumentManifest",
        "DocumentReference",
        "EligibilityRequest",
        "EligibilityResponse",
        "Encounter",
        "Endpoint",
        "EnrollmentRequest",
        "EnrollmentResponse",
        "EpisodeOfCare",
        "ExpansionProfile",
        "ExplanationOfBenefit",
        "FamilyMemberHistory",
        "Flag",
        "Goal",
        "GraphDefinition",
        "Group",
        "GuidanceResponse",
        "HealthcareService",
        "ImagingManifest",
        "ImagingStudy",
        "Immunization",
        "ImmunizationRecommendation",
        "ImplementationGuide",
        "Library",
        "Linkage",
        "List",
        "Location",
        "Measure",
        "MeasureReport",
        "Media",
        "Medication",
        "MedicationAdministration",
        "MedicationDispense",
        "MedicationRequest",
        "MedicationStatement",
        "MessageDefinition",
        "MessageHeader",
        "NamingSystem",
        "NutritionOrder",
        "Observation",
        "OperationDefinition",
        "OperationOutcome",
        "Organization",
        "Patient",
        "PaymentNotice",
        "PaymentReconciliation",
        "Person",
        "PlanDefinition",
        "Practitioner",
        "PractitionerRole",
        "Procedure",
        "ProcedureRequest",
        "ProcessRequest",
        "ProcessResponse",
        "Provenance",
        "Questionnaire",
        "QuestionnaireResponse",
        "ReferralRequest",
        "RelatedPerson",
        "RequestGroup",
        "ResearchStudy",
        "ResearchSubject",
        "RiskAssessment",
        "Schedule",
        "SearchParameter",
        "Sequence",
        "ServiceDefinition",
        "Slot",
        "Specimen",
        "StructureDefinition",
        "StructureMap",
        "Subscription",
        "Substance",
        "SupplyDelivery",
        "SupplyRequest",
        "Task",
        "TestReport",
        "TestScript",
        "ValueSet",
        "VisionPrescription",
    ],
}
