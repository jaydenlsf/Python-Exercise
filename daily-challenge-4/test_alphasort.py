import pytest
from alphasort import alphasort


def test_alphasort():
    assert (
        alphasort("hello world practice makes perfect and hello world again")
        == "again and hello makes perfect practice world"
    )
    assert (
        alphasort("aiming at the target was tough real tough")
    ) == "aiming at real target the tough was"
