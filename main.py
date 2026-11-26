"""What the Elevator Would Say - entry program.

Writes one line, the funniest thing a talking elevator would say,
in the elevator's own voice, to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os

# The entry: one observed scene, concrete numbers, a deadpan close.
# 108 characters, inside the 120-character cap.
ENTRY_TEXT = (
    "Floor 7. Four strangers, one mirror, 38 seconds of silence. "
    "I dinged early. Even I couldn't take it anymore."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def main():
    text = ENTRY_TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry length %d outside 1..%d" % (len(text), MAX_CHARS))
    if not text.strip():
        raise ValueError("entry is blank")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Re-read and confirm the written bytes are exactly the entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("written entry differs from ENTRY_TEXT")
    print("entry.txt: %d characters" % len(written))


if __name__ == "__main__":
    main()
