#!/usr/bin/env bash
set -e
OUT_DIR="${1:-$HOME/aifs_classroom_yolo/images}"
COUNT="${2:-20}"
mkdir -p "$OUT_DIR"
echo "Saving $COUNT images to $OUT_DIR"

# quick camera test
rpicam-hello -t 2000 || true

for i in $(seq -w 1 "$COUNT"); do
  out="$OUT_DIR/classroom_${i}.jpg"
  echo "Capturing $out"
  rpicam-still -o "$out" --width 1280 --height 720 --timeout 1000 --nopreview
  sleep 2
done

echo "Done. Images are in $OUT_DIR"
