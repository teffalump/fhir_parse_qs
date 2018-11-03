__all__=['appointment_mapping', 'appointment_references']

appointment_mapping = {
    'actor': 'reference',
    'appointment-type': 'token',
    'date': 'date',
    'identifier': 'token',
    'incomingreferral': 'reference',
    'location': 'reference',
    'part-status': 'token',
    'patient': 'reference',
    'practitioner': 'reference',
    'service-type': 'token',
    'status': 'token',
    }

appointment_references = {
    'actor': [ 'Practitioner', 'Device', 'Patient', 'HealthcareService', 'RelatedPerson', 'Location' ],
    'incomingreferral': [ 'ReferralRequest' ],
    'location': [ 'Location' ],
    'patient': [ 'Patient' ],
    'practitioner': [ 'Practitioner' ],
    }
