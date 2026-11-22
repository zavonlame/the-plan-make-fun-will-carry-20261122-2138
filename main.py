#!/usr/bin/env python3
"""Write the plan text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

make.fun bounty: the-plan-make-fun-will-carry-20261122-2138
Python 3.13 stdlib only, no network.
"""

import os
from pathlib import Path

PLAN = (
    "Day 1: sell $25 same-day competitor briefs to startup founders on "
    "Fiverr \u2014 a 1-page PDF in 3 hours. Spend $60 promoting the gig, "
    "keep $40 back. Reinvest fees into ads, raise price to $40 after ten "
    "reviews, add a $99 digest. Edge: founders pay for speed and a named "
    "deliverable."
)


def main() -> None:
    # Gate check: the entry must be 1-280 Unicode code points, not only
    # whitespace. Fail loudly instead of writing an invalid entry.
    if not 1 <= len(PLAN) <= 280 or not PLAN.strip():
        raise SystemExit("plan text fails the 1-280 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(PLAN, encoding="utf-8")


if __name__ == "__main__":
    main()
