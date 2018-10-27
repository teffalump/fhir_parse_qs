mapping = {
        'actor': 'reference',
        'appointment-type':  'token',
        'date':  'date',
        'identifier':  'token',
        'incomingreferral':  'reference',
        'location':  'reference',
        'part-status':  'token',
        'patient':  'reference',
        'practitioner':  'reference',
        'service-type':  'token',
        'status':  'token',
        }

references = {
        'actor': ['Practitioner', 'Device', 'Patient', 'HealthcareService', 'RelatedPerson', 'Location'],
        'incomingreferral': ['ReferralRequest'],
        'location': ['Location'],
        'patient': ['Patient'],
        'practitioner': ['Practitioner'],
        }
