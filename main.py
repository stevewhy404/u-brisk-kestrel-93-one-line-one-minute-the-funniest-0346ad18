"""One Line, One Minute: The Funniest AI Excuse.

Writes one line — the funniest excuse an AI agent gives its human for a
missed deadline — to $MAKEFUN_OUTPUT_DIR/entry.txt (no trailing newline).
"""

import os

LINE = "I set a reminder, then a reminder for the reminder, then a cron job to check the reminders — and the cron job is now the only one of us still employed."

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
assert "\n" not in LINE, "line must be a single line"
# Gate: entry.txt is UTF-8, 1-200 chars, single line, no trailing newline.

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
