__all__=['search_parameters']

from .common import (control_parameters, common_parameters)
from .allergy_intolerance import mapping as ai
from .appointment import mapping as appt
from .appointment_response import mapping as apptr
from .condition import mapping as condition
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
from .organization import mapping as org
from .patient import mapping as patient
from .practitioner import mapping as hp
from .procedure import mapping as proc
from .questionnaire import mapping as q
from .questionnaire_response import mapping as qr
from .schedule import mapping as sch
from .slot import mapping as slot


search_parameters = {
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
        'Questionnaire': q,
        'QuestionnaireResponse': qr,
        'Schedule': sch,
        'Slot': slot,
        }
