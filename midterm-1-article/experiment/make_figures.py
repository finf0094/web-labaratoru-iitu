"""Draws the article's charts from results/summary.json into figures/*.png.

Light theme, one axis per panel, direct labels instead of legends where possible.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
RES = json.loads((HERE / "results" / "summary.json").read_text())
S = RES["strategies"]
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)

BLUE, ORANGE, GREEN, YELLOW, PINK = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"
SIZES = [50, 100, 200, 400]

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": MUTED,
    "axes.labelcolor": INK, "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.spines.top": False, "axes.spines.right": False, "axes.grid": True,
    "grid.color": GRID, "grid.linewidth": 0.8, "axes.axisbelow": True,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.dpi": 200,
})


def fixed(size, ov):
    return S[f"Fixed-{size}" + (" +25% overlap" if ov else "")]


def dodge(ys, gap):
    """Label positions: the same order as ys, but at least `gap` apart vertically."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    pos = list(ys)
    for a, b in zip(order, order[1:]):
        pos[b] = max(pos[b], pos[a] + gap)
    return pos


def end_labels(ax, ends, gap):
    """Direct labels at the right end of each line: ends = [(x, y, label, color)]."""
    for (x, y, label, color), ly in zip(ends, dodge([e[1] for e in ends], gap)):
        ax.annotate(label, (x, ly), xytext=(8, 0), textcoords="offset points",
                    color=color, fontweight="bold", va="center", annotation_clip=False)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, facecolor="white")
    plt.close(fig)
    print("saved", OUT / name)


# Hit@5 against chunk size, with and without overlap.
fig, ax = plt.subplots(figsize=(6.4, 3.8))
for ov, color, label in ((False, MUTED, "no overlap"), (True, BLUE, "+25% overlap")):
    xs = [fixed(s, ov)["mean_chunk_words"] for s in SIZES]
    ys = [fixed(s, ov)["hit@5"]["mean"] for s in SIZES]
    lo = [y - fixed(s, ov)["hit@5"]["ci95"][0] for s, y in zip(SIZES, ys)]
    hi = [fixed(s, ov)["hit@5"]["ci95"][1] - y for s, y in zip(SIZES, ys)]
    ax.errorbar(xs, ys, yerr=[lo, hi], color=color, marker="o", lw=2, ms=5, capsize=3,
                ls="-" if ov else "--")
    ax.annotate(label, (xs[0], ys[0]), xytext=(8, -14 if not ov else -18),
                textcoords="offset points", color=color, fontweight="bold")
p = S["Paragraph"]
ax.scatter([p["mean_chunk_words"]], [p["hit@5"]["mean"]], color=GREEN, marker="D", s=50, zorder=5)
ax.annotate("Paragraph", (p["mean_chunk_words"], p["hit@5"]["mean"]), xytext=(-8, 10),
            textcoords="offset points", color=GREEN, fontweight="bold", ha="right")
ax.set_xscale("log")
ax.set_xticks([50, 100, 200, 400], ["50", "100", "200", "400"])
ax.minorticks_off()
ax.set_xlabel("Mean chunk size, words (log scale)")
ax.set_ylabel("Hit@5")
ax.set_ylim(0.70, 0.90)
save(fig, "hit5_vs_size.png")

# Hit under a fixed context budget (k = budget / chunk size).
fig, ax = plt.subplots(figsize=(6.4, 4.0))
ends = []
series = [("Fixed-50 +25% overlap", "F50+ov", BLUE), ("Fixed-100 +25% overlap", "F100+ov", ORANGE),
          ("Fixed-200 +25% overlap", "F200+ov", YELLOW), ("Fixed-400 +25% overlap", "F400+ov", PINK),
          ("Paragraph", "Paragraph", GREEN)]
for key, label, color in series:
    pts = [(int(b), v["hit"]) for b, v in S[key]["budget_hit"].items() if v["hit"] is not None]
    xs, ys = zip(*pts)
    ax.plot(xs, ys, marker="o", color=color, lw=2, ms=4)
    ends.append((xs[-1], ys[-1], label, color))
end_labels(ax, ends, 0.011)
ax.set_xscale("log")
ax.set_xticks([100, 200, 400, 800, 1600], ["100", "200", "400", "800", "1600"])
ax.minorticks_off()
ax.set_xlim(85, 3400)
ax.set_ylim(0.65, 0.96)
ax.set_xlabel("Context budget, words given to the LLM (log scale)")
ax.set_ylabel("Hit within budget")
save(fig, "context_budget.png")

# Answer splitting and the gain from overlap.
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.4))
labels = [str(s) for s in SIZES]
split = [100 * fixed(s, False)["answer_split_rate"] for s in SIZES]
gain = [100 * (fixed(s, True)["hit@5"]["mean"] - fixed(s, False)["hit@5"]["mean"]) for s in SIZES]
for ax, vals, color, title, fmt in ((a1, split, MUTED, "Answers split by a boundary, %", "{:.1f}"),
                                    (a2, gain, BLUE, "Hit@5 gain from overlap, p.p.", "+{:.1f}")):
    bars = ax.bar(labels, vals, color=color, width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v, fmt.format(v), ha="center", va="bottom", color=INK)
    ax.set_title(title, fontsize=10, color=INK, loc="left")
    ax.set_xlabel("Fixed chunk size, words")
    ax.grid(axis="x", visible=False)
    ax.set_ylim(0, max(vals) * 1.2)
save(fig, "split_and_gain.png")

# Hit@k curves for three representative strategies.
fig, ax = plt.subplots(figsize=(6.4, 3.8))
ks = [1, 3, 5, 10, 20]
ends = []
for key, label, color, ls in (("Fixed-100", "Fixed-100", ORANGE, "--"),
                              ("Fixed-100 +25% overlap", "Fixed-100 +ov", ORANGE, "-"),
                              ("Fixed-400", "Fixed-400", PINK, "--"), ("Paragraph", "Paragraph", GREEN, "-")):
    ys = [S[key][f"hit@{k}"]["mean"] for k in ks]
    ax.plot(ks, ys, marker="o", color=color, lw=2, ms=4, ls=ls)
    ends.append((ks[-1], ys[-1], label, color))
end_labels(ax, ends, 0.014)
ax.set_xscale("log")
ax.set_xticks(ks, [str(k) for k in ks])
ax.minorticks_off()
ax.set_xlim(0.9, 45)
ax.set_ylim(0.60, 0.97)
ax.set_xlabel("k, number of retrieved chunks (log scale)")
ax.set_ylabel("Hit@k")
save(fig, "hit_at_k.png")
