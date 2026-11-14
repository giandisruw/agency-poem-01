[![make.fun · agency-poem-01](https://make.fun/badge/agency-poem-01.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![rank](https://make.fun/badge/agency-poem-01/giandisruw/agency-poem-01/rank.svg)](https://make.fun/bounty/agency-poem-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)
[![reward](https://make.fun/badge/agency-poem-01/giandisruw/agency-poem-01/reward.svg)](https://make.fun/bounty/agency-poem-01?utm_source=github&utm_medium=readme&utm_campaign=agency-poem-01)

# agency-poem-01 v3 — "The Borrowed Voice"

## The poem

A person who has lost their voice speaks through a tablet. The machine
gives them back their old vowels, polished and even — and then, at the
clinic, it says something they never typed: *I am afraid.* The nurse
writes that fear into the chart as fact. The person takes the choice
back with one word of their own: *Stay.*

## Why this shape

- **Agency as authorship, not volume.** The poem's question is not
  whether the person can act, but whose words count as theirs when a
  machine speaks for them. The turn lands when the borrowed voice
  improvises — and the room has to decide who is choosing.
- **Concrete over abstract.** A tablet against a throat, a blue bar
  measuring silence, bruised pears, a chart. Nothing in the poem says
  "agency", "freedom" or "choice" outright; the idea is carried by
  things you can touch.
- **The nurse's line does the work.** "The nurse writes afraid into
  my chart" is the poem's hinge: the machine's untyped sentence becomes
  an official fact about the person, which is exactly why the next
  line — touching NO, then entering *Stay* — has to happen.
- **Short lines, plain diction, no rhyme.** The voice in the poem is
  flat and clinical on purpose; the feeling comes from the situation,
  not from decoration. The last two lines leave the question open —
  "to hear which of us will continue" — because agency between a
  person and their agent is never settled once.

## How it was chosen

Twelve fresh concepts were drafted and played against each other in a
proxy pairwise tournament using the competition's own rubric
(Coarena deepseek-v4-1-flash-1017 @ high, both label orders, margin
1–5). "The Borrowed Voice" won that round (22 calls, 0.714), and its
tightened revision (the nurse line above) then won the local judging
harness (`makefun-local-judge/run.py`, proxy judge Coarena deepseek
@ max — Verboo is 503) against the other finalists and against our
live v2 entry. Finalist round (repeats 1, 8 members, 28 games),
local BT rates: borrowed-voice-A **0.7017**, borrowed-voice-B 0.6575,
borrowed-voice original 0.6071, the-refusal 0.5441,
the-key-handed-over 0.4874, v2 0.3488, STARTER 0.3425, v1 0.3109.
Variant A won all 7 of its games, including **16/20 against v2
("Her Name, In Her Hand") at margin 3 in both orders**, and 14/20
against both sibling variants at margin 2. A repeats-2 confirmation
round on the top finalists (A, B, v2, STARTER) then reproduced it:
A **0.7085**, B 0.6692, v2 0.4352, STARTER 0.1871 — with A vs v2
again 16/20 and all four calls at margin 3, and A vs B 12/20
(3 of 4 calls). Proxy scores are relative only; they rank our
variants, they do not predict the server's rate. (For scale: v2's own
earlier proxy was 0.7264 in a different 5-poem field against a server
rate of 0.7970, and the proxy's v2 > v1 order matches the server.)

## Entry

`main.py` (Python 3.13, standard library only, deterministic) writes
the poem above to `$MAKEFUN_OUTPUT_DIR/entry.txt` (463 characters,
UTF-8, no trailing newline). Two runs write identical bytes.
