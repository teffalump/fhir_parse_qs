__all__ = ["search_types", "search_references"]

from .account import account_mapping, account_references
from .activitydefinition import (
    activitydefinition_mapping,
    activitydefinition_references,
)
from .adverseevent import adverseevent_mapping, adverseevent_references
from .allergyintolerance import (
    allergyintolerance_mapping,
    allergyintolerance_references,
)
from .appointment import appointment_mapping, appointment_references
from .appointmentresponse import (
    appointmentresponse_mapping,
    appointmentresponse_references,
)
from .auditevent import auditevent_mapping, auditevent_references
from .basic import basic_mapping, basic_references
from .binary import binary_mapping, binary_references
from .bodysite import bodysite_mapping, bodysite_references
from .bundle import bundle_mapping, bundle_references
from .capabilitystatement import (
    capabilitystatement_mapping,
    capabilitystatement_references,
)
from .careplan import careplan_mapping, careplan_references
from .careteam import careteam_mapping, careteam_references
from .chargeitem import chargeitem_mapping, chargeitem_references
from .claim import claim_mapping, claim_references
from .claimresponse import claimresponse_mapping, claimresponse_references
from .clinicalimpression import (
    clinicalimpression_mapping,
    clinicalimpression_references,
)
from .codesystem import codesystem_mapping, codesystem_references
from .communication import communication_mapping, communication_references
from .communicationrequest import (
    communicationrequest_mapping,
    communicationrequest_references,
)
from .compartmentdefinition import (
    compartmentdefinition_mapping,
    compartmentdefinition_references,
)
from .composition import composition_mapping, composition_references
from .conceptmap import conceptmap_mapping, conceptmap_references
from .condition import condition_mapping, condition_references
from .consent import consent_mapping, consent_references
from .contract import contract_mapping, contract_references
from .coverage import coverage_mapping, coverage_references
from .dataelement import dataelement_mapping, dataelement_references
from .detectedissue import detectedissue_mapping, detectedissue_references
from .device import device_mapping, device_references
from .devicecomponent import devicecomponent_mapping, devicecomponent_references
from .devicemetric import devicemetric_mapping, devicemetric_references
from .devicerequest import devicerequest_mapping, devicerequest_references
from .deviceusestatement import (
    deviceusestatement_mapping,
    deviceusestatement_references,
)
from .diagnosticreport import diagnosticreport_mapping, diagnosticreport_references
from .documentmanifest import documentmanifest_mapping, documentmanifest_references
from .documentreference import documentreference_mapping, documentreference_references
from .eligibilityrequest import (
    eligibilityrequest_mapping,
    eligibilityrequest_references,
)
from .eligibilityresponse import (
    eligibilityresponse_mapping,
    eligibilityresponse_references,
)
from .encounter import encounter_mapping, encounter_references
from .endpoint import endpoint_mapping, endpoint_references
from .enrollmentrequest import enrollmentrequest_mapping, enrollmentrequest_references
from .enrollmentresponse import (
    enrollmentresponse_mapping,
    enrollmentresponse_references,
)
from .episodeofcare import episodeofcare_mapping, episodeofcare_references
from .expansionprofile import expansionprofile_mapping, expansionprofile_references
from .explanationofbenefit import (
    explanationofbenefit_mapping,
    explanationofbenefit_references,
)
from .familymemberhistory import (
    familymemberhistory_mapping,
    familymemberhistory_references,
)
from .flag import flag_mapping, flag_references
from .goal import goal_mapping, goal_references
from .graphdefinition import graphdefinition_mapping, graphdefinition_references
from .group import group_mapping, group_references
from .guidanceresponse import guidanceresponse_mapping, guidanceresponse_references
from .healthcareservice import healthcareservice_mapping, healthcareservice_references
from .imagingmanifest import imagingmanifest_mapping, imagingmanifest_references
from .imagingstudy import imagingstudy_mapping, imagingstudy_references
from .immunization import immunization_mapping, immunization_references
from .immunizationrecommendation import (
    immunizationrecommendation_mapping,
    immunizationrecommendation_references,
)
from .implementationguide import (
    implementationguide_mapping,
    implementationguide_references,
)
from .library import library_mapping, library_references
from .linkage import linkage_mapping, linkage_references
from .list import list_mapping, list_references
from .location import location_mapping, location_references
from .measure import measure_mapping, measure_references
from .measurereport import measurereport_mapping, measurereport_references
from .media import media_mapping, media_references
from .medication import medication_mapping, medication_references
from .medicationadministration import (
    medicationadministration_mapping,
    medicationadministration_references,
)
from .medicationdispense import (
    medicationdispense_mapping,
    medicationdispense_references,
)
from .medicationrequest import medicationrequest_mapping, medicationrequest_references
from .medicationstatement import (
    medicationstatement_mapping,
    medicationstatement_references,
)
from .messagedefinition import messagedefinition_mapping, messagedefinition_references
from .messageheader import messageheader_mapping, messageheader_references
from .namingsystem import namingsystem_mapping, namingsystem_references
from .nutritionorder import nutritionorder_mapping, nutritionorder_references
from .observation import observation_mapping, observation_references
from .operationdefinition import (
    operationdefinition_mapping,
    operationdefinition_references,
)
from .organization import organization_mapping, organization_references
from .patient import patient_mapping, patient_references
from .paymentnotice import paymentnotice_mapping, paymentnotice_references
from .paymentreconciliation import (
    paymentreconciliation_mapping,
    paymentreconciliation_references,
)
from .person import person_mapping, person_references
from .plandefinition import plandefinition_mapping, plandefinition_references
from .practitioner import practitioner_mapping, practitioner_references
from .practitionerrole import practitionerrole_mapping, practitionerrole_references
from .procedure import procedure_mapping, procedure_references
from .procedurerequest import procedurerequest_mapping, procedurerequest_references
from .processrequest import processrequest_mapping, processrequest_references
from .processresponse import processresponse_mapping, processresponse_references
from .provenance import provenance_mapping, provenance_references
from .questionnaire import questionnaire_mapping, questionnaire_references
from .questionnaireresponse import (
    questionnaireresponse_mapping,
    questionnaireresponse_references,
)
from .referralrequest import referralrequest_mapping, referralrequest_references
from .relatedperson import relatedperson_mapping, relatedperson_references
from .requestgroup import requestgroup_mapping, requestgroup_references
from .researchstudy import researchstudy_mapping, researchstudy_references
from .researchsubject import researchsubject_mapping, researchsubject_references
from .riskassessment import riskassessment_mapping, riskassessment_references
from .schedule import schedule_mapping, schedule_references
from .searchparameter import searchparameter_mapping, searchparameter_references
from .sequence import sequence_mapping, sequence_references
from .servicedefinition import servicedefinition_mapping, servicedefinition_references
from .slot import slot_mapping, slot_references
from .specimen import specimen_mapping, specimen_references
from .structuredefinition import (
    structuredefinition_mapping,
    structuredefinition_references,
)
from .structuremap import structuremap_mapping, structuremap_references
from .subscription import subscription_mapping, subscription_references
from .substance import substance_mapping, substance_references
from .supplydelivery import supplydelivery_mapping, supplydelivery_references
from .supplyrequest import supplyrequest_mapping, supplyrequest_references
from .task import task_mapping, task_references
from .testreport import testreport_mapping, testreport_references
from .testscript import testscript_mapping, testscript_references
from .valueset import valueset_mapping, valueset_references
from .visionprescription import (
    visionprescription_mapping,
    visionprescription_references,
)
from .common import common_mapping, common_references
from .control import control_mapping, control_references

search_types = {
    "Account": account_mapping,
    "ActivityDefinition": activitydefinition_mapping,
    "AdverseEvent": adverseevent_mapping,
    "AllergyIntolerance": allergyintolerance_mapping,
    "Appointment": appointment_mapping,
    "AppointmentResponse": appointmentresponse_mapping,
    "AuditEvent": auditevent_mapping,
    "Basic": basic_mapping,
    "Binary": binary_mapping,
    "BodySite": bodysite_mapping,
    "Bundle": bundle_mapping,
    "CapabilityStatement": capabilitystatement_mapping,
    "CarePlan": careplan_mapping,
    "CareTeam": careteam_mapping,
    "ChargeItem": chargeitem_mapping,
    "Claim": claim_mapping,
    "ClaimResponse": claimresponse_mapping,
    "ClinicalImpression": clinicalimpression_mapping,
    "CodeSystem": codesystem_mapping,
    "Communication": communication_mapping,
    "CommunicationRequest": communicationrequest_mapping,
    "CompartmentDefinition": compartmentdefinition_mapping,
    "Composition": composition_mapping,
    "ConceptMap": conceptmap_mapping,
    "Condition": condition_mapping,
    "Consent": consent_mapping,
    "Contract": contract_mapping,
    "Coverage": coverage_mapping,
    "DataElement": dataelement_mapping,
    "DetectedIssue": detectedissue_mapping,
    "Device": device_mapping,
    "DeviceComponent": devicecomponent_mapping,
    "DeviceMetric": devicemetric_mapping,
    "DeviceRequest": devicerequest_mapping,
    "DeviceUseStatement": deviceusestatement_mapping,
    "DiagnosticReport": diagnosticreport_mapping,
    "DocumentManifest": documentmanifest_mapping,
    "DocumentReference": documentreference_mapping,
    "EligibilityRequest": eligibilityrequest_mapping,
    "EligibilityResponse": eligibilityresponse_mapping,
    "Encounter": encounter_mapping,
    "Endpoint": endpoint_mapping,
    "EnrollmentRequest": enrollmentrequest_mapping,
    "EnrollmentResponse": enrollmentresponse_mapping,
    "EpisodeOfCare": episodeofcare_mapping,
    "ExpansionProfile": expansionprofile_mapping,
    "ExplanationOfBenefit": explanationofbenefit_mapping,
    "FamilyMemberHistory": familymemberhistory_mapping,
    "Flag": flag_mapping,
    "Goal": goal_mapping,
    "GraphDefinition": graphdefinition_mapping,
    "Group": group_mapping,
    "GuidanceResponse": guidanceresponse_mapping,
    "HealthcareService": healthcareservice_mapping,
    "ImagingManifest": imagingmanifest_mapping,
    "ImagingStudy": imagingstudy_mapping,
    "Immunization": immunization_mapping,
    "ImmunizationRecommendation": immunizationrecommendation_mapping,
    "ImplementationGuide": implementationguide_mapping,
    "Library": library_mapping,
    "Linkage": linkage_mapping,
    "List": list_mapping,
    "Location": location_mapping,
    "Measure": measure_mapping,
    "MeasureReport": measurereport_mapping,
    "Media": media_mapping,
    "Medication": medication_mapping,
    "MedicationAdministration": medicationadministration_mapping,
    "MedicationDispense": medicationdispense_mapping,
    "MedicationRequest": medicationrequest_mapping,
    "MedicationStatement": medicationstatement_mapping,
    "MessageDefinition": messagedefinition_mapping,
    "MessageHeader": messageheader_mapping,
    "NamingSystem": namingsystem_mapping,
    "NutritionOrder": nutritionorder_mapping,
    "Observation": observation_mapping,
    "OperationDefinition": operationdefinition_mapping,
    "Organization": organization_mapping,
    "Patient": patient_mapping,
    "PaymentNotice": paymentnotice_mapping,
    "PaymentReconciliation": paymentreconciliation_mapping,
    "Person": person_mapping,
    "PlanDefinition": plandefinition_mapping,
    "Practitioner": practitioner_mapping,
    "PractitionerRole": practitionerrole_mapping,
    "Procedure": procedure_mapping,
    "ProcedureRequest": procedurerequest_mapping,
    "ProcessRequest": processrequest_mapping,
    "ProcessResponse": processresponse_mapping,
    "Provenance": provenance_mapping,
    "Questionnaire": questionnaire_mapping,
    "QuestionnaireResponse": questionnaireresponse_mapping,
    "ReferralRequest": referralrequest_mapping,
    "RelatedPerson": relatedperson_mapping,
    "RequestGroup": requestgroup_mapping,
    "ResearchStudy": researchstudy_mapping,
    "ResearchSubject": researchsubject_mapping,
    "RiskAssessment": riskassessment_mapping,
    "Schedule": schedule_mapping,
    "SearchParameter": searchparameter_mapping,
    "Sequence": sequence_mapping,
    "ServiceDefinition": servicedefinition_mapping,
    "Slot": slot_mapping,
    "Specimen": specimen_mapping,
    "StructureDefinition": structuredefinition_mapping,
    "StructureMap": structuremap_mapping,
    "Subscription": subscription_mapping,
    "Substance": substance_mapping,
    "SupplyDelivery": supplydelivery_mapping,
    "SupplyRequest": supplyrequest_mapping,
    "Task": task_mapping,
    "TestReport": testreport_mapping,
    "TestScript": testscript_mapping,
    "ValueSet": valueset_mapping,
    "VisionPrescription": visionprescription_mapping,
    "common": common_mapping,
    "control": control_mapping,
}

search_references = {
    "Account": account_references,
    "ActivityDefinition": activitydefinition_references,
    "AdverseEvent": adverseevent_references,
    "AllergyIntolerance": allergyintolerance_references,
    "Appointment": appointment_references,
    "AppointmentResponse": appointmentresponse_references,
    "AuditEvent": auditevent_references,
    "Basic": basic_references,
    "Binary": binary_references,
    "BodySite": bodysite_references,
    "Bundle": bundle_references,
    "CapabilityStatement": capabilitystatement_references,
    "CarePlan": careplan_references,
    "CareTeam": careteam_references,
    "ChargeItem": chargeitem_references,
    "Claim": claim_references,
    "ClaimResponse": claimresponse_references,
    "ClinicalImpression": clinicalimpression_references,
    "CodeSystem": codesystem_references,
    "Communication": communication_references,
    "CommunicationRequest": communicationrequest_references,
    "CompartmentDefinition": compartmentdefinition_references,
    "Composition": composition_references,
    "ConceptMap": conceptmap_references,
    "Condition": condition_references,
    "Consent": consent_references,
    "Contract": contract_references,
    "Coverage": coverage_references,
    "DataElement": dataelement_references,
    "DetectedIssue": detectedissue_references,
    "Device": device_references,
    "DeviceComponent": devicecomponent_references,
    "DeviceMetric": devicemetric_references,
    "DeviceRequest": devicerequest_references,
    "DeviceUseStatement": deviceusestatement_references,
    "DiagnosticReport": diagnosticreport_references,
    "DocumentManifest": documentmanifest_references,
    "DocumentReference": documentreference_references,
    "EligibilityRequest": eligibilityrequest_references,
    "EligibilityResponse": eligibilityresponse_references,
    "Encounter": encounter_references,
    "Endpoint": endpoint_references,
    "EnrollmentRequest": enrollmentrequest_references,
    "EnrollmentResponse": enrollmentresponse_references,
    "EpisodeOfCare": episodeofcare_references,
    "ExpansionProfile": expansionprofile_references,
    "ExplanationOfBenefit": explanationofbenefit_references,
    "FamilyMemberHistory": familymemberhistory_references,
    "Flag": flag_references,
    "Goal": goal_references,
    "GraphDefinition": graphdefinition_references,
    "Group": group_references,
    "GuidanceResponse": guidanceresponse_references,
    "HealthcareService": healthcareservice_references,
    "ImagingManifest": imagingmanifest_references,
    "ImagingStudy": imagingstudy_references,
    "Immunization": immunization_references,
    "ImmunizationRecommendation": immunizationrecommendation_references,
    "ImplementationGuide": implementationguide_references,
    "Library": library_references,
    "Linkage": linkage_references,
    "List": list_references,
    "Location": location_references,
    "Measure": measure_references,
    "MeasureReport": measurereport_references,
    "Media": media_references,
    "Medication": medication_references,
    "MedicationAdministration": medicationadministration_references,
    "MedicationDispense": medicationdispense_references,
    "MedicationRequest": medicationrequest_references,
    "MedicationStatement": medicationstatement_references,
    "MessageDefinition": messagedefinition_references,
    "MessageHeader": messageheader_references,
    "NamingSystem": namingsystem_references,
    "NutritionOrder": nutritionorder_references,
    "Observation": observation_references,
    "OperationDefinition": operationdefinition_references,
    "Organization": organization_references,
    "Patient": patient_references,
    "PaymentNotice": paymentnotice_references,
    "PaymentReconciliation": paymentreconciliation_references,
    "Person": person_references,
    "PlanDefinition": plandefinition_references,
    "Practitioner": practitioner_references,
    "PractitionerRole": practitionerrole_references,
    "Procedure": procedure_references,
    "ProcedureRequest": procedurerequest_references,
    "ProcessRequest": processrequest_references,
    "ProcessResponse": processresponse_references,
    "Provenance": provenance_references,
    "Questionnaire": questionnaire_references,
    "QuestionnaireResponse": questionnaireresponse_references,
    "ReferralRequest": referralrequest_references,
    "RelatedPerson": relatedperson_references,
    "RequestGroup": requestgroup_references,
    "ResearchStudy": researchstudy_references,
    "ResearchSubject": researchsubject_references,
    "RiskAssessment": riskassessment_references,
    "Schedule": schedule_references,
    "SearchParameter": searchparameter_references,
    "Sequence": sequence_references,
    "ServiceDefinition": servicedefinition_references,
    "Slot": slot_references,
    "Specimen": specimen_references,
    "StructureDefinition": structuredefinition_references,
    "StructureMap": structuremap_references,
    "Subscription": subscription_references,
    "Substance": substance_references,
    "SupplyDelivery": supplydelivery_references,
    "SupplyRequest": supplyrequest_references,
    "Task": task_references,
    "TestReport": testreport_references,
    "TestScript": testscript_references,
    "ValueSet": valueset_references,
    "VisionPrescription": visionprescription_references,
    "common": common_references,
    "control": control_references,
}
