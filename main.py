"""Fortune Cookie Wisdom for Developers — one original line.

Writes the entry line to /output/entry.txt (created if missing).
Pure Python standard library; deterministic: the same line every run.
"""

import os

LINE = (
    "The bug is never in the code you suspect; "
    "it is in the code you trusted."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)
    # Read back what we wrote: the gate requires 1-120 chars of real text.
    with open(path, encoding="utf-8") as f:
        written = f.read().strip()
    assert written == text, "round-trip mismatch"
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()
