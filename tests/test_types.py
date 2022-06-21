import pytest
from src.entry import convert_json_schema_to_py
from tests.data.singles import (
    day_schema,
    number_schema,
    text_schema,
    email_schema,
    time_schema,
    date_time_schema,
    textarea_schema
)


@pytest.mark.parametrize(
    "schema,expected_output",
    [
        (day_schema, "day"),
        (number_schema, "number"),
        (text_schema, "textfield"),
        (email_schema, "email"),
        (time_schema, "time"),
        (date_time_schema, "datetime"),
        (textarea_schema,"textarea")
    ],
)
def test_simple(schema, expected_output):
    assert convert_json_schema_to_py(schema)["components"][0]["type"] == expected_output


if __name__ == "__main__":
    pass
