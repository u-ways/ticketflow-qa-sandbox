"""Command-line interface for qacalc."""

import argparse
import math
import sys

from qacalc import add, divide, multiply, subtract


def parse_number(s: str):
    """Parse a CLI argument as an int, falling back to float."""
    try:
        return int(s)
    except ValueError:
        return float(s)


def format_result(value) -> str:
    """Format a numeric result, dropping a trailing ".0" for whole-number floats."""
    if isinstance(value, float) and value.is_integer():
        if value == 0 and math.copysign(1.0, value) < 0:
            return "-0"
        return str(int(value))
    return str(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="qacalc", description="Simple calculator CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    commands = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    for name, func in commands.items():
        subparser = subparsers.add_parser(name)
        subparser.add_argument("a", type=parse_number)
        subparser.add_argument("b", type=parse_number)
        subparser.set_defaults(func=func)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        result = args.func(args.a, args.b)
    except ArithmeticError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    print(format_result(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
