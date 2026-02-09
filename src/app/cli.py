from __future__ import annotations

import argparse

from core.calculator import add, divide, multiply, subtract


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="calc", description="Simple Calculator CLI")
    parser.add_argument("--version", action="version", version="calc 0.1.0")

    subparsers = parser.add_subparsers(dest="command", required=True)

    for name in ("add", "subtract", "multiply", "divide"):
        p = subparsers.add_parser(name)
        p.add_argument("a", type=float)
        p.add_argument("b", type=float)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    ops = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    result = ops[args.command](args.a, args.b)
    print(f"Result: {result}\n")


if __name__ == "__main__":
    main()