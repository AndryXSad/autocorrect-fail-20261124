# Design — Funniest Autocorrect Fail

## The task

One line, under 200 characters, that reads as a funny autocorrect fail and
nothing else. The house judge compares entries pairwise and weighs, most
important first:

1. The entry is a one-line autocorrect fail (anything else loses).
2. Funny on first read, with a clear and surprising wrong word.
3. Reads as a real autocorrect slip rather than a written joke.
4. Clear without explanation, fits in one line.
5. The wrong word is specific and original rather than a generic typo.

## Candidates

14 fresh lines were written for this entry, avoiding the field's overused
swaps (meeting/mating, wedding/weeding, see/sue, Satan, orgasm/organization,
pubic, condoms, funeral/funfair, kick/kiss, defrost/marinate children).
Each was scored 1–5 on the five criteria above, in order.

| # | Candidate (short name) | C1 | C2 | C3 | C4 | C5 |
|---|---|---|---|---|---|---|
| PRESCRIPTION | prescription → prostitution, mom, "we need to talk" | 5 | 5 | 4 | 5 | 5 |
| BREAD | bread → beard, wife comes home with a lumberjack | 5 | 4 | 5 | 5 | 4 |
| MUSSEL | muscle → mussel, coach, stop eating seafood | 5 | 4 | 5 | 5 | 3 |
| CIRCUS | circle back → circus back, ran away with the circus | 5 | 4 | 4 | 5 | 5 |
| ATTACKED | resume attached → attacked, security escorts me out | 5 | 4 | 4 | 5 | 4 |
| HIDING | hiking → hiding, date thinks I'm a serial killer | 5 | 4 | 4 | 4 | 4 |
| PIZZA | pizza → prison, wife asking questions | 5 | 4 | 3 | 5 | 4 |
| BLESSED | toilet blocked → blessed, plumber replies "amen" | 5 | 4 | 3 | 5 | 4 |
| OCEAN | dinner in the oven → in the ocean | 5 | 4 | 3 | 5 | 4 |
| NAUGHTY | nauseous → naughty, mom sends lecture + bible verse | 5 | 4 | 3 | 5 | 4 |
| EGGS | can't feel my legs → my eggs, trainer replies "...what" | 5 | 4 | 3 | 4 | 3 |
| BROKERED | heater broken → brokered, landlord sends an agent | 5 | 3 | 4 | 5 | 4 |
| SPOON | see you soon → see you spoon, into cutlery | 5 | 3 | 4 | 5 | 3 |
| FEELING | dentist, feeling vs filling (explains its own joke) | 4 | 3 | 3 | 4 | 3 |

## Tournament

Round-robin, 13 games each. A game is decided by the judge's own rule: go
through the criteria in order and let the first one where the two entries
differ decide.

| Place | Candidate | Wins / 13 |
|---|---|---|
| 1 | PRESCRIPTION | 13 |
| 2 | BREAD | 12 |
| 3 | MUSSEL | 11 |
| 4 | CIRCUS | 10 |
| 5 | ATTACKED | 9 |
| 6 | HIDING | 8 |
| 7 | PIZZA / BLESSED / OCEAN / NAUGHTY | 4 |
| 11 | EGGS | 3 |
| 12 | BROKERED | 2 |
| 13 | SPOON | 1 |
| 14 | FEELING | 0 |

## Winner

> Texted my mom ‘can you pick up my prescription?’ — autocorrect sent ‘can you pick up my prostitution?’ and she replied ‘we need to talk’.

137 characters, 151 bytes UTF-8. Why it won: the wrong word is shocking
and specific (C2, C5); "prescription" and "prostitution" share the
pro-...-tion shape, so the swap reads as a genuine autocorrect slip (C3);
the payoff needs no explanation (C4); and no other entry in the field uses
this swap (checked against all 155 submissions visible at build time).

## Program

`main.py` (stdlib only: `os`, `pathlib`) writes exactly this line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. It is deterministic — two runs produce
byte-identical files — and it self-checks the gate (1–199 characters,
single non-blank line) before writing. Verified locally: stdlib-only,
byte-identical across runs, gate pass, runs clean with the repository
read-only.
