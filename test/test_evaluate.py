from flib import Flib
import pytest


@pytest.fixture
def setup():
    return "111202011000"


@pytest.mark.parametrize(
    "input_string, expected_value",
    (
        ("010101", 4),
        ("110110110", 4),
        ("0100110100110", 12),
    ),
)
def test_evaluate(setup, input_string, expected_value):
    flib = Flib(setup)
    assert flib.evaluate(input_string) == expected_value
