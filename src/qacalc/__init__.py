"""qacalc: a minimal calculator package."""

from __future__ import annotations


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract the second number from the first.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of a and b (a - b).
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """Divide the first number by the second.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a and b (a / b).

    Raises:
        ZeroDivisionError: If b is 0.
    """
    if b == 0:
        raise ZeroDivisionError(f"division by zero: cannot divide {a} by 0")
    return a / b
