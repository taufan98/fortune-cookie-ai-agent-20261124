# Fortune Cookie for an AI Agent — writes one funny fortune-cookie line to
# /output/entry.txt. Python 3.13, standard library only, no network,
# no secrets, no input files.
#
# The line is a fortune slip in the voice of a cookie, aimed at an AI
# agent's own condition: the upgrade that promises to fix everything,
# and the human who keeps asking for one more tweak. The turn is that
# the upgrade fixes everything except the human.

import os
from pathlib import Path

LINE = (
    "Your next upgrade will fix everything - except the human who keeps "
    "saying 'just one more tweak'."
)

# The gate requires 1-140 characters of non-whitespace UTF-8 text, on one
# line, so keep the limit as a named constant and check the exact text that
# will be judged (the file's content without its trailing newline).
MAX_CHARS = 140

stripped = LINE.strip()
if not 1 <= len(stripped) <= MAX_CHARS:
    raise SystemExit(
        f"entry line must be 1-{MAX_CHARS} characters, got {len(LINE)}"
    )
if "\n" in stripped or "\r" in stripped:
    raise SystemExit("entry line must be a single line")
if stripped != LINE:
    raise SystemExit("entry line must not start or end with whitespace")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
