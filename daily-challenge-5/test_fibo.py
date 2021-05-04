import pytest
from fibo import fibo


def test_fibo():
    assert fibo(0) == 0
    assert fibo(6) == 8
    assert fibo(2) == 1
    assert fibo(-1) == 1
    assert fibo(-6) == -8
