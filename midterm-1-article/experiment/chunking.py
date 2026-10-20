"""Corpus loading and chunking strategies.

Every article of SQuAD v1.1 (train + dev, 490 Wikipedia articles) is one
document. Its paragraphs are joined with blank lines; the exact character
offsets of the gold answers are kept so that a chunk can be checked for
whether it fully contains an answer span.
"""
import json
import re
from dataclasses import dataclass
from pathlib import Path

WORD = re.compile(r"\S+")


@dataclass
class Article:
    title: str
    text: str
    paragraph_spans: list   # [(start, end)] of each paragraph in text
    split: str              # "train" or "dev"


@dataclass
class Chunk:
    article: int
    start: int
    end: int
    text: str
    n_words: int


def load_squad(data_dir):
    """Return articles and dev questions [(question, article_idx, [(start, end), ...])]."""
    articles, questions = [], []
    for split in ("train", "dev"):
        data = json.loads(Path(data_dir, f"{split}-v1.1.json").read_text(encoding="utf-8"))["data"]
        for art in data:
            parts, spans, pos = [], [], 0
            qs = []
            for para in art["paragraphs"]:
                ctx = para["context"]
                spans.append((pos, pos + len(ctx)))
                for qa in para["qas"]:
                    golds = [(pos + a["answer_start"], pos + a["answer_start"] + len(a["text"]))
                             for a in qa["answers"]]
                    qs.append((qa["question"], golds))
                parts.append(ctx)
                pos += len(ctx) + 2
            idx = len(articles)
            articles.append(Article(art["title"].replace("_", " "), "\n\n".join(parts), spans, split))
            if split == "dev":
                questions.extend((q, idx, g) for q, g in qs)
    return articles, questions


def fixed_chunks(articles, size, overlap):
    """Sliding windows of `size` words with `overlap` words shared between neighbours."""
    step = size - overlap
    chunks = []
    for ai, art in enumerate(articles):
        words = [(m.start(), m.end()) for m in WORD.finditer(art.text)]
        i = 0
        while i < len(words):
            win = words[i:i + size]
            s, e = win[0][0], win[-1][1]
            chunks.append(Chunk(ai, s, e, art.text[s:e], len(win)))
            if i + size >= len(words):
                break
            i += step
    return chunks


def paragraph_chunks(articles):
    """Structure-aware chunking: one chunk per original paragraph."""
    chunks = []
    for ai, art in enumerate(articles):
        for s, e in art.paragraph_spans:
            chunks.append(Chunk(ai, s, e, art.text[s:e], len(WORD.findall(art.text[s:e]))))
    return chunks


STRATEGIES = {
    "Fixed-50": lambda a: fixed_chunks(a, 50, 0),
    "Fixed-50 +25% overlap": lambda a: fixed_chunks(a, 50, 12),
    "Fixed-100": lambda a: fixed_chunks(a, 100, 0),
    "Fixed-100 +25% overlap": lambda a: fixed_chunks(a, 100, 25),
    "Fixed-200": lambda a: fixed_chunks(a, 200, 0),
    "Fixed-200 +25% overlap": lambda a: fixed_chunks(a, 200, 50),
    "Fixed-400": lambda a: fixed_chunks(a, 400, 0),
    "Fixed-400 +25% overlap": lambda a: fixed_chunks(a, 400, 100),
    "Paragraph": paragraph_chunks,
}
