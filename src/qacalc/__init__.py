"""Minimal QA calculator utilities."""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is 0.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero: b must not be 0")
    return a / b
