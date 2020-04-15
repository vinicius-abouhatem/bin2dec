import pytest

from main import is_valid_binary_number, to_decimal


@pytest.mark.parametrize(
    "raw,expected",
    [
        ('0', True),
        ('1', True),
        ('11001010', True),
        ('2', False),
        ('3', False),
        ('4', False),
        ('a', False),
    ]
)
def test_is_valid_binary_number(raw, expected):
    assert is_valid_binary_number(raw) == expected


@pytest.mark.parametrize(
    "raw,expected",
    [
        ('0', 0),
        ('1', 1),
        ('10', 2),
        ('11', 3),
        ('11001010', 202)
    ]
)
def test_to_decimal(raw, expected):
    assert to_decimal(raw) == expected
