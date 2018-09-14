__all__=['search_parameters']

from .common import (control_parameters, common_parameters)
from .allergy_intolerance import mapping as ai
from .condition import mapping as condition
from .diagnostic_report import mapping as dr
from .family_member_history import mapping as fm
from .imaging_study import mapping as im
from .observation import mapping as obs
from .patient import mapping as patient
from .practitioner import mapping as hp
from .procedure import mapping as proc
from .questionnaire import mapping as q
from .questionnaire_response import mapping as qr


search_parameters = {
        'ctrl_parameters': control_parameters,
        'common_parameters': common_parameters,
        'AllergyIntolerance': ai,
        'Condition': condition,
        'DiagnosticReport': dr,
        'FamilyMemberHistory': fm,
        'ImagingStudy': im,
        'Observation': obs,
        'Patient': patient,
        'Practitioner': hp,
        'Procedure': proc,
        'Questionnaire': q,
        'QuestionnaireResponse': qr,
        }
