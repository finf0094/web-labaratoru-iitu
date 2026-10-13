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
  extra=()
  ref="$REF_DOC"
  # A work with student.json (PW6) is personalised: name/group in text and figures,
  # its own formatting profile and the file name required by the assignment.
  if [ -f "$dir/student.json" ]; then
    name=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['name_surname'])" "$dir/student.json")
    group=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['group'])" "$dir/student.json")
    [ -f common/reference-pw6.docx ] || python3 common/make_reference_docx.py pw6
    ref="common/reference-pw6.docx"
    if python3 -c "import matplotlib" 2>/dev/null; then
      python3 "$dir/experiment/make_figures.py" >/dev/null
    fi
    extra=(--lua-filter "$dir/name.lua" --metadata "student_name=$name" --metadata "student_group=$group")
    out="$dir/${name//_/}_${group}_PW6.docx"
    rm -f "$dir"/*_PW6.docx
  fi
  pandoc "${inputs[@]}" \
    --from markdown \
    --citeproc --bibliography "$BIB" --csl common/csl/ieee.csl \
    --metadata link-citations=true \
    --resource-path "$dir:$dir/report" \
    --reference-doc "$ref" \
    --toc --toc-depth 2 \
    "${extra[@]}" \
    -o "$out"
  echo "built $out"
done
