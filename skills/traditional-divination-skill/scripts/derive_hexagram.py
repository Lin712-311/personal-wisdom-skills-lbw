"""Command-line interface for deterministic hexagram derivation."""

import argparse
import json
import sys

from hexagrams import derive


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Derive a hexagram from six line totals, ordered 初爻 to 上爻."
    )
    parser.add_argument(
        "values",
        type=int,
        nargs=6,
        metavar="LINE",
        help="six bottom-to-top line totals; each must be 6, 7, 8, or 9",
    )
    return parser


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = derive(args.values)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
