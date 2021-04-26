import pytest
from even_number import even_num


def test_even_number_10_30():
    assert even_num(10, 30) == "20, 22, 24, 26, 28"


def test_even_number_1_100():
    assert (
        even_num(1, 100)
        == "2, 4, 6, 8, 20, 22, 24, 26, 28, 40, 42, 44, 46, 48, 60, 62, 64, 66, 68, 80, 82, 84, 86, 88"
    )


def test_even_number_200_400():
    assert (
        even_num(200, 400)
        == "200, 202, 204, 206, 208, 220, 222, 224, 226, 228, 240, 242, 244, 246, 248, 260, 262, 264, 266, 268, 280, 282, 284, 286, 288, 400"
    )


def test_even_number_string():
    with pytest.raises(TypeError):
        assert even_num("hello", "hello")


def test_even_number_additional_arg():
    with pytest.raises(TypeError):
        assert even_num(10, 20, 30)


def test_even_number_no_arg():
    with pytest.raises(TypeError):
        assert even_num()


def test_even_number_over_limit():
    with pytest.raises(AssertionError):
        assert even_num(1000, 2000)
