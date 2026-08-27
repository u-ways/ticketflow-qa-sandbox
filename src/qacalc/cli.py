from __future__ import annotations

import argparse

from qacalc import add, subtract


def _number(value: str) -> int | float:
    try:
        return int(value)
    except ValueError:
        return float(value)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="qacalc")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("a", type=_number)
    add_parser.add_argument("b", type=_number)

    subtract_parser = subparsers.add_parser("subtract")
    subtract_parser.add_argument("a", type=_number)
    subtract_parser.add_argument("b", type=_number)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "add":
        result = add(args.a, args.b)
    else:
        result = subtract(args.a, args.b)

    print(result)
    return 0
