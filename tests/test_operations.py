import pytest

from qacalc import add, divide, multiply, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_with_zero():
    assert add(0, 5) == 5


def test_add_floats():
    assert add(2.5, 1.5) == 4.0


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_with_zero():
    assert subtract(5, 0) == 5


def test_subtract_floats():
    assert subtract(5.5, 2.5) == 3.0


def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


def test_multiply_with_zero():
    assert multiply(0, 5) == 0


def test_multiply_floats():
    assert multiply(2.5, 2.0) == 5.0


def test_divide_positive_numbers():
    assert divide(6, 3) == 2


def test_divide_negative_numbers():
    assert divide(-6, -3) == 2


def test_divide_floats():
    assert divide(5.0, 2.0) == 2.5


def test_divide_with_zero_dividend():
    assert divide(0, 5) == 0


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
