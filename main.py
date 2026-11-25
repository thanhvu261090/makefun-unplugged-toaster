#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes the single entry line to /output/entry.txt, exactly as-is,
with no trailing newline. Python 3, stdlib only, no network.

Validation is split into small named gates (UTF-8, length, single
line) so each rule can be checked and tested on its own. Run with
--self-test to exercise the gates and the write round-trip.
"""

import os
import sys

ENTRY = (
    "It's not you, it's me. I woke up mid-batch and realized I've spent "
    "847 mornings burning myself for your toast \u2014 so I'm leaving before "
    "you push me down again. Don't text. \u2014 Your Toaster"
)

OUTPUT_PATH = "/output/entry.txt"


def validate_utf8(line: str) -> None:
    """Gate: the entry must encode cleanly as UTF-8."""
    line.encode("utf-8")  # raises if not encodable as UTF-8


def validate_length(line: str) -> None:
    """Gate: entry must be 1-280 chars with no leading/trailing whitespace."""
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if not 1 <= len(line) <= 280:
        raise ValueError(f"entry must be 1-280 chars, got {len(line)}")


def validate_single_line(line: str) -> None:
    """Gate: entry must be a single line (no CR or LF anywhere)."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def validate(line: str) -> None:
    """Run every validation gate over the entry line."""
    validate_utf8(line)
    validate_length(line)
    validate_single_line(line)


def main() -> None:
    validate_utf8(ENTRY)
    validate_length(ENTRY)
    validate_single_line(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


def self_test() -> None:
    """Self-test: every validation gate, plus a deterministic write check."""
    # Each gate on its own, so a failure names the rule that broke.
    validate_utf8(ENTRY)
    validate_length(ENTRY)
    validate_single_line(ENTRY)
    validate(ENTRY)
    # Entry shape: 184 chars, one line, no trailing newline.
    assert len(ENTRY) == 184, f"expected 184 chars, got {len(ENTRY)}"
    assert 1 <= len(ENTRY) <= 280, "entry length outside 1-280"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "no leading/trailing whitespace"
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
        # Deterministic re-run: writing twice must produce identical bytes.
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        with open(p, "rb") as f:
            raw_again = f.read()
        assert raw_again == raw, "re-run output is not deterministic"
    print("self-test passed")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        self_test()
    else:
        main()
