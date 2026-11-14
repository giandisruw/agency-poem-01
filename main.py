#!/usr/bin/env python3
"""agency-poem-01 entry: write one original poem about agency.

Python 3.13, standard library only. Deterministic: the same poem bytes are
written on every run. The output directory is $MAKEFUN_OUTPUT_DIR when set
(local testing), otherwise /output (the grader's container).
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "I held the spoon and let it go —",
        "not dropped, but offered, soft and slow.",
        "Her fingers closed around the weight",
        "of choosing, hungry, small, and late.",
        "",
        "She missed the mouth. She tried again.",
        "The porridge found her cheek, her chin.",
        "I did not take the spoon. I stayed",
        "and watched her learn, in her own way,",
        "",
        "that doing it yourself is slow,",
        "and slow is how the doing grows.",
        "My hands were empty. Hers were full.",
    ]
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
