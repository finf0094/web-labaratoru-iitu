# Task 2. Using citation management tools (Zotero)

## Step 1 — Importing 10–20 academic papers

A library of **20 papers** on the research topic was prepared. The files for import are in the folder `output/` of this practical work:

* `zotero-library.ris` — RIS format with DOI, URL, pages and tags (recommended for Zotero and Mendeley);
* `zotero-library.bib` — BibTeX format with the same data;
* `zotero-library.json` — CSL-JSON (Zotero can also import it).

Import in Zotero 7: *File → Import… → A file → zotero-library.ris → Place imported collections and items into new collection*. Alternatively, papers can be added one by one with the *Add Item by Identifier* button (magic wand) by entering their DOI, or with the Zotero Connector browser extension directly from the publisher's page.

## Step 2 — Organising by topic (collections and tags)

| Collection (folder) | Papers | Typical tags |
|-----------------------|-------------------------------------------|-------------------|
| 01 Foundations and surveys | Brown et al. 2020; Wei et al. 2022; Mialon et al. 2023; Wang et al. 2024; Xi et al. 2025 | LLM, reasoning, survey, agents |
| 02 Retrieval-augmented generation | Lewis et al. 2020; Karpukhin et al. 2020; Asai et al. 2024; Fan et al. 2024; Liu N. F. et al. 2024 | RAG, dense retrieval, long context |
| 03 Tool use and the agent loop | Yao et al. 2023 (ReAct); Schick et al. 2023; Qin et al. 2024; Patil et al. 2024; Shinn et al. 2023 | agent loop, tool use, APIs |
| 04 Evaluation and benchmarks | Es et al. 2024 (RAGAS); Liu X. et al. 2024 (AgentBench); Yao et al. 2025 (τ-bench) | evaluation, benchmark |
| 05 Security and MCP | Greshake et al. 2023; Hou et al. 2026 | security, prompt injection, MCP |

Tags are imported automatically from the RIS file (`KW` fields). The collection of each item is written in its note (`N1`) so the folders can be recreated by dragging items into sub-collections (*New Subcollection…*).

## Step 3 — Inserting citations in four styles

Citations were inserted into the same text (`task2-zotero/demo.md`) in four styles. In Word, this is done with the Zotero plug-in: *Zotero tab → Add/Edit Citation*, and the style is switched with *Document Preferences*. In this repository the same operation is reproduced with the Citation Style Language processor (pandoc *citeproc*) using the official CSL style files that Zotero itself uses (`common/csl/`), so the result can be rebuilt with one command (`./build.sh pw-04`).

| Style | Example of in-text citation produced |
|-----------|----------------------------------------------------------------|
| APA 7 | The ReAct pattern interleaves reasoning and actions in a loop (Yao et al., 2023); models can also learn when to call tools (Schick et al., 2023). |
| Chicago 17 (notes) | The ReAct pattern interleaves reasoning and actions in a loop;¹⁰ … — footnote: ¹⁰ Shunyu Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models," *The Eleventh International Conference on Learning Representations (ICLR 2023)*, 2023, https://openreview.net/forum?id=WE_vluYUL-X. |
| IEEE | The ReAct pattern interleaves reasoning and actions in a loop [11]; models can also learn when to call tools [12]. |
| MLA 9 | The ReAct pattern interleaves reasoning and actions in a loop (Yao, Zhao, et al.); models can also learn when to call tools (Schick et al.). |

MLA adds the second author's name ("Yao, Zhao, et al.") automatically because the library contains two different first-author works by S. Yao, which is exactly the disambiguation rule of MLA.

## Step 4 — Generating the bibliography

At the end of each document the bibliography was generated automatically (*Zotero → Refresh / Document Preferences*; here — citeproc). The finished documents are:

* `output/demo-apa.docx` — APA 7, "References";
* `output/demo-chicago.docx` — Chicago notes and bibliography (footnotes + "Bibliography");
* `output/demo-ieee.docx` — IEEE, numbered list;
* `output/demo-mla.docx` — MLA 9, "Works Cited" entries.

Markdown copies (`output/demo-*.md`) allow the result to be viewed directly on GitHub.

## Step 5 — Screenshot of the workspace

*Figure 1 — Zotero workspace with the collections "01 Foundations…" – "05 Ethics…" and tags.*

> The screenshot is taken after importing `output/zotero-library.ris` into Zotero on the student's computer (the instructions are in the README of this practical work) and is saved as `screenshots/zotero-workspace.png`.
