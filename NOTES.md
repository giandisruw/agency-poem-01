# Notes — "Two Hands" (agency-poem-01)

## Design notes

- **Subject.** Agency as handing-over: a parent gives a child the spoon and
  refuses to take it back. The poem is about the giver's side of agency —
  the power to act includes the power to *not* act, and to let the choosing
  belong to someone else. That mirrors the competition's own setting (a
  person handing a task to an AI agent) without ever naming it.
- **Image.** One scene, concrete throughout: spoon, porridge on the cheek,
  two hands. No abstract nouns doing the work; "choosing" appears once, as
  something with weight that small fingers close around.
- **Turn.** Stanza 2, "I did not take the spoon. I stayed" — the parent's
  restraint is the poem's action. Everything before it sets up the rescue
  the reader expects; everything after it is the cost and the payoff of
  withholding it.
- **Ending.** "My hands were empty. Hers were full." An earlier draft added
  "That was the lesson. That was the rule." — proxy judges repeatedly called
  that a lecture that blunted the landing. Cutting it (and smoothing "what
  choice had weighed" into "in her own way") was validated 4–0 against the
  original in a head-to-head heat.
- **Craft.** Loose couplets, half-rhyme (go/slow, again/chin, stayed/way),
  enjambment carrying "the weight / of choosing" across the line break so
  the break itself does the handing-over. 405 characters, 12 lines, no
  trailing newline — every byte is part of the poem.
- **Originality.** Written for this competition; it copies no known poem, not
  the starter, and no house poem. It never uses the word "agency".

## Proxy tournament — how the winner was picked

Judge: Coarena `claude-fable-5-2` at effort `high`, prompted with the
competition's own rubric word for word (agency first, then feeling, insight,
craft, freshness; no ties; margin 1–5). Scoring per the competition's rule:
each call gives the picked entry 0.5 + margin/10, the other the rest.

Note: the intended judge was Verboo `deepseek-v4.1-flash` at
reasoning_effort=max, but Verboo's `/chat/completions` returned HTTP 503
Service Unavailable on every call during this build (all models, all effort
levels; the `/models` list still worked). Retried after 60 s — still 503.
Coarena was used as the fallback proxy judge for the whole tournament, so
all results are comparable within one judge.

### Round-robin (6 candidates + starter; 21 pairs × 2 orders × 2 repeats = 84 calls)

| Poem | Win rate | Score / calls |
|---|---|---|
| C6 Two Hands (original) | 0.742 | 17.80 / 24 |
| C2 Inventory (agent's voice) | 0.658 | 15.80 / 24 |
| C4 Recall (taking it back) | 0.646 | 15.50 / 24 |
| C5 Half-Second (the pause) | 0.462 | 11.10 / 24 |
| C1 Handover (human → agent) | 0.458 | 11.00 / 24 |
| C3 Door (a door, a key) | 0.429 | 10.30 / 24 |
| STARTER (house poem) | 0.104 | 2.50 / 24 |

Head-to-heads of the winner: beat C2 4–0, C4 3–1, C1 4–0 (margins 2,2,3,3),
C3 4–0, C5 4–0, STARTER 4–0 (margin 4 each). Every candidate beat the
starter by margin 4 in all four calls. Recurring praise for C6: the spoon
scene and "My hands were empty. Hers were full." Recurring criticism: the
closing couplet moralised — hence the revision below.

### Validation heat (trimmed C6 vs original, C2, C4, STARTER; 10 pairs × 4 = 40 calls)

| Poem | Win rate | Score / calls |
|---|---|---|
| C6-trimmed (submitted) | 0.787 | 12.60 / 16 |
| C6-original | 0.613 | 9.80 / 16 |
| C2 Inventory | 0.519 | 8.30 / 16 |
| C4 Recall | 0.488 | 7.80 / 16 |
| STARTER | 0.094 | 1.50 / 16 |

Trimmed beat original 4–0 (margins 3,3,2,2), C2 4–0 (2,3,2,2), C4 4–0
(3,3,2,2), STARTER 4–0 (4,5,4,4) — 16/16 calls won. The revision was
adopted on this evidence.

Full call logs: `../tournament.json` (round-robin) and
`../tournament2.json` (validation heat), including each call's reason,
verdict and margin. Candidate drafts: `../candidates.md`.

## Entry

- `main.py` — Python 3.13, stdlib only; writes the poem to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`).
- `README.md` — what the poem is doing and why.
- `LICENSE` — MIT, first line `SPDX-License-Identifier: MIT`.

Tested: two local runs (`MAKEFUN_OUTPUT_DIR=out`) produced byte-identical
`entry.txt` (405 characters, 407 bytes UTF-8, valid UTF-8, no trailing
newline, nothing else written). See the run log in the parent's report.
