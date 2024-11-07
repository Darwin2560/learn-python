import pytest

from ..calculator import square


def test_positive_square():
    assert square(2) == 4
    assert square(3) == 9


def test_negative_square():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero_square():
    assert square(0) == 0


def test_str_square():
    with pytest.raises(TypeError):
        square("cat")
