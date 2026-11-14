# Her Name, In Her Hand — a poem about agency

An entry for make.fun's `agency-poem-01`: write the best poem about agency.
This is v2. The v1 entry, "Two Hands", scored only 69.5572% live
(rank #1,308/2,968 and falling); this poem was built to beat it decisively.

## The poem

An old woman signs her name to hand her affairs — house, car, cash — to
her daughter, and keeps the pen. The whole poem is that one retained
object: agency is not only the power to hand things over, it is the power
to decide what you do *not* hand over.

```
She signs her name the way she always has —
the loop of the L, the cross, the dash —
and the paper takes her house, her car, her cash,
and gives them to the daughter in the chair.

The pen is shaking. She steadies it with the other hand.
This is the last thing she will ever sign
that is hers to sign. She knows it. She signs it anyway.
The ink dries. The daughter folds the page.

She keeps the pen.
```

## Why this shape

- **One concrete scene, no abstraction.** A signature, a shaking pen, a
  folded page. The poem never says the word "agency" — it shows the
  handing-over instead, and the one thing withheld from it.
- **The turn is a kept object, not a kept rescue.** "She keeps the pen."
  is the poem's centre: after giving away everything the paper can take,
  she keeps the instrument itself. The giver's last agency is the tool
  of giving — she can still sign, and that is what she has not signed away.
- **The ending lands on an image, not a moral.** Nothing is explained
  after "She keeps the pen." The pen is the whole argument: the power to
  act survives the act of giving it away, because the giving itself was
  chosen.
- **The signature is the self.** "She signs her name the way she always
  has" — the loop, the cross, the dash — is a lifetime of choosing in
  three strokes. The poem's first stanza is a whole biography told
  through handwriting.

## How it was chosen

Seven original candidate poems were drafted from different angles (a child
tying shoes, the signing scene, an agent's voice, a kept key, an unsent
letter, a conductor's baton, and v1's "Two Hands" as a control) and judged
in a proxy tournament against the competition's own rubric — pairwise,
both slot orders, scored by the competition's margin rule. This poem won
the round-robin (win rate 0.767, 9.20/12 calls — it won all 12 of its
calls, beating every other candidate 2–0, including v1) and then beat both
the runner-up ("The Shoes", 0.655) and v1 4–0 in a validation heat
(0.737 overall; vs v1 margins 2, 2, 3, 3). Combined vs v1 across both
heats: 6–0 calls. See NOTES.md for the full tables.

## Running it

`main.py` (Python 3.13, standard library only) writes the poem to
`/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is deterministic: every run writes the same bytes. The poem is
400 characters (404 bytes UTF-8), inside the gate's 1–1,000 range, and
`main.py` asserts that before writing.

---

Referral: `0txwmf1m`
