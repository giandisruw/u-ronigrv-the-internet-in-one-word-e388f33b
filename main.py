#!/usr/bin/env python3
"""Entry for 'The Internet in One Word' (make.fun).

Writes exactly one word to the output entry file. The word was chosen by a
local pairwise Swiss tournament (14 candidates, 3 rounds, 21 games, 42 judge
calls, Caffeine router only, using the kit judge brief verbatim): "circus"
won with 2.15 points over 3 games.

Standard library only. Deterministic, no network, no randomness, no secrets.
"""

import os

WORD = "circus"


def main():
    # Gate in RULES.txt: 1 to 30 UTF-8 characters, not only white space,
    # and the brief's first criterion: a single word, nothing else.
    # No trailing newline: the file holds exactly the word.
    assert WORD and len(WORD) <= 30 and WORD.split() == [WORD]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
