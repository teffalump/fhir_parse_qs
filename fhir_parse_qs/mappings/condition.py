__all__=['condition_mapping', 'condition_references']

condition_mapping = {
    'code': 'token',
    'identifier': 'token',
    'patient': 'reference',
    'abatement-age': 'quantity',
    'abatement-boolean': 'token',
    'abatement-date': 'date',
    'abatement-string': 'string',
    'asserted-date': 'date',
    'asserter': 'reference',
    'body-site': 'token',
    'category': 'token',
    'clinical-status': 'token',
    'context': 'reference',
    'encounter': 'reference',
    'evidence': 'token',
    'evidence-detail': 'reference',
    'onset-age': 'quantity',
    'onset-date': 'date',
    'onset-info': 'string',
    'severity': 'token',
    'stage': 'token',
    'subject': 'reference',
    'verification-status': 'token',
    }

condition_references = {
    'patient': [ 'Patient' ],
    'asserter': [ 'Practitioner', 'Patient', 'RelatedPerson' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'encounter': [ 'Encounter' ],
    'evidence-detail': [ 'Account', 'ActivityDefinition', 'AdverseEvent', 'AllergyIntolerance', 'Appointment', 'AppointmentResponse', 'AuditEvent', 'Basic', 'Binary', 'BodySite', 'Bundle', 'CapabilityStatement', 'CarePlan', 'CareTeam', 'ChargeItem', 'Claim', 'ClaimResponse', 'ClinicalImpression', 'CodeSystem', 'Communication', 'CommunicationRequest', 'CompartmentDefinition', 'Composition', 'ConceptMap', 'Condition', 'Consent', 'Contract', 'Coverage', 'DataElement', 'DetectedIssue', 'Device', 'DeviceComponent', 'DeviceMetric', 'DeviceRequest', 'DeviceUseStatement', 'DiagnosticReport', 'DocumentManifest', 'DocumentReference', 'EligibilityRequest', 'EligibilityResponse', 'Encounter', 'Endpoint', 'EnrollmentRequest', 'EnrollmentResponse', 'EpisodeOfCare', 'ExpansionProfile', 'ExplanationOfBenefit', 'FamilyMemberHistory', 'Flag', 'Goal', 'GraphDefinition', 'Group', 'GuidanceResponse', 'HealthcareService', 'ImagingManifest', 'ImagingStudy', 'Immunization', 'ImmunizationRecommendation', 'ImplementationGuide', 'Library', 'Linkage', 'List', 'Location', 'Measure', 'MeasureReport', 'Media', 'Medication', 'MedicationAdministration', 'MedicationDispense', 'MedicationRequest', 'MedicationStatement', 'MessageDefinition', 'MessageHeader', 'NamingSystem', 'NutritionOrder', 'Observation', 'OperationDefinition', 'OperationOutcome', 'Organization', 'Patient', 'PaymentNotice', 'PaymentReconciliation', 'Person', 'PlanDefinition', 'Practitioner', 'PractitionerRole', 'Procedure', 'ProcedureRequest', 'ProcessRequest', 'ProcessResponse', 'Provenance', 'Questionnaire', 'QuestionnaireResponse', 'ReferralRequest', 'RelatedPerson', 'RequestGroup', 'ResearchStudy', 'ResearchSubject', 'RiskAssessment', 'Schedule', 'SearchParameter', 'Sequence', 'ServiceDefinition', 'Slot', 'Specimen', 'StructureDefinition', 'StructureMap', 'Subscription', 'Substance', 'SupplyDelivery', 'SupplyRequest', 'Task', 'TestReport', 'TestScript', 'ValueSet', 'VisionPrescription' ],
    'subject': [ 'Group', 'Patient' ],
    }
