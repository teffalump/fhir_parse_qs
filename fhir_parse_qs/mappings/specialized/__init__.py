__all__=['specialized_types', 'specialized_references']

from .questionnaire import mapping as q
from .questionnaire import references as r_q

specialized_types = {
        'Questionnaire': q,
        }

specialized_references = {
        'Questionnaire': r_q,
        }
