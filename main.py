#!/usr/bin/env python3
"""One Line, One Chill — make.fun bounty entry.

Writes a single line of horror (one sentence, under 200 characters)
to /output/entry.txt.
"""

import os

ENTRY = "The baby monitor said 'goodnight' in my voice \u2014 and I hadn't spoken all evening."

# The bounty requires a single sentence under 200 characters.
assert len(ENTRY) < 200, "entry must be under 200 characters"
assert ENTRY.count(".") == 1, "entry must be a single sentence"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
