"""Command-line interface for qacalc."""

from __future__ import annotations

import argparse

from qacalc import add, subtract


def _number(value: str) -> int | float:
    """Parse a string as an int, falling back to float."""
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"invalid number: {value!r}") from None


def build_parser() -> argparse.ArgumentParser:
    """Build the qacalc argument parser."""
    parser = argparse.ArgumentParser(prog="qacalc")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add two numbers.")
    add_parser.add_argument("a", type=_number)
    add_parser.add_argument("b", type=_number)

    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers.")
    subtract_parser.add_argument("a", type=_number)
    subtract_parser.add_argument("b", type=_number)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the qacalc CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        result = add(args.a, args.b)
    else:
        result = subtract(args.a, args.b)

    print(result)
    return 0
