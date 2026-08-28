import pytest

from qacalc import add, divide, multiply, subtract


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-2, 3, 1),
        (-2, -3, -5),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
        (1.1, 2.2, pytest.approx(3.3)),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (5, 3, 2),
        (3, 5, -2),
        (-2, 3, -5),
        (-2, -3, 1),
        (0, 0, 0),
        (5.5, 2.5, 3.0),
        (2.5, 5.5, -3.0),
        (1.1, 0.1, pytest.approx(1.0)),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (0, 5, 0),
        (2.5, 4, 10.0),
        (-2.5, 4, -10.0),
        (1.1, 2.0, pytest.approx(2.2)),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (6, 3, 2),
        (-6, 3, -2),
        (-6, -3, 2),
        (0, 5, 0),
        (5.0, 2, 2.5),
        (-5.0, 2, -2.5),
        (1.0, 3, pytest.approx(0.3333333333333333)),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize("a", [1, -1, 0, 1.5, -1.5])
def test_divide_by_zero_raises(a):
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(a, 0)
