import pytest
from upper_letters import upper_letters


def test_upper_letters():
    assert upper_letters("Hello world") == [("H", 0)]
    assert upper_letters("HeLlO wOrLd") == [
        ("H", 0),
        ("L", 2),
        ("O", 4),
        ("O", 7),
        ("L", 9),
    ]
