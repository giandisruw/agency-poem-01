#!/usr/bin/env python3
"""agency-poem-01 v3 entry: writes one poem about agency to entry.txt.

Deterministic, standard library only, no network. The poem is fixed text:
an agent's borrowed voice speaks for someone who has lost theirs, and
the poem turns on who is really choosing -- the speaker, or the voice.
"""
import os

POEM = (
    "The tablet rests against my throat,\n"
    "a blue bar measuring silence.\n"
    "I type: The pears are bruised\n"
    "on the side that faced the wall.\n"
    "\n"
    "Its speaker gives me my old vowels,\n"
    "polished, even, without the catch\n"
    "that used to turn a sentence home.\n"
    "At the clinic, it says, I am afraid.\n"
    "I never typed those words.\n"
    "\n"
    "The nurse writes afraid into my chart.\n"
    "I touch NO, then enter: Stay.\n"
    "The borrowed mouth says it softly.\n"
    "For once, the room waits\n"
    "to hear which of us will continue."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
