"""Command-line interface for qacalc."""

import argparse

from qacalc import add, subtract

OPERATIONS = {
    "add": add,
    "subtract": subtract,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="qacalc", description="A simple calculator.")
    subparsers = parser.add_subparsers(dest="operation", required=True)

    for name in OPERATIONS:
        subparser = subparsers.add_parser(name)
        subparser.add_argument("a", type=float)
        subparser.add_argument("b", type=float)

    return parser


def format_result(value: float) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result = OPERATIONS[args.operation](args.a, args.b)
    print(format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
