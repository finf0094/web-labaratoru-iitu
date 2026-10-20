#!/usr/bin/env bash
# Builds the Midterm 1 article: figures -> diagrams -> mockup/code screenshots -> DOCX.
# Usage: ./build_article.sh            (from any directory)
#        ./build_article.sh --docx-only  only rebuild the DOCX from existing images
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/.." && pwd)"
cd "$HERE"

if [ "${1:-}" != "--docx-only" ]; then
  python3 experiment/make_figures.py
  if [ -n "${PLANTUML_JAR:-}" ]; then
    (cd diagrams && java -jar "$PLANTUML_JAR" -tpng ./*.puml)
  else
    echo "PLANTUML_JAR is not set: keeping the existing diagram PNGs"
  fi
  python3 mockup/screenshot.py || echo "Playwright/Chromium not available: keeping the mockup PNG"
  python3 code-screenshots/render_code.py
fi

[ -f "$ROOT/common/reference-article.docx" ] || python3 "$ROOT/common/make_reference_docx.py" article
OUT="KulushAskhat_IT1CCO-2402IS_MT1.docx"
pandoc article/article.md \
  --from markdown \
  --citeproc --bibliography "$ROOT/common/references.json" \
  --csl "$ROOT/common/csl/gost-r-7-0-5-2008-numeric.csl" \
  --resource-path "article" --columns 40 \
  --reference-doc "$ROOT/common/reference-article.docx" \
  -o "$OUT"
echo "built $HERE/$OUT"
