__all__=['encounter_mapping', 'encounter_references']

encounter_mapping = {
    'date': 'date',
    'identifier': 'token',
    'patient': 'reference',
    'type': 'token',
    'appointment': 'reference',
    'class': 'token',
    'diagnosis': 'reference',
    'episodeofcare': 'reference',
    'incomingreferral': 'reference',
    'length': 'number',
    'location': 'reference',
    'location-period': 'date',
    'part-of': 'reference',
    'participant': 'reference',
    'participant-type': 'token',
    'practitioner': 'reference',
    'reason': 'token',
    'service-provider': 'reference',
    'special-arrangement': 'token',
    'status': 'token',
    'subject': 'reference',
    }

encounter_references = {
    'patient': [ 'Patient' ],
    'appointment': [ 'Appointment' ],
    'diagnosis': [ 'Condition', 'Procedure' ],
    'episodeofcare': [ 'EpisodeOfCare' ],
    'incomingreferral': [ 'ReferralRequest' ],
    'location': [ 'Location' ],
    'part-of': [ 'Encounter' ],
    'participant': [ 'Practitioner', 'RelatedPerson' ],
    'practitioner': [ 'Practitioner' ],
    'service-provider': [ 'Organization' ],
    'subject': [ 'Group', 'Patient' ],
    }
