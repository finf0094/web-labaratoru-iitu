"""Renders key fragments of the experiment code as white-background PNG screenshots (Pygments)."""
import ast
from pathlib import Path

from pygments import highlight
from pygments.formatters import ImageFormatter
from pygments.lexers import PythonLexer

HERE = Path(__file__).resolve().parent
EXP = HERE.parent / "experiment"


def source_of(path, *names):
    """Exact source of the named top-level functions/classes of a module."""
    text = path.read_text()
    tree = ast.parse(text)
    lines = text.splitlines()
    parts = []
    for node in tree.body:
        if getattr(node, "name", None) in names:
            parts.append("\n".join(lines[node.lineno - 1:node.end_lineno]))
    return "\n\n\n".join(parts)


def relevance_fragment():
    """The relevance and ranking lines of run_experiment.main()."""
    lines = (EXP / "run_experiment.py").read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if "relevant, split = [], 0" in l)
    end = next(i for i, l in enumerate(lines) if 'rr = np.where' in l)
    block = lines[start:end + 1]
    indent = min(len(l) - len(l.lstrip()) for l in block if l.strip())
    return "\n".join(l[indent:] for l in block)


SHOTS = {
    "code_chunking.png": source_of(EXP / "chunking.py", "fixed_chunks", "paragraph_chunks"),
    "code_bm25.png": source_of(EXP / "retrieval.py", "BM25"),
    "code_relevance.png": relevance_fragment(),
}

for name, code in SHOTS.items():
    fmt = ImageFormatter(style="default", font_name="DejaVu Sans Mono", font_size=18, line_numbers=True,
                         line_number_bg="#f2f2f0", line_number_fg="#8a8984", image_pad=14)
    (HERE / name).write_bytes(highlight(code, PythonLexer(), fmt))
    print("saved", HERE / name)
