#!/usr/bin/env python3
"""agency-poem-01 v2 entry: write one original poem about agency.

Python 3.13, standard library only. Deterministic: the same poem bytes are
written on every run. The output directory is $MAKEFUN_OUTPUT_DIR when set
(local testing), otherwise /output (the grader's container).

The poem: an old woman signs her name to hand her affairs to her daughter —
house, car, cash — and keeps the pen. Agency as the last thing you sign
away, and the one thing you refuse to give up.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "She signs her name the way she always has —",
        "the loop of the L, the cross, the dash —",
        "and the paper takes her house, her car, her cash,",
        "and gives them to the daughter in the chair.",
        "",
        "The pen is shaking. She steadies it with the other hand.",
        "This is the last thing she will ever sign",
        "that is hers to sign. She knows it. She signs it anyway.",
        "The ink dries. The daughter folds the page.",
        "",
        "She keeps the pen.",
    ]
)


def main() -> None:
    # Gate check (mirrors the competition's sealed scorer): 1 to 1,000
    # characters, not only white space. Fail loudly instead of writing an
    # invalid entry.
    assert 1 <= len(POEM) <= 1000, f"poem is {len(POEM)} chars"
    assert POEM.strip(), "poem is only white space"
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
