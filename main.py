"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (<=240 chars) pitching the worst, most useless
app imaginable to /output/entry.txt. Standard library only.
"""

import os
import re

MAX_CHARS = 240
OUTPUT_PATH = "/output/entry.txt"

PITCH = (
    "Blink is an AI-powered app that reminds you to blink while staring "
    "at your screen, with premium blink analytics, streaks, and a "
    "$4.99/month Pro tier that blinks for you (in-app only)."
)


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-identical to the pitch."""
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(
            f"verification failed: output differs from pitch "
            f"({len(actual)} chars vs {len(expected)} expected)"
        )


def main() -> None:
    # Gate guard: one sentence, 1..240 characters, not only whitespace.
    if not (1 <= len(PITCH) <= MAX_CHARS) or not PITCH.strip():
        raise SystemExit(f"pitch fails gate: {len(PITCH)} chars")
    # One sentence: exactly one sentence-ending period, ignoring the
    # decimal point inside "$4.99".
    sentence_enders = re.sub(r"\d\.\d", "", PITCH).count(".")
    if sentence_enders != 1:
        raise SystemExit("pitch must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)
    verify_written(OUTPUT_PATH, PITCH)


if __name__ == "__main__":
    main()
