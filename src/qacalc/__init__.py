"""A minimal calculator package."""

from __future__ import annotations


def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of ``a`` and ``b``.
    """
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract the second number from the first.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The difference of ``a`` and ``b``.
    """
    return a - b
