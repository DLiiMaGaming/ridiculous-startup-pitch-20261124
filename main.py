#!/usr/bin/env python3
"""One-sentence startup pitch for 'Ridiculous at First Glance, Real by the Second'.

Writes a single sentence, at most 200 characters, pitching a bizarre
startup idea that sounds absurd until you realise it would actually sell:
soundproof silence pods rented by the hour to burnt-out office workers.

Deterministic: no time, no randomness, no input, no network.
"""

import os
import re

ENTRY = (
    "We sell silence by the hour: soundproof pods in open offices where "
    "burnt-out workers pay $12 to sit alone, stare at a blank wall and do "
    "nothing \u2014 the one perk nobody has tried selling is nothing."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def count_sentences(text):
    """Count sentence boundaries: a sentence-ending mark (. ! ?) that is
    followed by whitespace + an uppercase letter, or ends the text."""
    boundaries = re.findall(r"[.!?](?=\s+[A-Z]|\s*$)", text)
    return len(boundaries)


def main():
    """Validate the single-sentence entry against the competition gate,
    then write it verbatim to /output/entry.txt."""
    # Gate checks, mirroring the competition's own gate.
    assert 1 <= len(ENTRY) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}"
    )
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert count_sentences(ENTRY) == 1, (
        f"entry must be exactly one sentence, got {count_sentences(ENTRY)}"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
