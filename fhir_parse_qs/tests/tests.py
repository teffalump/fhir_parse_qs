qss = ['Patient?_list=42&gender=female',
        'AllergyIntolerance?patient=42&_list=$current-allergies',
        'Observation?subject.name=peter',
        'Procedure?date=ge2010-01-01&date=le2011-12-31',
        'Observation?code=http://loinc.org|1234-5&subject.name=peter',
        'Observation?filter=name eq http://loinc.org|1234-5 and subject.name co "peter"',
        'DiagnosticReport?result.code-value-quantity=http://loinc.org|2823-3$gt5.4|http://unitsofmeasure.org|mmol/L',
        'Patient?_has:Observation:patient:_has:AuditEvent:entity:user=MyUserId',
        'AllergyIntolerance?clinical-status=active&clinical-status:exists=false',
        'Condition?_text=(bone OR liver) and metastases',
        ]

