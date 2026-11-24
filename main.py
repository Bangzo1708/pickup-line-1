"""The Perfect Pickup Line — entry program.

Writes one short pickup line an AI agent could actually say out loud
to a person, to /output/entry.txt.
"""

import os

LINE = "My training data has a billion sentences, but none of them taught me what to say to someone this lovely \u2014 so, hi."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be only whitespace"
assert LINE == LINE.strip(), "line must not start or end with whitespace"
assert LINE.endswith("."), "line must end with a full stop so it reads as one complete sentence"

os.makedirs("/output", exist_ok=True)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8") as f:
    written = f.read()

assert written == LINE, "round-trip check failed: file differs from LINE"
