import unittest
from fhir_parse_qs import Search
from datetime import datetime
from pendulum import now

qss = [
        ('Observation', 'filter=name eq http://loinc.org|1234-5 and subject.name co "peter"'),
        ('DiagnosticReport', 'result.code-value-quantity=http://loinc.org|2823-3$gt5.4|http://unitsofmeasure.org|mmol/L'),
        #('Patient', '_has:Observation:patient:_has:AuditEvent:entity:user=MyUserId'),
        ]

class TestQS(unittest.TestCase):

    def test_not_supported(self):
        try:
            s = Search('Blark', 'eueu=aoeuaoeu')
            assert False
        except:
            assert True

    def test_unknown(self):
        s = Search('Patient', 'blank=female')
        assert len(s.error) == 1
        assert len(s) == 0


    def test_basic(self):
        s = Search('Patient', 'gender=female')
        assert len(s) == 1
        assert s.endpoint == 'Patient'
        assert not s.modifier
        assert not s.prefix

    def test_basic_plus(self):
        s = Search('Patient', '_count=42&gender=female')
        assert s.endpoint == 'Patient'
        assert len(s) == 2
        assert s['_count'].value == 42
        assert s['gender'].value == 'female'
        assert not s.modifier

    #def test_basic_plus2(self):
        #s = Search('AllergyIntolerance', 'patient=42')
        #assert s.endpoint == 'AllergyIntolerance'
        #assert len(s) == 2
        #assert s['_list'].value == '$current-allergies'

    def test_mod(self):
        s = Search('Patient', 'given:contains=eve')
        assert s[0].modifier == 'contains'
        assert s[0].value == 'eve'
        assert s[0].parameter == 'given'
        assert not s.prefix

    def test_prefix_cast(self):
        s = Search('Procedure', 'date=ge2010-01-01&date=le2011-12-31')
        assert s.endpoint == 'Procedure'
        assert len(s) == 2
        assert len(s['date']) == 2
        assert 'ge' in s.prefix
        assert 'le' in s.prefix
        n = now('Europe/London')
        assert isinstance(s['date'][0].value, datetime)
        assert s['date'][0].value < n
        assert isinstance(s['date'][1].value, datetime)
        assert s['date'][1].value < n

        # quantity
        s = Search('Observation', 'value-quantity=gt234|http://loinc.org|mg')
        assert s['value-quantity'].value == 234
        assert s['value-quantity'].prefix == 'gt'

    def test_token(self):
        s = Search('Condition', 'code=http://acme.org/conditions/codes|ha125')
        assert s['code'].value == 'ha125'

    def test_chain(self):
        s = Search('Observation', 'subject:Patient.name=peter')
        assert not s['name'].modifier
        assert s['name'].type_ == 'string'
        assert s['name'].chain[0].target == 'subject'
        assert s['name'].chain[1].endpoint == 'Patient'
        assert s['name'].chain[0].endpoint == 'Observation'
        assert s['name'].value == 'peter'
        try:
            s = Search('Observation', 'subject:Patient.organization=peter')
        except TypeError:
            pass
        else:
            assert False

    #def test_chain_plus(self):
        #s = Search('Observation', 'code=http://loinc.org|1234-5&subject.name=peter')
        #assert s['code'].value == 'http://loinc.org|1234-5'
        #assert s['subject'].value == 'peter'
        #assert s['subject'].chain[0].endpoint == 'Patient'
        #assert s['subject'].chain[0].ttype == 'string'
        #assert s['subject'].chain[0].target == 'name'

    def test_control(self):
        s = Search('Procedure', 'date=le2011-12-31&_count=34')
        assert len(s.control) == 1
        assert s.control[0].parameter == '_count'
        assert s.control[0].value == 34


    def test_mod_plus(self):
        s = Search('AllergyIntolerance', 'clinical-status=active&clinical-status:exists=false')
        assert len(s['clinical-status']) == 2
        assert s['clinical-status'][0].value == 'active'
        assert not s['clinical-status'][0].modifier
        assert s['clinical-status'][1].value == 'false'
        assert s['clinical-status'][1].modifier == 'exists'

    def test_or(self):
        s = Search('Condition', '_text=(bone OR liver) and metastases')
        assert s[0].value == '(bone OR liver) and metastases'
        assert s[0].parameter == '_text'

if __name__ == '__main__':
    unittest.main()
