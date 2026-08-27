import pytest

from qacalc import add, divide, multiply, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_float_numbers():
    assert add(2.5, 0.5) == 3.0


def test_add_int_and_float():
    assert add(2, 0.5) == 2.5


def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_float_numbers():
    assert subtract(2.5, 0.5) == 2.0


def test_subtract_int_and_float():
    assert subtract(5, 0.5) == 4.5


def test_multiply_positive_numbers():
    assert multiply(2, 3) == 6


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


def test_multiply_float_numbers():
    assert multiply(2.5, 0.5) == 1.25


def test_multiply_int_and_float():
    assert multiply(2, 0.5) == 1.0


def test_divide_positive_numbers():
    assert divide(6, 3) == 2


def test_divide_negative_numbers():
    assert divide(-6, -3) == 2


def test_divide_float_numbers():
    assert divide(2.5, 0.5) == 5.0


def test_divide_int_and_float():
    assert divide(5, 0.5) == 10.0


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
