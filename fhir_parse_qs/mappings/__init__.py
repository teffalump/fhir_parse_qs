__all__=['search_types', 'search_references']

from .common import (control_parameters, common_parameters)
from .foundation import (foundation_types, foundation_references)
from .clinical import (clinical_types, clinical_references)
from .specialized import (specialized_types, specialized_references)
from .base import (base_types, base_references)
from .financial import (financial_types, financial_references)

search_references = {}
search_types = {
        'ctrl_parameters': control_parameters,
        'common_parameters': common_parameters
        }

for t in (base_types, clinical_types, financial_types, foundation_types, specialized_types):
    search_types.update(t)

for r in (base_references, clinical_references, financial_references, foundation_references, specialized_references):
    search_references.update(r)
