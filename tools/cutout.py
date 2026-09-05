# Recursive product-image background removal, replacing files IN PLACE.
#
# BiRefNet segmentation + pymatting foreground estimation: the second step
# re-computes true edge colors so semi-transparent edge pixels don't keep the
# old background mixed in (no halo on colored/dark theme tiles).
#
# Usage: python remove-bg.py <images-root>
#
# - .webp files are replaced with transparent webp, quality 85
# - .png files are replaced with transparent png
# - .jpg is skipped (no alpha channel)
# - already-transparent images are skipped, so re-runs only pick up new files
#
# Run via remove-bg.sh, which bootstraps the virtualenv.

import sys, time
import numpy as np
from pathlib import Path
from PIL import Image
from rembg import remove, new_session
from pymatting import estimate_foreground_ml

ROOT = Path(sys.argv[1]).resolve()
session = new_session("birefnet-general")

def has_alpha(img: Image.Image) -> bool:
    return img.mode in ("RGBA", "LA") and img.getextrema()[-1][0] < 255

def cutout(src: Image.Image) -> Image.Image:
    img = src.convert("RGB")
    rgba = remove(img, session=session)
    alpha = np.asarray(rgba)[:, :, 3].astype(np.float64) / 255.0
    rgb = np.asarray(img).astype(np.float64) / 255.0
    fg = estimate_foreground_ml(rgb, alpha)
    out = np.dstack([np.clip(fg * 255, 0, 255).astype(np.uint8),
                     (alpha * 255).astype(np.uint8)])
    return Image.fromarray(out, "RGBA")

files = sorted(p for p in ROOT.rglob("*")
               if p.suffix.lower() in (".webp", ".png") and "cache" not in p.parts)
total = len(files)
done = failed = skipped = 0
start = time.time()

for p in files:
    try:
        src = Image.open(p)
        if has_alpha(src):
            skipped += 1
            continue
        result = cutout(src)
        if p.suffix.lower() == ".png":
            result.save(p, "PNG")
        else:
            result.save(p, "WEBP", quality=85, method=4)
        done += 1
    except Exception as e:
        failed += 1
        print(f"FAILED {p}: {e}", flush=True)
    if (done + failed + skipped) % 20 == 0:
        rate = (time.time() - start) / max(done + failed, 1)
        eta = (total - done - failed - skipped) * rate / 60
        print(f"progress: {done+failed+skipped}/{total} (skip={skipped} fail={failed}) ~{rate:.1f}s/img ETA {eta:.0f}min", flush=True)

print(f"FINISHED: {done} ok, {skipped} skipped, {failed} failed of {total} in {(time.time()-start)/60:.1f}min", flush=True)
