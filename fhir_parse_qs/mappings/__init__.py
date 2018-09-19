__all__=['search_types', 'search_references']

from .common import (control_parameters, common_parameters)
from .allergy_intolerance import mapping as ai
from .allergy_intolerance import references as r_ai
from .appointment import mapping as appt
from .appointment import references as r_appt
from .appointment_response import mapping as apptr
from .appointment_response import references as r_apptr
from .condition import mapping as condition
from .condition import references as r_condition
from .diagnostic_report import mapping as dr
from .diagnostic_report import references as r_dr
from .encounter import mapping as enc
from .encounter import references as r_enc
from .family_member_history import mapping as fm
from .imaging_study import mapping as img
from .immunization import mapping as im
from .location import mapping as loc
from. medication import mapping as m
from .medication_administration import mapping as ma
from .medication_dispense import mapping as md
from .medication_request import mapping as mr
from .medication_statement import mapping as ms
from .observation import mapping as obs
from .observation import references as r_obs
from .organization import mapping as org
from .patient import mapping as patient
from .patient import references as r_patient
from .practitioner import mapping as hp
from .procedure import mapping as proc
from .procedure_request import mapping as procr
from .questionnaire import mapping as q
from .questionnaire_response import mapping as qr
from .schedule import mapping as sch
from .slot import mapping as slot

search_types = {
        'ctrl_parameters': control_parameters,
        'common_parameters': common_parameters,
        'AllergyIntolerance': ai,
        'Appointment': appt,
        'AppointmentResponse': apptr,
        'Condition': condition,
        'DiagnosticReport': dr,
        'Encounter': enc,
        'FamilyMemberHistory': fm,
        'ImagingStudy': img,
        'Immunization': im,
        'Location': loc,
        'Medication': m,
        'MedicationAdministration': ma,
        'MedicationDispense': md,
        'MedicationRequest': mr,
        'MedicationStatement': ms,
        'Observation': obs,
        'Organization': org,
        'Patient': patient,
        'Practitioner': hp,
        'Procedure': proc,
        'ProcedureRequest': procr,
        'Questionnaire': q,
        'QuestionnaireResponse': qr,
        'Schedule': sch,
        'Slot': slot,
        }

search_references = {
        'AllergyIntolerance': r_ai,
        'Appointment': r_appt,
        'AppointmentResponse': r_apptr,
        'Condition': r_condition,
        'DiagnosticReport': r_dr,
        'Encounter': r_enc,
        'FamilyMemberHistory': None,
        'ImagingStudy': None,
        'Immunization': None,
        'Location': None,
        'Medication': None,
        'MedicationAdministration': None,
        'MedicationDispense': None,
        'MedicationRequest': None,
        'MedicationStatement': None,
        'Observation': r_obs,
        'Organization': None,
        'Patient': r_patient,
        'Practitioner': None,
        'Procedure': None,
        'ProcedureRequest': None,
        'Questionnaire': None,
        'QuestionnaireResponse': None,
        'Schedule': None,
        'Slot': None,
        }
