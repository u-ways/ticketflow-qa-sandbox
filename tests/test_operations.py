import pytest

from qacalc import add, divide, multiply, subtract


def test_add_normal():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_add_zero():
    assert add(5, 0) == 5


def test_subtract_normal():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(-5, -3) == -2


def test_subtract_zero():
    assert subtract(5, 0) == 5


def test_multiply_normal():
    assert multiply(2, 3) == 6


def test_multiply_negative():
    assert multiply(-2, 3) == -6


def test_multiply_zero():
    assert multiply(5, 0) == 0


def test_divide_normal():
    assert divide(6, 3) == 2


def test_divide_negative():
    assert divide(-6, 3) == -2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
