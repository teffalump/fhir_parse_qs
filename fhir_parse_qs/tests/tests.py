import unittest
from fhir_parse_qs import Search

qss = [
        ('Patient', 'gender=female'),
        ('Patient', '_list=42&gender=female'),
        ('AllergyIntolerance', 'patient=42&_list=$current-allergies'),
        ('Observation', 'subject.name=peter'),
        ('Procedure', 'date=ge2010-01-01&date=le2011-12-31'),
        ('Observation', 'code=http://loinc.org|1234-5&subject.name=peter'),
        ('Observation', 'filter=name eq http://loinc.org|1234-5 and subject.name co "peter"'),
        ('DiagnosticReport', 'result.code-value-quantity=http://loinc.org|2823-3$gt5.4|http://unitsofmeasure.org|mmol/L'),
        ('Patient', '_has:Observation:patient:_has:AuditEvent:entity:user=MyUserId'),
        ('AllergyIntolerance', 'clinical-status=active&clinical-status:exists=false'),
        ('Condition', '_text=(bone OR liver) and metastases'),
        ]

class TestQS(unittest.TestCase):

    def test_basic(self):
        s = Search(qss[0][0], qss[0][1])
        assert len(s) == 1
        assert s.endpoint == 'Patient'

    def test_basic_plus(self):
        s = Search(qss[1][0], qss[1][1])
        assert s.endpoint == 'Patient'
        assert len(s) == 2
        assert s.endpoint == 'Patient'
        assert s['_list'].value == '42'
        assert s['gender'].value == 'female'
        assert not s.modifier

    def test_prefix(self):
        #TODO More
        s = Search(qss[4][0], qss[4][1])
        assert s.endpoint == 'Procedure'
        assert len(s) == 2
        assert len(s['date']) == 2
        assert 'ge' in s.prefix
        assert 'le' in s.prefix

if __name__ == '__main__':
    unittest.main()
