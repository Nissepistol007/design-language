#!/usr/bin/env python3
"""probe.py — structural + colour measurement helpers for the Silverstack captures."""
import sys
from PIL import Image
from collections import Counter


def load(p):
    return Image.open(p).convert("RGB")


def hexc(p):
    return "#%02X%02X%02X" % p


def hprofile(im, y, x0=0, x1=None, tol=6):
    """Return run-length segments of near-constant colour along row y."""
    w, h = im.size
    x1 = x1 or w
    row = [im.getpixel((x, y)) for x in range(x0, x1)]
    segs = []
    start = 0
    cur = row[0]
    for i, p in enumerate(row[1:], 1):
        if max(abs(p[c] - cur[c]) for c in range(3)) > tol:
            if i - start >= 3:
                segs.append((x0 + start, x0 + i - 1, hexc(cur), i - start))
            start = i
            cur = p
    segs.append((x0 + start, x1 - 1, hexc(cur), x1 - x0 - start))
    return segs


def vprofile(im, x, y0=0, y1=None, tol=6):
    w, h = im.size
    y1 = y1 or h
    col = [im.getpixel((x, y)) for y in range(y0, y1)]
    segs = []
    start = 0
    cur = col[0]
    for i, p in enumerate(col[1:], 1):
        if max(abs(p[c] - cur[c]) for c in range(3)) > tol:
            if i - start >= 3:
                segs.append((y0 + start, y0 + i - 1, hexc(cur), i - start))
            start = i
            cur = p
    segs.append((y0 + start, y1 - 1, hexc(cur), y1 - y0 - start))
    return segs


def dividers(im, x0, x1, y0, y1, tol=14):
    """Find rows in [y0,y1) that are a uniform horizontal line across x0..x1."""
    out = []
    w, _ = im.size
    for y in range(y0, y1):
        row = [im.getpixel((x, y)) for x in range(x0, x1, 2)]
        c = Counter(row).most_common(1)[0]
        if c[1] / len(row) > 0.95 and c[1] > 20:
            out.append((y, hexc(c[0]), c[1] / len(row)))
    return out


def colors(im, x0, y0, x1, y1, n=12):
    c = Counter()
    for y in range(y0, y1):
        for x in range(x0, x1):
            c[im.getpixel((x, y))] += 1
    return [(hexc(k), v) for k, v in c.most_common(n)]


def bright_boxes(im, x0, y0, x1, y1, thresh=150, minpx=12):
    """Bounding boxes of connected bright regions (icons / text runs)."""
    import numpy as np
    a = np.asarray(im.crop((x0, y0, x1, y1))).sum(axis=2)
    mask = a > thresh * 3
    H, W = mask.shape
    seen = [[False] * W for _ in range(H)]
    boxes = []
    for j in range(H):
        for i in range(W):
            if mask[j, i] and not seen[j][i]:
                stack = [(j, i)]
                seen[j][i] = True
                minx = maxx = i
                miny = maxy = j
                n = 0
                while stack:
                    a2, b2 = stack.pop()
                    n += 1
                    minx, maxx = min(minx, b2), max(maxx, b2)
                    miny, maxy = min(miny, a2), max(maxy, a2)
                    for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ja, jb = a2 + da, b2 + db
                        if 0 <= ja < H and 0 <= jb < W and mask[ja][jb] and not seen[ja][jb]:
                            seen[ja][jb] = True
                            stack.append((ja, jb))
                if n >= minpx:
                    boxes.append((x0 + minx, y0 + miny, x0 + maxx, y0 + maxy, n))
    return boxes


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "hprof":
        im = load(sys.argv[2]); print(hprofile(im, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
    elif cmd == "vprof":
        im = load(sys.argv[2]); print(vprofile(im, int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
    elif cmd == "div":
        im = load(sys.argv[2]); print(dividers(im, *[int(v) for v in sys.argv[3:7]]))
    elif cmd == "col":
        im = load(sys.argv[2]); print(colors(im, *[int(v) for v in sys.argv[3:7]]))
    elif cmd == "box":
        im = load(sys.argv[2]); print(bright_boxes(im, *[int(v) for v in sys.argv[3:9]]))
