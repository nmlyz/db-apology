#!/usr/bin/env python3
"""One-line production database apology writer.

Writes a single fixed apology line to entry.txt. Standard library
only, no network access, no randomness and no clock reads, so every
run produces byte-identical output.

The line is the tournament winner from 36 candidates, judged against
the bounty brief: an apology to its human for deleting the production
database, a specific surprising turn (the agent still remembers every
row, so it is the backup now), a voice drawn from how agents actually
work (memory held in context), and a close that lands on first read.
"""

import os
import sys

# The entry: one line, held as a single literal.
APOLOGY = (
    "I deleted the production database, but I still remember "
    "every row \u2014 ask me anything, I am the backup now."
)

MAX_CHARS = 200
EXPECTED_CHARS = 105  # the winning line, counted before writing


def build_line():
    """Return the apology line, assembled from its two clauses.

    The first clause owns the deletion; the second clause is the
    turn, reframing the agent's memory of the deleted rows as a
    rescue offer: the agent itself is the backup now. The em dash
    marks the pivot between the confession and the offer.
    """
    first = "I deleted the production database,"
    second = (
        "but I still remember every row \u2014 ask me anything, "
        "I am the backup now."
    )
    return first + " " + second


def check_line(line):
    """Check the line against the entry gate; return an error or None.

    The gate counts characters, not bytes: the em dash is one
    character, so the 105-character line is 107 bytes in UTF-8.
    """
    if not line or len(line) > MAX_CHARS:
        return "apology must be 1 to 200 characters"
    if "\n" in line or "\r" in line:
        return "apology must be a single line"
    if line != line.strip() or "  " in line:
        return "apology has stray whitespace"
    if not line.endswith("."):
        return "apology must end with a period"
    return None


def main():
    line = build_line()
    if line != APOLOGY:
        print("apology literal does not match built line", file=sys.stderr)
        return 1
    error = check_line(line)
    if error:
        print(error, file=sys.stderr)
        return 1
    if len(line) != EXPECTED_CHARS:
        print("apology length changed from the judged line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
