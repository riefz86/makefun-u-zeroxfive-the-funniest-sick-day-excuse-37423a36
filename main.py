#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line (under 200 characters) to /output/entry.txt.
The line is a fixed, hand-written excuse: deterministic output.
"""

import os

EXCUSE = (
    "My smartwatch diagnosed me with an allergy to Mondays and locked "
    "my calendar until I rest, so I'm taking the day off on doctor's "
    "orders \u2014 the watch is the doctor."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
