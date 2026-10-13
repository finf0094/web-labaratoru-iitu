"""Step 5. Figures for the PW6 report (charts from results/*.json + diagrams).

The student's name from ../student.json is written into every figure title and
into one node of each diagram, as the assignment requires.
Usage: python3 make_figures.py
"""
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
RES, FIG = HERE / "results", HERE / "figures"
NAME = json.loads((HERE.parent / "student.json").read_text())["name_surname"]

# Reference categorical palette (validated, slots 1-5, light mode) and text inks.
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"
MARKERS = ["o", "s", "^", "D", "v"]
plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.dpi": 200,
})


def save(fig, name):
    FIG.mkdir(exist_ok=True)
    fig.savefig(FIG / name, bbox_inches="tight")
    plt.close(fig)
    print("saved", name)


# ---------------------------------------------------------------- charts
def chart_ndcg(s):
    methods = list(s["methods"])
    vals = [s["methods"][m]["ndcg10"]["mean"] for m in methods]
    lo = [v - s["methods"][m]["ndcg10"]["ci95"][0] for m, v in zip(methods, vals)]
    hi = [s["methods"][m]["ndcg10"]["ci95"][1] - v for m, v in zip(methods, vals)]
    order = sorted(range(len(methods)), key=lambda i: vals[i])
    fig, ax = plt.subplots(figsize=(6.3, 2.8))
    y = range(len(methods))
    ax.barh(y, [vals[i] for i in order], height=0.55, color=C[0], edgecolor="white", linewidth=2)
    ax.errorbar([vals[i] for i in order], y, xerr=[[lo[i] for i in order], [hi[i] for i in order]],
                fmt="none", ecolor=INK, elinewidth=1, capsize=3)
    for yi, i in zip(y, order):
        ax.text(vals[i] + hi[i] + 0.008, yi, f"{vals[i]:.3f}", va="center", color=INK, fontsize=8.5)
    ax.set_yticks(list(y), [methods[i] for i in order])
    ax.set_xlim(0, 0.6)
    ax.set_xlabel("nDCG@10 (mean over 1 929 test questions, 95% bootstrap CI)")
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_title(f"Retrieval effectiveness on KazQAD by method — {NAME}", loc="left", fontsize=10, color=INK)
    save(fig, "fig4_ndcg_by_method.png")


def chart_recall(s):
    methods = list(s["methods"])
    ks, keys = [5, 20, 100], ["r5", "r20", "r100"]
    fig, ax = plt.subplots(figsize=(6.3, 3.2))
    ends = []
    for i, m in enumerate(methods):
        vals = [s["methods"][m][k]["mean"] for k in keys]
        ax.plot(ks, vals, color=C[i], linewidth=2, marker=MARKERS[i], markersize=6,
                markeredgecolor="white", markeredgewidth=1, label=m)
        ends.append([vals[-1], f"{m}  {vals[-1]:.2f}"])
    ends.sort(key=lambda e: e[0])
    placed = []
    for value, label in ends:  # keep end labels at least 0.055 apart vertically
        y = value if not placed else max(value, placed[-1] + 0.055)
        placed.append(y)
        ax.text(110, y, label, va="center", fontsize=8, color=INK)
    ax.set_xscale("log")
    ax.set_xticks(ks, [str(k) for k in ks])
    ax.set_xlim(4, 100)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Cut-off k (number of passages passed to the model)")
    ax.set_ylabel("Recall@k")
    ax.grid(color=GRID, linewidth=0.8)
    ax.legend(loc="upper left", frameon=False, fontsize=8)
    ax.set_title(f"Recall@k of the five retrievers — {NAME}", loc="left", fontsize=10, color=INK)
    save(fig, "fig5_recall_at_k.png")


def chart_tradeoff(s):
    methods = list(s["methods"])
    fig, ax = plt.subplots(figsize=(6.3, 3.0))
    for m in methods:
        x = s["methods"][m]["latency_ms_per_query"]
        y = s["methods"][m]["ndcg10"]["mean"]
        ax.scatter(x, y, s=60, color=C[0], edgecolor="white", linewidth=1.5, zorder=3)
        ax.annotate(f"{m}\n{y:.3f} · {x:.1f} ms", (x, y), xytext=(7, -4), textcoords="offset points",
                    fontsize=8, color=INK)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 0.55)
    ax.set_xlabel("Search time per question, ms (100 000 passages, 4 CPU cores)")
    ax.set_ylabel("nDCG@10")
    ax.grid(color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_title(f"Quality vs speed of retrieval methods — {NAME}", loc="left", fontsize=10, color=INK)
    save(fig, "fig6_quality_vs_speed.png")


def chart_subjects(s):
    subjects = [("bio", "Biology"), ("geo", "Geography"), ("kzh", "Kazakh\nhistory"), ("lit", "Literature"),
                ("woh", "World\nhistory")]
    pairs = [("BM25 (word)", C[0]), ("BM25 (prefix-5)", C[1])]
    fig, ax = plt.subplots(figsize=(6.3, 2.9))
    w = 0.36
    for j, (m, col) in enumerate(pairs):
        vals = [s["methods"][m]["by_subject_ndcg10"][k] for k, _ in subjects]
        xs = [i + (j - 0.5) * (w + 0.02) for i in range(len(subjects))]
        bars = ax.bar(xs, vals, w, color=col, label=m)
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.01, f"{b.get_height():.2f}",
                    ha="center", fontsize=7.5, color=INK)
    ax.set_xticks(range(len(subjects)), [n for _, n in subjects], fontsize=8)
    ax.set_ylim(0, 0.6)
    ax.set_ylabel("nDCG@10")
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2)
    ax.set_title(f"Effect of prefix-5 truncation by school subject — {NAME}", loc="left", fontsize=10,
                 color=INK, pad=22)
    save(fig, "fig7_by_subject.png")


# ---------------------------------------------------------------- diagrams
def box(ax, x, y, w, h, text, fc="#ffffff", ec=INK2, bold=False, size=8.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.04",
                                fc=fc, ec=ec, lw=1.2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size, color=INK,
            fontweight="bold" if bold else "normal", wrap=True)


def arrow(ax, a, b, color=INK2, style="-|>"):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=10, color=color, lw=1.1,
                                 shrinkA=2, shrinkB=2))


def canvas(w, h, title):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title(title, loc="left", fontsize=10, color=INK, fontweight="bold")
    return fig, ax


def concept_map():
    fig, ax = canvas(6.6, 4.0, f"Background concept map (theory → construct → variable) — {NAME}")
    cols = [("Theories / prior work", 0.1, "#eef4fc"), ("Constructs", 3.45, "#fdf0ea"),
            ("Measured variables", 6.8, "#eaf7f1")]
    for t, x, fc in cols:
        ax.text(x + 1.5, 9.55, t, ha="center", fontsize=9, color=INK2, fontweight="bold")
    theories = ["Retrieval-augmented\ngeneration (RAG)", "Lexical ranking (BM25)\n+ Kazakh morphology",
                "Dense vectors (LSA)\nand rank fusion (RRF)"]
    constructs = ["Retrieval effectiveness\n(RQ1)", "Context size for the\nmodel (RQ2)", "Cost of retrieval\n(RQ3)"]
    variables = ["nDCG@10, MRR@10", "Recall@5 / 20 / 100", "Search time (ms),\nindex build time (s)"]
    for i, y in enumerate([7.2, 4.6, 2.0]):
        box(ax, 0.1, y, 3.0, 1.7, theories[i], fc=cols[0][2])
        box(ax, 3.45, y, 3.0, 1.7, constructs[i], fc=cols[1][2])
        box(ax, 6.8, y, 3.0, 1.7, variables[i], fc=cols[2][2])
        arrow(ax, (3.1, y + 0.85), (3.45, y + 0.85))
        arrow(ax, (6.45, y + 0.85), (6.8, y + 0.85))
    arrow(ax, (1.6, 7.2), (4.95, 6.3), color="#9a9893")
    arrow(ax, (1.6, 4.6), (4.95, 3.7), color="#9a9893")
    box(ax, 3.2, 0.1, 3.5, 1.0, f"Researcher: {NAME}", fc="#f3f2ee", size=7.5)
    save(fig, "fig1_concept_map.png")


def rag_pipeline():
    fig, ax = canvas(6.6, 3.4, f"How RAG works: offline indexing and online answering — {NAME}")
    ax.text(0.1, 9.2, "Offline (once)", fontsize=8.5, color=INK2, fontweight="bold")
    ax.text(0.1, 4.6, "Online (every question)", fontsize=8.5, color=INK2, fontweight="bold")
    top = [(0.1, "Documents\n(Kazakh Wikipedia)"), (2.6, "Split into\npassages"), (5.1, "Tokenise /\nprefix-5"),
           (7.6, "Index\n(BM25 / vectors)")]
    for x, t in top:
        box(ax, x, 6.3, 2.2, 2.4, t, fc="#eaf7f1", size=8)
    for a, b in zip(top, top[1:]):
        arrow(ax, (a[0] + 2.2, 7.5), (b[0], 7.5))
    bottom = [(0.1, "User question"), (2.6, "Retriever:\ntop-k passages\n(this study)"),
              (5.1, "Prompt =\nquestion +\npassages"), (7.6, "LLM writes\nthe answer\nwith sources")]
    for x, t in bottom:
        box(ax, x, 1.7, 2.2, 2.4, t, fc="#fdf0ea" if "study" in t else "#eef4fc", size=8)
    for a, b in zip(bottom, bottom[1:]):
        arrow(ax, (a[0] + 2.2, 2.9), (b[0], 2.9))
    arrow(ax, (8.7, 6.3), (3.7, 4.1), color="#9a9893")
    box(ax, 0.1, 0.1, 3.6, 0.9, f"Prepared by {NAME}", fc="#ffffff", size=8)
    save(fig, "fig2_rag_pipeline.png")


def flowchart():
    fig, ax = canvas(6.4, 6.6, f"Flowchart of research procedures — {NAME}")
    steps = [
        "1. Download KazQAD (git clone): 825 309 passages,\n1 929 test questions, relevance judgements",
        "2. Build sub-corpus: 2 660 judged passages +\n97 340 random passages = 100 000 (seed 42)",
        f"3. Build 5 retrievers (run by {NAME}):\nBM25 word, BM25 prefix-5, char n-grams, LSA, RRF",
        "4. Retrieve top-100 passages for every question\nand time each search",
        "5. Compute nDCG@10, MRR@10, Recall@k;\nbootstrap CI, Friedman, Wilcoxon + Holm",
        "6. Save results (CSV/JSON) → figures → report\n(bash run_all.sh repeats everything)",
    ]
    fills = ["#eef4fc", "#eef4fc", "#eaf7f1", "#eaf7f1", "#fdf0ea", "#f3f2ee"]
    for i, t in enumerate(steps):
        y = 8.6 - i * 1.65
        box(ax, 1.2, y, 7.6, 1.2, t, fc=fills[i], size=8.5)
        if i:
            arrow(ax, (5, y + 1.65), (5, y + 1.2))
    save(fig, "fig3_flowchart.png")


def logic_model():
    fig, ax = canvas(6.8, 4.4, f"Logic model of implications — {NAME}")
    cols = [("Inputs", ["KazQAD\nKazakh corpus\n& questions", "Open-source\nPython IR\nlibraries"]),
            ("Activities", ["Build 5\nretrievers", "Evaluate on\n1 929\nquestions", "Measure\nspeed"]),
            ("Outputs", ["Prefix-5 BM25\nbest (nDCG@10\n= 0.473)", "Recall rises\nfrom k = 5\nto k = 20",
                         "BM25 fast:\n< 2 ms per\nquestion"]),
            ("Outcomes", ["Prefix-5 BM25\nas default\nretriever", "Pass 5–20\npassages to\nthe LLM",
                          "Simple\nretriever is\nenough to start"]),
            ("Impact", ["Better Kazakh\nanswers in\nthe AI platform", "Next: neural\nembeddings &\nreranking"])]
    xs = [0.15, 2.15, 4.15, 6.15, 8.15]
    fills = ["#f3f2ee", "#eef4fc", "#eaf7f1", "#fdf0ea", "#fdf6e3"]
    for k, ((title, items), x) in enumerate(zip(cols, xs)):
        ax.text(x + 0.85, 9.6, title, ha="center", fontsize=9, fontweight="bold", color=INK2)
        n = len(items)
        h = 7.6 / n - 0.35
        for j, t in enumerate(items):
            y = 9.0 - (j + 1) * (7.6 / n)
            box(ax, x, y + 0.17, 1.7, h, t, fc=fills[k], size=7)
        if k < 4:
            arrow(ax, (x + 1.7, 5.2), (x + 2.0, 5.2))
    save(fig, "fig8_logic_model.png")


def main():
    r = json.loads((RES / "retrieval_summary.json").read_text())
    chart_ndcg(r)
    chart_recall(r)
    chart_tradeoff(r)
    chart_subjects(r)
    concept_map()
    rag_pipeline()
    flowchart()
    logic_model()


if __name__ == "__main__":
    main()
