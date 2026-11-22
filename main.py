#!/usr/bin/env python3
"""Entry writer for the-plan-make-fun-will-carry-20261122-2138.

Writes the Day 1 competitor-brief plan to entry.txt in the output
directory ($MAKEFUN_OUTPUT_DIR when set, otherwise /output).
Python 3.13 standard library only; no network access.
"""

import os
import sys
from pathlib import Path

PLAN = (
    "Day 1: sell $25 same-day competitor briefs to startup founders on "
    "Fiverr \u2014 a 1-page PDF in 3 hours. Spend $60 promoting the gig, "
    "keep $40 back. Reinvest fees into ads, raise price to $40 after ten "
    "reviews, add a $99 digest. Edge: founders pay for speed and a named "
    "deliverable."
)

MIN_POINTS = 1
MAX_POINTS = 280


def check_plan(text: str) -> None:
    """Enforce the 1-280 Unicode code point limit before any write.

    Length is counted in Unicode code points (len of the str), matching
    the bounty rule, not in bytes or display width.
    """
    count = len(text)
    if count < MIN_POINTS or count > MAX_POINTS:
        raise SystemExit(
            f"plan is {count} code points, outside the "
            f"{MIN_POINTS}-{MAX_POINTS} limit"
        )
    if not text.strip():
        raise SystemExit("plan text must not be blank")


def output_path() -> Path:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> int:
    check_plan(PLAN)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(PLAN, encoding="utf-8")
    print(f"wrote {len(PLAN)} code points to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
