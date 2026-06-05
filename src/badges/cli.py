from __future__ import annotations

import argparse
import sys

from badges.core import add, divide, subtract


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="badges",
        description="Simple arithmetic utilities.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add two numbers.")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    subtract_parser = subparsers.add_parser("subtract", help="Subtract two numbers.")
    subtract_parser.add_argument("a", type=float)
    subtract_parser.add_argument("b", type=float)

    divide_parser = subparsers.add_parser("divide", help="Divide two numbers.")
    divide_parser.add_argument("a", type=float)
    divide_parser.add_argument("b", type=float)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "add":
            result = add(args.a, args.b)
        elif args.command == "subtract":
            result = subtract(args.a, args.b)
        else:
            result = divide(args.a, args.b)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
