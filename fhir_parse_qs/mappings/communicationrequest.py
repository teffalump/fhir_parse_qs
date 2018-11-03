__all__=['communicationrequest_mapping', 'communicationrequest_references']

communicationrequest_mapping = {
    'authored': 'date',
    'based-on': 'reference',
    'category': 'token',
    'context': 'reference',
    'encounter': 'reference',
    'group-identifier': 'token',
    'identifier': 'token',
    'medium': 'token',
    'occurrence': 'date',
    'patient': 'reference',
    'priority': 'token',
    'recipient': 'reference',
    'replaces': 'reference',
    'requester': 'reference',
    'sender': 'reference',
    'status': 'token',
    'subject': 'reference',
    }

communicationrequest_references = {
    'based-on': [ 'Account', 'ActivityDefinition', 'AdverseEvent', 'AllergyIntolerance', 'Appointment', 'AppointmentResponse', 'AuditEvent', 'Basic', 'Binary', 'BodySite', 'Bundle', 'CapabilityStatement', 'CarePlan', 'CareTeam', 'ChargeItem', 'Claim', 'ClaimResponse', 'ClinicalImpression', 'CodeSystem', 'Communication', 'CommunicationRequest', 'CompartmentDefinition', 'Composition', 'ConceptMap', 'Condition', 'Consent', 'Contract', 'Coverage', 'DataElement', 'DetectedIssue', 'Device', 'DeviceComponent', 'DeviceMetric', 'DeviceRequest', 'DeviceUseStatement', 'DiagnosticReport', 'DocumentManifest', 'DocumentReference', 'EligibilityRequest', 'EligibilityResponse', 'Encounter', 'Endpoint', 'EnrollmentRequest', 'EnrollmentResponse', 'EpisodeOfCare', 'ExpansionProfile', 'ExplanationOfBenefit', 'FamilyMemberHistory', 'Flag', 'Goal', 'GraphDefinition', 'Group', 'GuidanceResponse', 'HealthcareService', 'ImagingManifest', 'ImagingStudy', 'Immunization', 'ImmunizationRecommendation', 'ImplementationGuide', 'Library', 'Linkage', 'List', 'Location', 'Measure', 'MeasureReport', 'Media', 'Medication', 'MedicationAdministration', 'MedicationDispense', 'MedicationRequest', 'MedicationStatement', 'MessageDefinition', 'MessageHeader', 'NamingSystem', 'NutritionOrder', 'Observation', 'OperationDefinition', 'OperationOutcome', 'Organization', 'Patient', 'PaymentNotice', 'PaymentReconciliation', 'Person', 'PlanDefinition', 'Practitioner', 'PractitionerRole', 'Procedure', 'ProcedureRequest', 'ProcessRequest', 'ProcessResponse', 'Provenance', 'Questionnaire', 'QuestionnaireResponse', 'ReferralRequest', 'RelatedPerson', 'RequestGroup', 'ResearchStudy', 'ResearchSubject', 'RiskAssessment', 'Schedule', 'SearchParameter', 'Sequence', 'ServiceDefinition', 'Slot', 'Specimen', 'StructureDefinition', 'StructureMap', 'Subscription', 'Substance', 'SupplyDelivery', 'SupplyRequest', 'Task', 'TestReport', 'TestScript', 'ValueSet', 'VisionPrescription' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'encounter': [ 'Encounter' ],
    'patient': [ 'Patient' ],
    'recipient': [ 'Practitioner', 'Group', 'Organization', 'CareTeam', 'Device', 'Patient', 'RelatedPerson' ],
    'replaces': [ 'CommunicationRequest' ],
    'requester': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'sender': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'subject': [ 'Group', 'Patient' ],
    }
