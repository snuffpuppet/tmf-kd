#!/usr/bin/env bash
# Render all capability-map HTML files to PDF + PNG via Chrome headless.
# Usage: ./render.sh
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# (basename, png-window-width, png-window-height)
TARGETS=(
  "capability-map-s2r 1800 1200"
  "capability-map 1800 1400"
  "capability-map-combined 2200 2400"
)

for entry in "${TARGETS[@]}"; do
  read -r base w h <<< "$entry"
  src="$DIR/$base.html"
  pdf="$DIR/$base.pdf"
  png="$DIR/$base.png"

  if [[ ! -f "$src" ]]; then
    echo "skip — $src not found"
    continue
  fi

  echo "rendering $base..."

  # PDF — page size from @page CSS in each HTML
  "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$pdf" \
    "file://$src" 2>/dev/null

  # PNG — at 2× device scale for crispness
  "$CHROME" --headless --disable-gpu \
    --window-size="$w","$h" \
    --screenshot="$png" \
    --hide-scrollbars \
    --force-device-scale-factor=2 \
    "file://$src" 2>/dev/null
done

echo "---"
ls -la "$DIR"/*.pdf "$DIR"/*.png
