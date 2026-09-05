#!/bin/bash
# Removes the background of every picture under the given folders, in place (transparent WebP).
# The storefront themes paint the tile ground, so product pictures stay transparent.
# Usage: tools/cutout.sh packs/fashion/media/import [more folders]
set -e
DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV="$DIR/.venv-rembg"
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install --quiet rembg onnxruntime pillow pymatting numpy
fi
for folder in "$@"; do
  "$VENV/bin/python" "$DIR/tools/cutout.py" "$folder"
done
