__all__=['chargeitem_mapping', 'chargeitem_references']

chargeitem_mapping = {
    'account': 'reference',
    'code': 'token',
    'context': 'reference',
    'entered-date': 'date',
    'enterer': 'reference',
    'factor-override': 'number',
    'identifier': 'token',
    'occurrence': 'date',
    'participant-actor': 'reference',
    'participant-role': 'token',
    'patient': 'reference',
    'performing-organization': 'reference',
    'price-override': 'quantity',
    'quantity': 'quantity',
    'requesting-organization': 'reference',
    'service': 'reference',
    'subject': 'reference',
    }

chargeitem_references = {
    'account': [ 'Account' ],
    'context': [ 'EpisodeOfCare', 'Encounter' ],
    'enterer': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'participant-actor': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'patient': [ 'Patient' ],
    'performing-organization': [ 'Organization' ],
    'requesting-organization': [ 'Organization' ],
    'service': [ 'Immunization', 'MedicationDispense', 'SupplyDelivery', 'Observation', 'DiagnosticReport', 'ImagingStudy', 'MedicationAdministration', 'Procedure' ],
    'subject': [ 'Group', 'Patient' ],
    }
