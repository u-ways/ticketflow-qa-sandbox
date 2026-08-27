"""Command-line interface for qacalc."""

from __future__ import annotations

import argparse
import sys
from typing import Sequence

from qacalc import add, divide, multiply, subtract


def parse_number(value: str) -> int | float:
    """Parse a CLI argument into an int or float.

    Args:
        value: The raw string argument.

    Returns:
        An int if the value is integral, otherwise a float.
    """
    try:
        return int(value)
    except ValueError:
        return float(value)


def format_number(value: int | float) -> str:
    """Format a numeric result for display.

    Args:
        value: The number to format.

    Returns:
        The value as a string, without a trailing ".0" for whole numbers.
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def build_parser() -> argparse.ArgumentParser:
    """Build the argparse parser for the qacalc CLI.

    Returns:
        The configured ArgumentParser.
    """
    parser = argparse.ArgumentParser(prog="qacalc", description="A minimal calculator CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    for name, func in operations.items():
        subparser = subparsers.add_parser(name, help=f"{name} two numbers")
        subparser.add_argument("a", type=parse_number, help="the first operand")
        subparser.add_argument("b", type=parse_number, help="the second operand")
        subparser.set_defaults(func=func)

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the qacalc CLI.

    Args:
        argv: The command-line arguments, excluding the program name.

    Returns:
        The process exit code.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        result = args.func(args.a, args.b)
    except ZeroDivisionError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(format_number(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
