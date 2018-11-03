__all__=['medication_mapping', 'medication_references']

medication_mapping = {
    'code': 'token',
    'container': 'token',
    'form': 'token',
    'ingredient': 'reference',
    'ingredient-code': 'token',
    'manufacturer': 'reference',
    'over-the-counter': 'token',
    'package-item': 'reference',
    'package-item-code': 'token',
    'status': 'token',
    }

medication_references = {
    'ingredient': [ 'Medication', 'Substance' ],
    'manufacturer': [ 'Organization' ],
    'package-item': [ 'Medication' ],
    }
