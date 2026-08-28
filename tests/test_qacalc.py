import pytest

from qacalc import add, subtract


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
