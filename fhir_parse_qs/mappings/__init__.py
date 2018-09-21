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
from .family_member_history import references as r_fm
from .imaging_study import mapping as img
from .imaging_study import references as r_img
from .immunization import mapping as im
from .immunization import references as r_im
from .location import mapping as loc
from .location import references as r_loc
from. medication import mapping as m
from. medication import references as r_m
from .medication_administration import mapping as ma
from .medication_administration import references as r_ma
from .medication_dispense import mapping as md
from .medication_dispense import references as r_md
from .medication_request import mapping as mr
from .medication_request import references as r_mr
from .medication_statement import mapping as ms
from .medication_statement import references as r_ms
from .observation import mapping as obs
from .observation import references as r_obs
from .organization import mapping as org
from .organization import references as r_org
from .patient import mapping as patient
from .patient import references as r_patient
from .practitioner import mapping as hp
from .practitioner import references as r_hp
from .procedure import mapping as proc
from .procedure import references as r_proc
from .procedure_request import mapping as procr
from .procedure_request import references as r_procr
from .questionnaire import mapping as q
from .questionnaire import references as r_q
from .questionnaire_response import mapping as qr
from .questionnaire_response import references as r_qr
from .schedule import mapping as sch
from .schedule import references as r_sch
from .slot import mapping as slot
from .slot import references as r_slot

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
        'FamilyMemberHistory': r_fm,
        'ImagingStudy': r_img,
        'Immunization': r_im,
        'Location': r_loc,
        'Medication': r_m,
        'MedicationAdministration': r_ma,
        'MedicationDispense': r_md,
        'MedicationRequest': r_mr,
        'MedicationStatement': r_ms,
        'Observation': r_obs,
        'Organization': r_org,
        'Patient': r_patient,
        'Practitioner': r_hp,
        'Procedure': r_proc,
        'ProcedureRequest': r_procr,
        'Questionnaire': r_q,
        'QuestionnaireResponse': r_qr,
        'Schedule': r_sch,
        'Slot': r_slot,
        }
