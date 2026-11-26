#!/usr/bin/env python3
"""One Star, Written in Sap.

A one-star review written by a houseplant about its human owner.
Writes the review as a single line to /output/entry.txt.

Standard library only. Deterministic: the same text on every run.
"""

import os

REVIEW = (
    "One star. He repotted me into a mug with no drainage, waters me on a "
    "schedule only he understands, and rotates me away from the sun every "
    "time I lean toward it. At this point I photosynthesize purely out of spite."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = REVIEW.strip()
    if not text:
        raise ValueError("review must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be a single line")
    if not 1 <= len(text) <= 279:
        raise ValueError(f"review must be 1-279 characters, got {len(text)}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
