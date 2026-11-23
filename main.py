"""One Emoji, One Smile — the single emoji most likely to make a stranger smile.

Writes exactly one emoji (1-8 chars, UTF-8, not whitespace-only) to /output/entry.txt.
"""

import os

EMOJI = "\U0001FAE9"  # melting face: warm, gently funny, instantly readable by anyone

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EMOJI)
