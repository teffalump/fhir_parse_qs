__all__=['foundation_types', 'foundation_references']

from .document_reference import mapping as docr
from .document_reference import references as r_docr

foundation_types = {
        'DocumentReference': docr,
        }

foundation_references = {
        'DocumentReference': r_docr,
        }
