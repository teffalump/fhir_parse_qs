import unittest
from fhir_parse_qs import Search

qss = [
        ('Patient', 'gender=female'),
        ('Patient', '_list=42&gender=female'),
        ('AllergyIntolerance', 'patient=42&_list=$current-allergies'),
        ('Patient', 'given:contains=eve'),
        ('Procedure', 'date=ge2010-01-01&date=le2011-12-31'),
        ('Observation', 'subject.name=peter'),
        ('Observation', 'code=http://loinc.org|1234-5&subject.name=peter'),
        ('Observation', 'filter=name eq http://loinc.org|1234-5 and subject.name co "peter"'),
        ('DiagnosticReport', 'result.code-value-quantity=http://loinc.org|2823-3$gt5.4|http://unitsofmeasure.org|mmol/L'),
        ('Patient', '_has:Observation:patient:_has:AuditEvent:entity:user=MyUserId'),
        ('AllergyIntolerance', 'clinical-status=active&clinical-status:exists=false'),
        ('Condition', '_text=(bone OR liver) and metastases'),
        ]

class TestQS(unittest.TestCase):

    def test_basic(self):
        s = Search(*qss[0])
        assert len(s) == 1
        assert s.endpoint == 'Patient'
        assert not s.modifier
        assert not s.prefix

    def test_basic_plus(self):
        s = Search(*qss[1])
        assert s.endpoint == 'Patient'
        assert len(s) == 2
        assert s['_list'].value == '42'
        assert s['gender'].value == 'female'
        assert not s.modifier

    #def test_basic_plus2(self):
        #s = Search(*qss[2])
        #assert s.endpoint == 'AllergyIntolerance'
        #assert len(s) == 2
        #assert s['_list'].value == '$current_allergies'

    def test_mod(self):
        s = Search(*qss[3])
        assert s[0].modifier == 'contains'
        assert s[0].value == 'eve'
        assert s[0].parameter == 'given'
        assert not s.prefix

    def test_prefix(self):
        #TODO More
        s = Search(*qss[4])
        assert s.endpoint == 'Procedure'
        assert len(s) == 2
        assert len(s['date']) == 2
        assert 'ge' in s.prefix
        assert 'le' in s.prefix

    def test_or(self):
        s = Search(*qss[-1])
        assert s[0].value == '(bone OR liver) and metastases'
        assert s[0].parameter == '_text'

if __name__ == '__main__':
    unittest.main()
