#!/usr/bin/env python3
"""crop.py <src> <x> <y> <w> <h> <out> [scale]
Crop a region and optionally upscale/downscale for reading. Prints output size."""
import sys
from PIL import Image

src, x, y, w, h, out = sys.argv[1:7]
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
im = Image.open(src).convert("RGB")
print("source:", im.size)
box = (int(x), int(y), int(x) + int(w), int(y) + int(h))
region = im.crop(box)
if scale != 1.0:
    region = region.resize((max(1, int(region.width * scale)), max(1, int(region.height * scale))), Image.LANCZOS)
region.save(out)
print("wrote", out, region.size, "box", box)
