__all__ = ["observation_mapping", "observation_references"]

observation_mapping = {
    "code": "token",
    "date": "date",
    "identifier": "token",
    "patient": "reference",
    "encounter": "reference",
    "based-on": "reference",
    "category": "token",
    "combo-code": "token",
    "combo-data-absent-reason": "token",
    "combo-value-concept": "token",
    "combo-value-quantity": "quantity",
    "component-code": "token",
    "component-data-absent-reason": "token",
    "component-value-concept": "token",
    "component-value-quantity": "quantity",
    "data-absent-reason": "token",
    "derived-from": "reference",
    "device": "reference",
    "focus": "reference",
    "has-member": "reference",
    "method": "token",
    "part-of": "reference",
    "performer": "reference",
    "specimen": "reference",
    "status": "token",
    "subject": "reference",
    "value-concept": "token",
    "value-date": "date",
    "value-quantity": "quantity",
    "value-string": "string",
    "code-value-concept": "composite",
    "code-value-date": "composite",
    "code-value-quantity": "composite",
    "code-value-string": "composite",
    "combo-code-value-concept": "composite",
    "combo-code-value-quantity": "composite",
    "component-code-value-concept": "composite",
    "component-code-value-quantity": "composite",
}

observation_references = {
    "patient": ["Patient"],
    "encounter": ["Encounter"],
    "based-on": [
        "CarePlan",
        "MedicationRequest",
        "NutritionOrder",
        "DeviceRequest",
        "ServiceRequest",
        "ImmunizationRecommendation",
    ],
    "derived-from": [
        "Media",
        "Observation",
        "ImagingStudy",
        "MolecularSequence",
        "QuestionnaireResponse",
        "DocumentReference",
    ],
    "device": ["Device", "DeviceMetric"],
    "focus": [
        "Account",
        "ActivityDefinition",
        "AdverseEvent",
        "AllergyIntolerance",
        "Appointment",
        "AppointmentResponse",
        "AuditEvent",
        "Basic",
        "Binary",
        "BiologicallyDerivedProduct",
        "BodyStructure",
        "Bundle",
        "CapabilityStatement",
        "CarePlan",
        "CareTeam",
        "CatalogEntry",
        "ChargeItem",
        "ChargeItemDefinition",
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
        "CoverageEligibilityRequest",
        "CoverageEligibilityResponse",
        "DetectedIssue",
        "Device",
        "DeviceDefinition",
        "DeviceMetric",
        "DeviceRequest",
        "DeviceUseStatement",
        "DiagnosticReport",
        "DocumentManifest",
        "DocumentReference",
        "EffectEvidenceSynthesis",
        "Encounter",
        "Endpoint",
        "EnrollmentRequest",
        "EnrollmentResponse",
        "EpisodeOfCare",
        "EventDefinition",
        "Evidence",
        "EvidenceVariable",
        "ExampleScenario",
        "ExplanationOfBenefit",
        "FamilyMemberHistory",
        "Flag",
        "Goal",
        "GraphDefinition",
        "Group",
        "GuidanceResponse",
        "HealthcareService",
        "ImagingStudy",
        "Immunization",
        "ImmunizationEvaluation",
        "ImmunizationRecommendation",
        "ImplementationGuide",
        "InsurancePlan",
        "Invoice",
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
        "MedicationKnowledge",
        "MedicationRequest",
        "MedicationStatement",
        "MedicinalProduct",
        "MedicinalProductAuthorization",
        "MedicinalProductContraindication",
        "MedicinalProductIndication",
        "MedicinalProductIngredient",
        "MedicinalProductInteraction",
        "MedicinalProductManufactured",
        "MedicinalProductPackaged",
        "MedicinalProductPharmaceutical",
        "MedicinalProductUndesirableEffect",
        "MessageDefinition",
        "MessageHeader",
        "MolecularSequence",
        "NamingSystem",
        "NutritionOrder",
        "Observation",
        "ObservationDefinition",
        "OperationDefinition",
        "OperationOutcome",
        "Organization",
        "OrganizationAffiliation",
        "Patient",
        "PaymentNotice",
        "PaymentReconciliation",
        "Person",
        "PlanDefinition",
        "Practitioner",
        "PractitionerRole",
        "Procedure",
        "Provenance",
        "Questionnaire",
        "QuestionnaireResponse",
        "RelatedPerson",
        "RequestGroup",
        "ResearchDefinition",
        "ResearchElementDefinition",
        "ResearchStudy",
        "ResearchSubject",
        "RiskAssessment",
        "RiskEvidenceSynthesis",
        "Schedule",
        "SearchParameter",
        "ServiceRequest",
        "Slot",
        "Specimen",
        "SpecimenDefinition",
        "StructureDefinition",
        "StructureMap",
        "Subscription",
        "Substance",
        "SubstanceNucleicAcid",
        "SubstancePolymer",
        "SubstanceProtein",
        "SubstanceReferenceInformation",
        "SubstanceSourceMaterial",
        "SubstanceSpecification",
        "SupplyDelivery",
        "SupplyRequest",
        "Task",
        "TerminologyCapabilities",
        "TestReport",
        "TestScript",
        "ValueSet",
        "VerificationResult",
        "VisionPrescription",
    ],
    "has-member": ["Observation", "MolecularSequence", "QuestionnaireResponse"],
    "part-of": [
        "Immunization",
        "MedicationDispense",
        "MedicationAdministration",
        "Procedure",
        "ImagingStudy",
        "MedicationStatement",
    ],
    "performer": [
        "Practitioner",
        "Organization",
        "CareTeam",
        "Patient",
        "PractitionerRole",
        "RelatedPerson",
    ],
    "specimen": ["Specimen"],
    "subject": ["Group", "Device", "Patient", "Location"],
}
