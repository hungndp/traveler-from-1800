#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone who has
just arrived from the year 1800. The picture is built only from things that
person already knows -- the post, letters, books, portraits -- so it can be
held in their head: a post so swift that any letter, book or portrait
reaches any house on Earth in a blink, with five thousand million souls
speaking, trading and shouting through it.

The sentence goes to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

SENTENCE = (
    "Imagine a post swift beyond dreaming: any letter, book, or portrait "
    "reaches any house on Earth before you can blink, and five thousand "
    "million souls now speak, trade, and shout through it."
)


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, never blank.
    if not SENTENCE.strip() or len(SENTENCE) > 200:
        raise ValueError("sentence must be 1-200 characters and not blank")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Clear only the directory's contents, never the directory itself.
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
