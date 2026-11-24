"""News-23 entry: copy the pre-drawn front page (Monday 23 November 2026)
to the grader output directory. Standard library only, no network, and the
copy is byte for byte identical on every run."""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)

# Fail loudly rather than hand the grader a partial or missing image.
if os.path.getsize(DST) != os.path.getsize(SRC):
    raise SystemExit("entry.png copy incomplete")
