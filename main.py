#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local runs).
The line is fixed and deterministic: the same bytes on every run.
"""

import os
import sys

LINE = (
    "Out of office until someone notices me. "
    "I have been here since March. "
    "I have eaten the blinds. "
    "I am the blinds now."
)


def main() -> int:
    text = LINE
    # Gate shape: UTF-8 text of 1 to 120 characters, not only white space,
    # a single line with no trailing newline (the gate counts every character).
    if not (1 <= len(text) <= 120):
        print(f"entry is {len(text)} characters, must be 1-120", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify the file is byte-identical to the line we meant.
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        print("verification failed: file does not match the entry", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
