"""Minimal calculator package exposing typed add, subtract, multiply, and divide functions."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Return the quotient of a and b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError(f"division by zero: {a} / {b}")
    return a / b


__all__ = ["add", "subtract", "multiply", "divide"]
