from qacalc import add, subtract


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
