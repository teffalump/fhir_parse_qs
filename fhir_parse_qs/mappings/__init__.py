__all__=['search_parameters']

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
from .encounter import mapping as enc
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

search_parameters = {
        'ctrl_parameters': control_parameters,
        'common_parameters': common_parameters,
        'AllergyIntolerance': (ai, r_ai),
        'Appointment': (appt, r_appt),
        'AppointmentResponse': (apptr, r_apptr),
        'Condition': (condition, r_condition),
        'DiagnosticReport': (dr, None),
        'Encounter': (enc, None),
        'FamilyMemberHistory': (fm, None),
        'ImagingStudy': (img, None),
        'Immunization': (im, None),
        'Location': (loc, None),
        'Medication': (m, None),
        'MedicationAdministration': (ma, None),
        'MedicationDispense': (md, None),
        'MedicationRequest': (mr, None),
        'MedicationStatement': (ms, None),
        'Observation': (obs, r_obs),
        'Organization': (org, None),
        'Patient': (patient, r_patient),
        'Practitioner': (hp, None),
        'Procedure': (proc, None),
        'ProcedureRequest': (procr, None),
        'Questionnaire': (q, None),
        'QuestionnaireResponse': (qr, None),
        'Schedule': (sch, None),
        'Slot': (slot, None)
        }
