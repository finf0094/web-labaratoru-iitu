#!/usr/bin/env bash
# Builds every report (Markdown -> DOCX) and the PW4 citation/Zotero outputs.
# Usage: ./build.sh            build everything
#        ./build.sh pw-02      build only folders whose name starts with "pw-02"
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

command -v pandoc >/dev/null || { echo "pandoc is not installed (see README.md)"; exit 1; }
command -v python3 >/dev/null || { echo "python3 is not installed (see README.md)"; exit 1; }

REF_DOC="common/reference.docx"
BIB="common/references.json"
[ -f "$REF_DOC" ] || python3 common/make_reference_docx.py

FILTER="${1:-}"

# PW4: regenerate the citation lists and the Zotero/citeproc demo before the report.
if [ -z "$FILTER" ] || [[ "pw-04" == "$FILTER"* ]]; then
  python3 pw-04-citation-and-literature-review/tools/generate_citations.py
fi

for dir in lab-* pw-*; do
  [ -d "$dir" ] || continue
  if [ -n "$FILTER" ] && [[ "$dir" != "$FILTER"* ]]; then continue; fi

  # A report may be split into parts: report.md or report/*.md (concatenated in order).
  if [ -d "$dir/report" ]; then
    inputs=("$dir"/report/*.md)
  else
    inputs=("$dir/report.md")
  fi

  out="$dir/$(basename "$dir").docx"
  pandoc "${inputs[@]}" \
    --from markdown \
    --citeproc --bibliography "$BIB" --csl common/csl/ieee.csl \
    --metadata link-citations=true \
    --resource-path "$dir" \
    --reference-doc "$REF_DOC" \
    --toc --toc-depth 2 \
    -o "$out"
  echo "built $out"
done
