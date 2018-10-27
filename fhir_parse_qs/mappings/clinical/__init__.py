__all__=['clinical_types', 'clinical_references']

from .allergy_intolerance import mapping as ai
from .allergy_intolerance import references as r_ai
from .condition import mapping as condition
from .condition import references as r_condition
from .care_plan import mapping as cp
from .care_plan import references as r_cp
from .care_team import mapping as ct
from .care_team import references as r_ct
from .diagnostic_report import mapping as dr
from .diagnostic_report import references as r_dr
from .family_member_history import mapping as fm
from .family_member_history import references as r_fm
from .imaging_study import mapping as img
from .imaging_study import references as r_img
from .immunization import mapping as im
from .immunization import references as r_im
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
from .procedure import mapping as proc
from .procedure import references as r_proc
from .procedure_request import mapping as procr
from .procedure_request import references as r_procr
from .questionnaire_response import mapping as qr
from .questionnaire_response import references as r_qr

clinical_types = {
        'AllergyIntolerance': ai,
        'Condition': condition,
        'CarePlan': cp,
        'CareTeam': ct,
        'DiagnosticReport': dr,
        'FamilyMemberHistory': fm,
        'ImagingStudy': img,
        'Immunization': im,
        'Medication': m,
        'MedicationAdministration': ma,
        'MedicationDispense': md,
        'MedicationRequest': mr,
        'MedicationStatement': ms,
        'Observation': obs,
        'Procedure': proc,
        'ProcedureRequest': procr,
        'QuestionnaireResponse': qr,
        }

clinical_references = {
        'AllergyIntolerance': r_ai,
        'Condition': r_condition,
        'CarePlan': r_cp,
        'CareTeam': r_ct,
        'DiagnosticReport': r_dr,
        'FamilyMemberHistory': r_fm,
        'ImagingStudy': r_img,
        'Immunization': r_im,
        'Medication': r_m,
        'MedicationAdministration': r_ma,
        'MedicationDispense': r_md,
        'MedicationRequest': r_mr,
        'MedicationStatement': r_ms,
        'Observation': r_obs,
        'Procedure': r_proc,
        'ProcedureRequest': r_procr,
        'QuestionnaireResponse': r_qr,
        }
