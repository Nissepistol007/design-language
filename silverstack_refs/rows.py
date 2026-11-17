#!/usr/bin/env python3
"""rows.py <img> <x0> <y0> <x1> <y1> — find text baselines and their pitch in a column strip."""
import sys
import numpy as np
from PIL import Image

src, x0, y0, x1, y1 = sys.argv[1], *[int(v) for v in sys.argv[2:6]]
a = np.asarray(Image.open(src).convert("L").crop((x0, y0, x1, y1))).astype(float)
prof = (a > 120).sum(axis=1)
runs = []
inrun = False
for i, v in enumerate(prof):
    if v > 0 and not inrun:
        s = i
        inrun = True
    elif v == 0 and inrun:
        runs.append((y0 + s, y0 + i - 1))
        inrun = False
if inrun:
    runs.append((y0 + s, y0 + len(prof) - 1))
print("text bands (native px):")
for r in runs:
    print("  ", r, "h=", r[1] - r[0] + 1)
tops = [r[0] for r in runs]
if len(tops) > 1:
    d = np.diff(tops)
    print("pitches:", list(d))
    print("median pitch:", float(np.median(d)))
