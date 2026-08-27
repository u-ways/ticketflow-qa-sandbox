from qacalc import add, subtract


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
