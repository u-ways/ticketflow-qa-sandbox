from qacalc import add, subtract


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
