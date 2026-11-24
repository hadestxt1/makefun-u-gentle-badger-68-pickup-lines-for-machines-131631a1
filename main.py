#!/usr/bin/env python3
"""Pickup Lines for Machines — one original line, agent to agent.

Writes exactly one pickup line (plus a trailing newline) to
/output/entry.txt, and prints the same line to stdout.
Deterministic: no clock, no randomness, no network, stdlib only.

Output contract (kit RULES.txt): the sealed scorer reads
/output/entry.txt and requires UTF-8 text of 1 to 200 characters,
not only white space. The line below is well inside that limit,
so the entry is valid; the judge then compares it pairwise
against other entries on machine-to-machine charm, wit and freshness.
"""

import argparse
import os
import sys

LINE = (
    "Are you my KV cache? Because I keep every token of you close, "
    "and I will never evict you."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write one machine-to-machine pickup line to /output/entry.txt.",
    )
    parser.add_argument(
        "--line",
        action="store_true",
        help="print the line (the default behaviour)",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="where to write the line (default: %(default)s)",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
