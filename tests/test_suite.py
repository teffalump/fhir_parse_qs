import pytest
from fhir_parse_qs import Search
from datetime import datetime
from pendulum import now

qss = [
    (
        "Observation",
        'filter=name eq http://loinc.org|1234-5 and subject.name co "peter"',
    ),
    (
        # Search for all diagnostic reports that contain on observation with a potassium value of >5.4 mmol/L (UCUM)
        "DiagnosticReport",
        "result.code-value-quantity=http://loinc.org|2823-3$gt5.4|http://unitsofmeasure.org|mmol/L",
    ),
    (
        # Search for all questionnaires that have a clinical focus = "Substance abuse prevention assessment (procedure)"
        "Questionnaire",
        "context-type-value=focus$http://snomed.info/sct|408934002",
    ),
    (
        # Search for all groups that have a characteristic "gender" with a text value of "mixed"
        "Group",
        "characteristic-value=gender$mixed",
    ),
    # ('Patient', '_has:Observation:patient:_has:AuditEvent:entity:user=MyUserId'),
]


class TestString:
    def test_not_supported(self):
        try:
            s = Search("Blark", "eueu=aoeuaoeu")
            assert False
        except:
            assert True

    def test_unknown(self):
        s = Search("Patient", "blank=female")
        assert len(s.error) == 1
        assert len(s) == 0

    def test_basic(self):
        s = Search("Patient", "gender=female")
        assert len(s) == 1
        assert s.endpoint == "Patient"
        assert not s.modifier
        assert not s.prefix

    def test_basic_plus(self):
        s = Search("Patient", "_count=42&gender=female")
        assert s.endpoint == "Patient"
        assert len(s) == 2
        assert s["_count"].value[0].value == 42
        assert s["gender"].value[0].value == "female"
        assert not s.modifier

    def test_mod(self):
        s = Search("Patient", "given:contains=eve")
        assert s[0].parameter.modifier == "contains"
        assert s[0].value[0].value == "eve"
        assert s[0].parameter.value == "given"
        assert not s.prefix

    def test_cast(self):
        try:
            s = Search("Observation", "value-quantity=AAA")
        except ValueError:
            pass

        try:
            s = Search("Procedure", "date=ge201000-01-01&date=le2011-12-31")
        except ValueError:
            pass

    def test_prefix_cast(self):
        s = Search("Procedure", "date=ge2010-01-01&date=le2011-12-31")
        assert s.endpoint == "Procedure"
        assert len(s) == 2
        assert len(s["date"]) == 2
        assert "ge" in s.prefix
        assert "le" in s.prefix
        n = now("Europe/London")
        assert isinstance(s["date"][0].value[0].value, datetime)
        assert s["date"][0].value[0].value < n
        assert isinstance(s["date"][1].value[0].value, datetime)
        assert s["date"][1].value[0].value < n

    def test_quantity(self):
        s = Search("Observation", "value-quantity=gt234|http://loinc.org|mg")
        assert s["value-quantity"].value[0].value == 234
        assert s["value-quantity"].value[0].prefix == "gt"
        assert s["value-quantity"].value[0].system == "http://loinc.org"
        assert s["value-quantity"].value[0].code == "mg"
        s = Search("Observation", "value-quantity=gt234||mg")
        assert s["value-quantity"].value[0].value == 234
        assert s["value-quantity"].value[0].prefix == "gt"
        assert s["value-quantity"].value[0].system == None
        assert s["value-quantity"].value[0].code == "mg"
        s = Search("Observation", "value-quantity=gt234")
        assert s["value-quantity"].value[0].value == 234
        assert s["value-quantity"].value[0].prefix == "gt"
        assert s["value-quantity"].value[0].system == None
        assert s["value-quantity"].value[0].code == None
        s = Search("Observation", "value-quantity=gt2.34e2|http://loinc.org|mg")
        assert s["value-quantity"].value[0].value == 234
        assert s["value-quantity"].value[0].prefix == "gt"
        assert s["value-quantity"].value[0].system == "http://loinc.org"
        assert s["value-quantity"].value[0].code == "mg"

    def test_token(self):
        s = Search("Condition", "code=http://acme.org/conditions/codes|ha125")
        assert s["code"].value[0].value == "ha125"
        assert s["code"].value[0].system == "http://acme.org/conditions/codes"
        assert s["code"].value[0].code == None
        s = Search("Condition", "code=|ha125")
        assert s["code"].value[0].value == "ha125"
        assert s["code"].value[0].system == None
        assert s["code"].value[0].code == None
        s = Search("Condition", "code=ha125")
        assert s["code"].value[0].value == "ha125"
        assert s["code"].value[0].system == None
        assert s["code"].value[0].code == None

    def test_chain(self):
        s = Search("Observation", "subject:Patient.name=peter")
        assert not s["name"].parameter.modifier
        assert s["name"].parameter.type_ == "string"
        assert s["name"].parameter.chain[0].target == "subject"
        assert s["name"].parameter.chain[1].endpoint == "Patient"
        assert s["name"].parameter.chain[0].endpoint == "Observation"
        assert len(s["name"].parameter.chain) == 2
        assert s["name"].value[0].value == "peter"
        try:
            s = Search("Observation", "subject.organization=peter")  # None
        except TypeError:
            pass
        else:
            assert False
        try:
            s = Search("Observation", "subject.name=peter")  # Ambiguous
        except TypeError:
            pass
        else:
            assert False
        s = Search("Observation", "subject.gender=male")  # Only 1 valid

    def test_or_values(self):
        s = Search("Patient", "name=peter,travis")
        assert s[0].value[0].value == "peter"
        assert s[0].value[1].value == "travis"

    def test_control(self):
        s = Search("Procedure", "date=le2011-12-31&_count=34")
        assert len(s.control) == 1
        assert s.control[0].parameter.value == "_count"
        assert s.control[0].value[0].value == 34

    def test_mod_plus(self):
        s = Search(
            "AllergyIntolerance", "clinical-status=active&clinical-status:exists=false"
        )
        assert len(s["clinical-status"]) == 2
        assert s["clinical-status"][0].value[0].value == "active"
        assert not s["clinical-status"][0].parameter.modifier
        assert s["clinical-status"][1].value[0].value == "false"
        assert s["clinical-status"][1].parameter.modifier == "exists"

    def test_text(self):
        s = Search("Condition", "_text=(bone OR liver) and metastases")
        assert s[0].value[0].value == "(bone OR liver) and metastases"
        assert s[0].parameter.value == "_text"
