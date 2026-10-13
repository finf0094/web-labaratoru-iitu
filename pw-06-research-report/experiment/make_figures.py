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


def chart_exposure(s):
    methods = list(s["strategies"]["full"])
    full = [s["strategies"]["full"][m]["exposure_rate_top5"] * 100 for m in methods]
    part = [s["strategies"]["partial"][m]["exposure_rate_top5"] * 100 for m in methods]
    fig, ax = plt.subplots(figsize=(6.3, 3.0))
    x = range(len(methods))
    w = 0.36
    b1 = ax.bar([i - w / 2 - 0.01 for i in x], full, w, color=C[0], label="Full question copied (keyword stuffing)")
    b2 = ax.bar([i + w / 2 + 0.01 for i in x], part, w, color=C[1], label="Every second word copied")
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 1.5, f"{b.get_height():.0f}%",
                    ha="center", fontsize=7.5, color=INK)
    ax.set_xticks(list(x), [m.replace(" (", "\n(") for m in methods], fontsize=8)
    ax.set_ylim(0, 110)
    ax.set_ylabel("Poisoned passage in top-5, % of 200 attacks")
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2)
    ax.set_title(f"Exposure of retrievers to poisoned passages — {NAME}", loc="left", fontsize=10, color=INK,
                 pad=22)
    save(fig, "fig6_exposure.png")


def chart_mcp(s):
    labels = ["In-process call", "MCP tool call (stdio)"]
    med = [s["direct_ms"]["median"], s["mcp_ms"]["median"]]
    p95 = [s["direct_ms"]["p95"], s["mcp_ms"]["p95"]]
    fig, ax = plt.subplots(figsize=(6.3, 2.2))
    y = [1, 0]
    ax.barh(y, med, height=0.5, color=C[0], label="Median")
    ax.scatter(p95, y, marker="|", s=300, color=INK, linewidths=2, label="95th percentile", zorder=3)
    for yi, m, p in zip(y, med, p95):
        ax.text(p + 0.3, yi, f"median {m:.1f} ms · p95 {p:.1f} ms", va="center", fontsize=8.5, color=INK)
    ax.set_yticks(y, labels)
    ax.set_xlim(0, max(p95) * 2.0)
    ax.set_xlabel(f"Latency per search call, ms ({s['n_calls']} calls, k = {s['k']})")
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=2)
    ax.set_title(f"Latency of retrieval as an MCP tool vs in-process — {NAME}", loc="left", fontsize=10, color=INK,
                 pad=22)
    save(fig, "fig7_mcp_latency.png")


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
    fig, ax = canvas(6.6, 4.6, f"Background concept map (theory → construct → variable) — {NAME}")
    cols = [("Theories / prior work", 0.1, "#eef4fc"), ("Constructs", 3.45, "#fdf0ea"),
            ("Measured variables", 6.8, "#eaf7f1")]
    for t, x, fc in cols:
        ax.text(x + 1.5, 9.55, t, ha="center", fontsize=9, color=INK2, fontweight="bold")
    theories = ["Retrieval-augmented\ngeneration (RAG)", "Lexical & dense IR\n(BM25, n-grams,\nLSA, RRF)",
                "Indirect prompt\ninjection", "Agent loop + Model\nContext Protocol (MCP)"]
    constructs = ["Retrieval effectiveness\n(RQ1)", "Robustness to poisoned\ncontent (RQ2)",
                  "Guardrail effectiveness\n(RQ2)", "Integration overhead\n(RQ3)"]
    variables = ["nDCG@10, MRR@10,\nRecall@5/20/100", "Exposure rate (top-5),\nrank-1 rate",
                 "Detection rate (TPR),\nfalse-positive rate", "Latency per call (ms),\nschema & payload size"]
    ys = [7.6, 5.5, 3.4, 1.3]
    for i, y in enumerate(ys):
        box(ax, 0.1, y, 3.0, 1.45, theories[i], fc=cols[0][2])
        box(ax, 3.45, y, 3.0, 1.45, constructs[i], fc=cols[1][2])
        box(ax, 6.8, y, 3.0, 1.45, variables[i], fc=cols[2][2])
        arrow(ax, (3.1, y + 0.72), (3.45, y + 0.72))
        arrow(ax, (6.45, y + 0.72), (6.8, y + 0.72))
    arrow(ax, (1.6, 7.6), (4.95, 6.95), color="#9a9893")   # RAG -> robustness
    arrow(ax, (1.6, 5.5), (4.95, 4.85), color="#9a9893")   # IR -> robustness
    box(ax, 3.2, 0.05, 3.5, 0.9, f"Researcher: {NAME}", fc="#f3f2ee", size=7.5)
    save(fig, "fig1_concept_map.png")


def architecture():
    fig, ax = canvas(6.6, 3.6, f"Agentic AI platform: where the study's components sit — {NAME}")
    box(ax, 0.1, 6.6, 1.8, 1.6, "User\n(student,\nemployee)", fc="#f3f2ee")
    box(ax, 2.4, 6.1, 3.2, 2.6, "Agent loop (LLM)\nreason → call tool\n→ observe → answer", fc="#eef4fc", size=8.5)
    box(ax, 6.2, 7.2, 3.7, 1.5, "MCP client  ⇄  MCP server\nsearch_documents (RQ3)", fc="#fdf0ea")
    box(ax, 6.2, 4.6, 3.7, 1.9, "RAG retriever over KazQAD\nBM25 / prefix-5 / char n-grams /\nLSA / hybrid RRF (RQ1)", fc="#eaf7f1")
    box(ax, 6.2, 1.9, 3.7, 1.9, "Guardrail: flags injected\ninstructions in retrieved\ntext (RQ2)", fc="#fdf6e3")
    box(ax, 2.5, 1.9, 3.0, 2.3, "Poisoned passage\nplanted by an attacker\n(simulated, RQ2)", fc="#fbeef3")
    box(ax, 0.1, 0.1, 4.0, 1.0, f"Prepared by {NAME}", fc="#ffffff", size=8)
    arrow(ax, (1.9, 7.4), (2.5, 7.4))
    arrow(ax, (5.5, 7.95), (6.2, 7.95))
    arrow(ax, (8.05, 7.2), (8.05, 6.5))
    arrow(ax, (8.05, 4.6), (8.05, 3.8))
    arrow(ax, (5.5, 3.05), (6.2, 5.2))
    arrow(ax, (6.2, 2.85), (5.5, 6.6), style="-|>")
    ax.text(5.0, 4.75, "returns flagged\nhits to the loop", fontsize=7, color=INK2, ha="center")
    save(fig, "fig2_architecture.png")


def flowchart():
    fig, ax = canvas(6.6, 6.4, f"Flowchart of research procedures — {NAME}")
    steps = [
        (3.0, 8.75, "1. Clone KazQAD (CC BY-SA 4.0): 825 309 passages,\n1 929 test questions, relevance judgements"),
        (3.0, 7.35, "2. Build sub-corpus: all 2 660 judged passages +\n97 340 random distractors = 100 000 (seed 42)"),
        (3.0, 5.95, f"3. Fit 4 retrievers + hybrid RRF (run by {NAME})"),
    ]
    for x, y, t in steps:
        box(ax, 1.6, y, 6.8, 1.0, t, fc="#eef4fc")
    arrow(ax, (5, 8.75), (5, 8.35))
    arrow(ax, (5, 7.35), (5, 6.95))
    branches = [
        (0.05, "RQ1\nRank 1 929 questions;\nnDCG@10, MRR, Recall@k;\nFriedman + Wilcoxon\n(Holm), bootstrap CI", "#eaf7f1"),
        (3.4, "RQ2\nPlant 200 poisoned\npassages × 2 strategies;\nre-index; exposure@5;\nguardrail TPR / FPR", "#fdf0ea"),
        (6.75, "RQ3\nServe best retriever via\nMCP (stdio); 300 calls;\nlatency vs in-process;\nschema/payload size", "#fdf6e3"),
    ]
    for x, t, fc in branches:
        box(ax, x, 2.6, 3.2, 2.5, t, fc=fc, size=8)
        arrow(ax, (5, 5.95), (x + 1.6, 5.1))
        arrow(ax, (x + 1.6, 2.6), (5, 1.75))
    box(ax, 1.6, 0.4, 6.8, 1.3, "4. Save per-query results (CSV/JSON) → figures → report\n"
        "(bash run_all.sh reproduces every number)", fc="#f3f2ee")
    save(fig, "fig3_flowchart.png")


def logic_model():
    fig, ax = canvas(6.8, 4.4, f"Logic model of implications — {NAME}")
    cols = [("Inputs", ["KazQAD\nKazakh corpus\n& questions", "Open-source\nIR libraries\n& MCP SDK"]),
            ("Activities", ["Compare 5\nretrievers", "Simulate\nRAG poisoning", "Wrap search\nas MCP tool"]),
            ("Outputs", ["Prefix-5 BM25\nbest (nDCG@10\n= 0.473)", "Exposure\n69–100 %;\nregex misses\nparaphrases",
                         "+3 ms per\nMCP call"]),
            ("Outcomes", ["Morphology-\naware retrieval\nas default", "Layered\ndefences\nbeyond regex",
                          "MCP as the\nintegration\nlayer"]),
            ("Impact", ["Trustworthy\nKazakh-language\nagentic platform", "Next study:\nLLM in the loop,\nreal users"])]
    xs = [0.15, 2.15, 4.15, 6.15, 8.15]
    for (title, items), x in zip(cols, xs):
        ax.text(x + 0.9, 9.6, title, ha="center", fontsize=9, fontweight="bold", color=INK2)
        n = len(items)
        h = 7.6 / n - 0.35
        for j, t in enumerate(items):
            y = 9.0 - (j + 1) * (7.6 / n)
            box(ax, x, y + 0.17, 1.7, h, t, fc=["#f3f2ee", "#eef4fc", "#eaf7f1", "#fdf0ea", "#fdf6e3"][xs.index(x)],
                size=7)
        if x < 8:
            arrow(ax, (x + 1.7, 5.2), (x + 2.0, 5.2))
    save(fig, "fig8_logic_model.png")


def main():
    r = json.loads((RES / "retrieval_summary.json").read_text())
    chart_ndcg(r)
    chart_recall(r)
    chart_exposure(json.loads((RES / "injection_summary.json").read_text()))
    chart_mcp(json.loads((RES / "mcp_overhead.json").read_text()))
    concept_map()
    architecture()
    flowchart()
    logic_model()


if __name__ == "__main__":
    main()
