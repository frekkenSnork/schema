import pytest
from src.entry import convert_json_schema_to_py
from tests.data.int_vs_number import (
    integer_schema,
    number_schema,
)


@pytest.mark.parametrize(
    "schema,expected_output",
    [
        (integer_schema, ""),
        (number_schema, None),
    ],
)
def test_compair(schema, expected_output):
    assert (
        convert_json_schema_to_py(schema)["components"][0]["validate"].get("integer")
        == expected_output
    )


if __name__ == "__main__":
    pass

"""
{'components': [{'key': 'huisnummer', 'label': 'home number', 
'description': None, 
'validate': {'required': True, 'pattern': None, 'max': None, 'min': None, 'integer': None, 'step': None}, 
'defaultValue': None, 
'type': 'number'}]}


{'components': [{'key': 'temp', 'label': 'Temp today', 
'description': "Check if it's sunny", 
'validate': {'required': False, 'pattern': None, 'max': None, 'min': None, 'integer': None, 'step': None}, 
'defaultValue': None, 
'type': 'number'}]}


"""
