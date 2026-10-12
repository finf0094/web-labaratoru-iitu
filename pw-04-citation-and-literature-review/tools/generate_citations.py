"""Generates the PW4 citation material with pandoc + citeproc (CSL styles).

All bibliographic data live in common/references.json (CSL-JSON).

Task 1: sources/task1-sources.json -> report/02-task1-citations.md and
        output/citations-<style>.md (every category in APA, Chicago, IEEE, MLA).
Task 2: sources/zotero-collections.json -> output/zotero-library.json / .bib
        (import into Zotero or Mendeley; tags become "keywords"),
        task2-zotero/demo.md -> output/demo-<style>.docx/.md (in-text citations +
        bibliography), i.e. what the Zotero Word plug-in produces for each style.

Run from anywhere:  python3 pw-04-citation-and-literature-review/tools/generate_citations.py
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent
CSL_DIR = ROOT / "common" / "csl"
REF_DOC = ROOT / "common" / "reference.docx"
OUT = HERE / "output"
REFS = {item["id"]: item for item in
        json.loads((ROOT / "common" / "references.json").read_text(encoding="utf-8"))}

STYLES = [
    ("apa", "APA 7th edition", "apa.csl"),
    ("chicago", "Chicago Manual of Style 17th ed. (notes and bibliography)", "chicago-notes-bibliography.csl"),
    ("ieee", "IEEE", "ieee.csl"),
    ("mla", "MLA 9th edition", "modern-language-association.csl"),
]

MD_FORMAT = "markdown-citations-raw_html-fenced_divs-native_divs-bracketed_spans-native_spans-raw_attribute-smart"


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


def polish(style, ids, entry):
    """Small post-fixes where the stock CSL output deviates from the style guide."""
    patents = ids and all(REFS[i]["type"] == "patent" for i in ids)
    theses = ids and all(REFS[i]["type"] == "thesis" for i in ids)
    if patents and style in ("ieee", "mla"):
        entry = entry.replace("No. ", "U.S. Patent ", 1)
    if style == "ieee":
        entry = entry.replace("Geneva., ", "Geneva, Switzerland, ")
        entry = re.sub(r"(\d{4}) Available:", r"\1. Available:", entry)
    if theses and style == "mla":
        # MLA 9: Author. Title. Year. Institution, PhD dissertation. URL.
        entry = re.sub(r"^(.*?\*\. )(\d{4}), (<[^>]+>)\. (.+?), Doctoral dissertation\.$",
                       r"\1\2. \4, PhD dissertation. \3.", entry)
    return entry


def task1():
    data = json.loads((HERE / "sources" / "task1-sources.json").read_text(encoding="utf-8"))
    sections = ["# Task 1. Manual citations in four styles\n",
                "Each source below is cited separately in APA, Chicago, IEEE and MLA. "
                f"Total: {sum(len(c.get('ids', c.get('manual', []))) for c in data['categories'])} sources in "
                f"{len(data['categories'])} categories.\n"]
    for key, title, csl in STYLES:
        per_style = [f"# Citations in {title}\n"]
        sections.append(f"## {title}\n")
        for cat in data["categories"]:
            if "manual" in cat:
                entries = [m[key] for m in cat["manual"]]
                if key == "ieee":
                    entries = [f"\\[{i}\\] {e}" for i, e in enumerate(entries, 1)]
            else:
                entries = [polish(key, cat["ids"], e)
                           for e in bibliography([REFS[i] for i in cat["ids"]], csl)]
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


RIS_TYPES = {"article-journal": "JOUR", "article-magazine": "MGZN", "paper-conference": "CONF",
             "chapter": "CHAP", "book": "BOOK"}
BIB_TYPES = {"article-journal": "article", "article-magazine": "article",
             "paper-conference": "inproceedings", "chapter": "incollection", "book": "book"}


def to_ris(items, collections):
    """RIS keeps DOI and tags (KW); Zotero imports it into a new collection."""
    folder = {i: name for name, ids in collections.items() for i in ids}
    lines = []
    for it in items:
        lines.append(f"TY  - {RIS_TYPES.get(it['type'], 'GEN')}")
        for a in it.get("author", []):
            if "family" in a:  # "others" (et al.) has no RIS equivalent
                lines.append(f"AU  - {a['family']}, {a['given']}")
        lines.append(f"PY  - {it['issued']['date-parts'][0][0]}")
        lines.append(f"TI  - {it['title']}")
        if "container-title" in it:
            lines.append(f"T2  - {it['container-title']}")
        for tag, key in (("VL", "volume"), ("IS", "issue"), ("DO", "DOI"),
                         ("UR", "URL"), ("PB", "publisher"), ("CY", "publisher-place")):
            if key in it:
                lines.append(f"{tag}  - {it[key]}")
        if "page" in it:
            start, _, end = it["page"].partition("-")
            lines.append(f"SP  - {start}")
            if end:
                lines.append(f"EP  - {end}")
        for kw in filter(None, it.get("keyword", "").split(", ")):
            lines.append(f"KW  - {kw}")
        lines.append(f"N1  - Collection: {folder.get(it['id'], '')}")
        lines.append("ER  - \n")
    return "\n".join(lines)


def to_bibtex(items):
    out = []
    for it in items:
        fields = {
            "author": " and ".join(f"{a['family']}, {a['given']}" if "family" in a else a["literal"]
                                   for a in it.get("author", [])),
            "title": "{" + it["title"] + "}",
            "year": str(it["issued"]["date-parts"][0][0]),
            "journal" if it["type"].startswith("article") else "booktitle": it.get("container-title"),
            "volume": it.get("volume"), "number": it.get("issue"),
            "pages": it.get("page", "").replace("-", "--") or None,
            "publisher": it.get("publisher"), "address": it.get("publisher-place"),
            "doi": it.get("DOI"), "url": it.get("URL"), "keywords": it.get("keyword"),
        }
        body = ",\n".join(f"  {k} = {{{v}}}" for k, v in fields.items() if v)
        out.append(f"@{BIB_TYPES.get(it['type'], 'misc')}{{{it['id']},\n{body}\n}}\n")
    return "\n".join(out)


def task2():
    cfg = json.loads((HERE / "sources" / "zotero-collections.json").read_text(encoding="utf-8"))
    items = []
    for ids in cfg["collections"].values():
        for i in ids:
            item = dict(REFS[i])
            item["keyword"] = ", ".join(cfg["tags"].get(i, []))
            items.append(item)
    lib = OUT / "zotero-library.json"
    lib.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "zotero-library.ris").write_text(to_ris(items, cfg["collections"]), encoding="utf-8")
    (OUT / "zotero-library.bib").write_text(to_bibtex(items), encoding="utf-8")
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
