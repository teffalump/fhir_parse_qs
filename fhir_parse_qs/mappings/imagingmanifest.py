__all__=['imagingmanifest_mapping', 'imagingmanifest_references']

imagingmanifest_mapping = {
    'patient': 'reference',
    'author': 'reference',
    'authoring-time': 'date',
    'endpoint': 'reference',
    'identifier': 'token',
    'imaging-study': 'reference',
    'selected-study': 'uri',
    }

imagingmanifest_references = {
    'patient': [ 'Patient' ],
    'author': [ 'Practitioner', 'Organization', 'Device', 'Patient', 'RelatedPerson' ],
    'endpoint': [ 'Endpoint' ],
    'imaging-study': [ 'ImagingStudy' ],
    }
