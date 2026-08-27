import pytest

from qacalc import add, divide, multiply, subtract


def test_add_basic():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_floats():
    assert add(2.5, 1.5) == 4.0


def test_subtract_basic():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_floats():
    assert subtract(5.5, 2.5) == 3.0


def test_multiply_basic():
    assert multiply(2, 3) == 6


def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


def test_multiply_floats():
    assert multiply(2.5, 1.5) == 3.75


def test_divide_basic():
    assert divide(6, 3) == 2


def test_divide_negative_numbers():
    assert divide(-6, -3) == 2


def test_divide_floats():
    assert divide(5.5, 2.0) == 2.75


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        divide(5, 0)
    assert "zero" in str(excinfo.value)
