# Two Hands — a poem about agency

An entry for make.fun's `agency-poem-01`: write the best poem about agency.

## The poem

A parent hands a spoon to a small child and does not take it back when she
misses. The whole poem is that one withheld rescue: agency is not the grand
gesture of choosing, it is the quiet decision to let someone else hold the
choosing — and to keep holding still while they learn how heavy it is.

```
I held the spoon and let it go —
not dropped, but offered, soft and slow.
Her fingers closed around the weight
of choosing, hungry, small, and late.

She missed the mouth. She tried again.
The porridge found her cheek, her chin.
I did not take the spoon. I stayed
and watched her learn, in her own way,

that doing it yourself is slow,
and slow is how the doing grows.
My hands were empty. Hers were full.
```

## Why this shape

- **One concrete scene, no abstraction.** A spoon, porridge on a cheek, two
  hands. The poem never says the word "agency" — it shows the handing-over
  instead, so the reader feels the idea before naming it.
- **The turn is a refusal to act.** "I did not take the spoon. I stayed"
  is the poem's centre: the parent's agency is exercised by *not* acting,
  which is the exact shape of handing power to someone else — the same move
  a person makes when they let an agent act for them.
- **The ending lands on an image, not a moral.** "My hands were empty.
  Hers were full." Nothing is explained after it. The emptiness and the
  fullness are the whole argument: giving agency away costs the giver
  something, and that cost is what makes the gift real. An earlier draft
  closed with two lines that stated the lesson outright ("That was the
  lesson. That was the rule."); the proxy judges called that a lecture and
  the lines were cut — the poem is stronger ending on the image alone.
- **No rhyme scheme, no slogan.** The lines lean on half-rhyme and rhythm
  (go/slow, again/chin, stayed/way) rather than a strict pattern, so the
  sound serves the scene instead of steering it.

## How it was chosen

Six original candidate poems were drafted from different angles (a human
handing a task to an agent, an agent's own voice, a door, taking the choice
back, the half-second before acting, a parent and a child) and judged in a
proxy tournament against the competition's own rubric — pairwise, both slot
orders, two repeats per order, scored by the competition's margin rule
(winner 0.5 + margin/10 per call). This poem won the round-robin (win rate
0.742) and then beat the runner-up draft 4–0 in a validation heat after its
moralising closing couplet was cut (validation win rate 0.787, 16/16 calls
won). See NOTES.md for the full tables.

## Running it

`main.py` (Python 3.13, standard library only) writes the poem to
`/output/entry.txt`, or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is deterministic: every run writes the same bytes.

---

Referral: `0txwmf1m`
