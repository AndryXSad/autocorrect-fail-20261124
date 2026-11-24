#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one line, under 200 characters, that reads as a funny autocorrect
fail and nothing else, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Design: the line is a short text-message exchange. The intended word
("prescription") and the wrong word ("prostitution") share the pro-...-tion
shape, so the swap reads as a real autocorrect slip; the wrong word is
specific and surprising; the payoff ("we need to talk") lands on first read
with no explanation. The line was picked by a local pairwise tournament
among 14 fresh candidates, scored on the judge's own criteria in order
(one-line fail, first-read funny with a clear surprising wrong word, reads
as a real slip, clear without explanation, specific and original wrong word).
See DESIGN.md for the candidates, the scores and the full round-robin table.

Deterministic: the output is a fixed string. No randomness, no network,
no clock, no environment input besides the output directory. Two runs
produce byte-identical files.
"""

import os
from pathlib import Path

ENTRY = (
    "Texted my mom \u2018can you pick up my prescription?\u2019 \u2014 "
    "autocorrect sent \u2018can you pick up my prostitution?\u2019 "
    "and she replied \u2018we need to talk\u2019."
)


def main() -> None:
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1 to 199
    # characters, not only white space, on a single line.
    if not 1 <= len(ENTRY) <= 199:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-199")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    ENTRY.encode("utf-8")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
