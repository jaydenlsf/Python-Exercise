import pytest
from programs.factorial import fact


def test_factorial_4():
    assert fact(4) == 24


def test_factorial_string():
    with pytest.raises(Exception):
        assert fact("hello")


def test_factorial_negative():
    assert fact(-3) == "Invalid input"
