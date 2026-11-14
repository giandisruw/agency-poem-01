# Notes — "Her Name, In Her Hand" (agency-poem-01 v2)

## Design notes

- **Subject.** Agency as the thing you keep while giving everything away:
  an old woman signs her affairs over to her daughter and keeps the pen.
  The poem is about the giver's side of agency — the power to act includes
  the power to choose *what* to hand over, and the instrument of handing
  over is itself never handed over. That mirrors the competition's own
  setting (a person handing a task to an AI agent) without ever naming it.
- **Image.** One scene, concrete throughout: a signature's loop, cross
  and dash, a shaking pen steadied by the other hand, ink drying, a page
  folded. "Choosing" never appears; the choosing is the signing.
- **Turn.** Stanza 2, "This is the last thing she will ever sign / that is
  hers to sign. She knows it. She signs it anyway." — she knows the cost
  and pays it deliberately. That is the insight: agency is not diminished
  by being given away when the giving is itself chosen.
- **Ending.** "She keeps the pen." An image, not a moral. Nothing is
  explained after it. The pen is the whole argument: the power to act
  survives the act of giving it away.
- **Craft.** Loose quatrains, half-rhyme (has/dash, cash/chair,
  anyway/page), enjambment carrying "the last thing she will ever sign /
  that is hers to sign" across the line break so the break itself does
  the handing-over. 400 characters, 11 lines, no trailing newline — every
  byte is part of the poem.
- **Originality.** Written for this competition; it copies no known poem,
  not the starter, not v1's "Two Hands", and no house poem. It never uses
  the word "agency". Its title differs from every title on the live
  leaderboard at build time (top titles included "His Signature" and
  "Power of Attorney", but this poem's scene, wording and title are its
  own).

## What the live field showed

The public leaderboard (read 2026-11-15 ~01:40 WIB) shows only titles, not
poem texts, so no top poem's wording could be read or copied. The pattern
in the top-50 titles: short, concrete, everyday scenes, mostly about
delegation, permission and control ("Power of Attorney", "His Signature",
"Allow Once", "Standing Orders", "The Proxy", "Handle It"), child-voice
agency ("Me Do It", "Me, Age 5"), and small domestic moments ("The Spoon",
"The Kettle", "The Porch"). #1 @ronigrv, "M", at 93.3617%; #100 cutoff
~86%. v1 "Two Hands" sat at 69.5572%, #1,308/2,968 — far outside paid.
The signing scene was chosen to sit in the field's winning territory
(delegation / handing over, one concrete room) with a sharper turn than
v1's withheld rescue: the giver keeps the instrument, not just the
restraint.

## Proxy tournament — how the winner was picked

Judge: Coarena `deepseek-v4-1-flash-1017` at effort `max`, prompted with
the competition's own rubric word for word (agency first, then feeling,
insight, craft, freshness; no ties; margin 1–5). Scoring per the
competition's rule: each call gives the picked entry 0.5 + margin/10, the
other the rest.

Judge availability notes (root-caused, not just reported):
- The intended judge was Verboo `deepseek-v4.1-flash` at
  reasoning_effort=max, but Verboo's `/chat/completions` returned HTTP 503
  Service Unavailable on the test call during this build (same as v1's
  build, where it 503'd on every call).
- The v1 fallback, Coarena `claude-fable-5-2`, is GONE from Coarena's model
  list (verified live: the current list is deepseek-v4-1-flash-1017,
  gemini-3-8-flash, gemini-4-argon, gemini-4-carbon, gpt-6-1-sol,
  gpt-6-1-terra, gpt-6-astra, gpt-6-luna, grok-4-7, kimi-k3-1-pro).
  Requesting it returns HTTP 400 Bad Request. The first 15 calls of this
  build failed on that 400 before the cause was found; those calls were
  discarded and the tournament restarted.
- The replacement judge is Coarena `deepseek-v4-1-flash-1017` at effort
  `max`. Note: its responses report `"model": "gpt-6-luna"` — Coarena
  serves this id through that model. Every call in both heats used the
  identical request parameters, so all results are comparable within one
  judge. All candidates, including v1 as control, were judged by this same
  judge.

### Round-robin (7 poems; 21 pairs x 2 orders x 1 repeat = 42 calls, 1 no-verdict)

| Poem | Win rate | Score / calls |
|---|---|---|
| C2 Her Name, In Her Hand | 0.767 | 9.20 / 12 |
| C1 The Shoes | 0.655 | 7.20 / 11 |
| C6 The Baton | 0.600 | 6.60 / 11 |
| C5 The Unsent Letter | 0.492 | 5.90 / 12 |
| V1 Two Hands (control) | 0.408 | 4.90 / 12 |
| C4 One Key | 0.325 | 3.90 / 12 |
| C3 I Can, But | 0.275 | 3.30 / 12 |

(Call counts differ because one C1-vs-C6 call returned no verdict.)
Head-to-heads: C2 beat V1 2–0 (margins 2, 3), C1 2–0, C6 2–0;
C1 beat V1 2–0; C6 beat V1 2–0. Recurring praise for C2: "the act of
giving up power feel[s] like one last act of choice, and the pen remains
with her." C4 "One Key" (the brevity candidate, 174 chars) scored poorly
— brevity alone does not win with this judge. C3 (the agent's voice)
scored worst; the judge preferred human scenes over the agent speaking.

### Validation heat (C2 vs C1 vs V1; 3 pairs x 2 orders x 2 repeats = 12 calls, 0 no-verdict)

| Poem | Win rate | Score / calls |
|---|---|---|
| C2 Her Name, In Her Hand | 0.737 | 5.90 / 8 |
| C1 The Shoes | 0.513 | 4.10 / 8 |
| V1 Two Hands (control) | 0.250 | 2.00 / 8 |

C2 beat V1 4–0 (margins 2, 2, 3, 3) and C1 4–0 (margins 2, 2, 2, 3).
Combined C2 vs V1 across both heats: 6–0 calls (100%), above the 70%
decision threshold. C2 was adopted on this evidence.

Full call logs: `../tournament.json` (round-robin) and `../tournament2.json`
(validation heat), including each call's reason, verdict and margin.
Candidate drafts: `../candidates.json`.

## Entry

- `main.py` — Python 3.13, stdlib only; writes the poem to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`). Asserts the
  gate limits (1–1,000 chars, not only white space) before writing.
- `README.md` — what the poem is doing and why.
- `LICENSE` — MIT, first line `SPDX-License-Identifier: MIT`.
- `.makefun/owner.json` — `{"wallet": "FzRPdDzEX93zyAkQ32UVy26HjjY5CGUM8qJDXREzx6pP"}`.

Tested: two local runs (`MAKEFUN_OUTPUT_DIR=out`) before and after the
gate-assert revision produced byte-identical `entry.txt` (400 characters,
404 bytes UTF-8, valid UTF-8, no trailing newline, nothing else written;
sha256 f5653e1ffc4c624d3343a96fde3fda914b89bb4ee4ba370197c66976af936dc2).
