#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single deadpan one-line joke to /output/entry.txt.

The joke is a fixed string: the program is deterministic on purpose, so
every run (local or in the grading sandbox) produces byte-identical output.
Standard library only; no network, no files read, no cwd dependence.
"""

import os

JOKE = (
    "My therapist says I use humor to avoid my feelings. "
    "Anyway, did you hear the one about my childhood?"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert text == text.strip() and "\n" not in text, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the file is exactly the one-line joke.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
