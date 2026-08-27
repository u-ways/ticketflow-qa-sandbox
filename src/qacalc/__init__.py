"""qacalc: a tiny calculator package."""

from __future__ import annotations


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of a and b."""
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """Return the quotient of a and b, raising ZeroDivisionError when b is 0."""
    if b == 0:
        raise ZeroDivisionError(f"cannot divide {a} by zero")
    return a / b
