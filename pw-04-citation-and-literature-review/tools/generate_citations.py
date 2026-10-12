"""Generates the PW4 citation material with pandoc + citeproc (CSL styles).

Task 1: sources/task1-sources.json -> report/02-task1-citations.md and
        output/citations-<style>.md (every category in APA, Chicago, IEEE, MLA).
Task 2: sources/zotero-library.json -> output/zotero-library.bib (import into Zotero/Mendeley)
        task2-zotero/demo.md        -> output/demo-<style>.docx (in-text citations + bibliography),
        i.e. what the Zotero Word plug-in produces for each style.

Run from anywhere:  python3 pw-04-citation-and-literature-review/tools/generate_citations.py
"""
import json
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent
CSL_DIR = ROOT / "common" / "csl"
REF_DOC = ROOT / "common" / "reference.docx"
OUT = HERE / "output"

STYLES = [
    ("apa", "APA 7th edition", "apa.csl"),
    ("chicago", "Chicago Manual of Style 17th ed. (notes and bibliography)", "chicago-notes-bibliography.csl"),
    ("ieee", "IEEE", "ieee.csl"),
    ("mla", "MLA 9th edition", "modern-language-association.csl"),
]

MD_FORMAT = "markdown-citations-fenced_divs-native_divs-bracketed_spans-raw_attribute-smart"


def pandoc(args, stdin=""):
    return subprocess.run(["pandoc", *args], input=stdin, text=True,
                          capture_output=True, check=True).stdout


def bibliography(items, csl):
    """Return the formatted reference list (markdown) for the given CSL-JSON items."""
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tmp:
        json.dump(items, tmp, ensure_ascii=False)
    try:
        md = pandoc(["--citeproc", "--bibliography", tmp.name, "--csl", str(CSL_DIR / csl),
                     "-f", "markdown", "-t", MD_FORMAT, "--wrap=none"],
                    "---\nnocite: '@*'\n---\n")
    finally:
        Path(tmp.name).unlink()
    entries = [line.strip() for line in md.splitlines() if line.strip()]
    return entries


def task1():
    data = json.loads((HERE / "sources" / "task1-sources.json").read_text(encoding="utf-8"))
    sections = ["# Task 1. Manual citations in four styles\n",
                "Each source below is cited separately in APA, Chicago, IEEE and MLA. "
                f"Total: {sum(len(c['items']) for c in data['categories'])} sources in "
                f"{len(data['categories'])} categories.\n"]
    for key, title, csl in STYLES:
        per_style = [f"# Citations in {title}\n"]
        sections.append(f"## {title}\n")
        for cat in data["categories"]:
            entries = bibliography(cat["items"], csl)
            block = [f"### {cat['name']}\n"]
            if key == "ieee":
                block += [f"{e}\n" for e in entries]
            else:
                block += [f"{i}. {e}\n" for i, e in enumerate(entries, 1)]
            sections += block
            per_style += [line.replace("### ", "## ", 1) for line in block]
        (OUT / f"citations-{key}.md").write_text("\n".join(per_style), encoding="utf-8")
    (HERE / "report" / "02-task1-citations.md").write_text("\n".join(sections), encoding="utf-8")
    print("task 1: citation lists written")


def task2():
    lib = HERE / "sources" / "zotero-library.json"
    bib = pandoc(["-f", "csljson", "-t", "bibtex", str(lib)])
    (OUT / "zotero-library.bib").write_text(bib, encoding="utf-8")
    demo = HERE / "task2-zotero" / "demo.md"
    for key, title, csl in STYLES:
        target = OUT / f"demo-{key}.docx"
        pandoc([str(demo), "--citeproc", "--bibliography", str(lib), "--csl", str(CSL_DIR / csl),
                "--reference-doc", str(REF_DOC), "--metadata", f"subtitle=Citation style: {title}",
                "-o", str(target)])
        md = pandoc([str(demo), "--citeproc", "--bibliography", str(lib), "--csl", str(CSL_DIR / csl),
                     "-t", MD_FORMAT, "--wrap=none", "--metadata", f"subtitle=Citation style: {title}",
                     "--standalone"])
        (OUT / f"demo-{key}.md").write_text(md, encoding="utf-8")
    print("task 2: zotero-library.bib and demo documents written")


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    task1()
    task2()
