#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the single entry line to /output/entry.txt, exactly as-is,
with no trailing newline. Python 3, stdlib only, no network.
"""

import os
import sys

ENTRY = (
    "It's not you, it's me. I woke up mid-batch and realized I've spent "
    "847 mornings burning myself for your toast \u2014 so I'm leaving before "
    "you push me down again. Don't text. \u2014 Your Toaster"
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate: UTF-8, 1-280 chars, single line, no leading/trailing whitespace."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(line)}")
    line.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


def self_test() -> None:
    """Small self-test: validate the entry and a round-trip write."""
    validate(ENTRY)
    assert len(ENTRY) == 184, f"expected 184 chars, got {len(ENTRY)}"
    assert ENTRY.count("\n") == 0
    assert "mid-batch" in ENTRY
    assert "Toaster" in ENTRY
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "entry.txt")
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        with open(p, "rb") as f:
            raw = f.read()
        assert raw == ENTRY.encode("utf-8"), "round-trip bytes differ"
        assert not raw.endswith(b"\n"), "no trailing newline allowed"
    print("self-test passed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        self_test()
    else:
        main()
