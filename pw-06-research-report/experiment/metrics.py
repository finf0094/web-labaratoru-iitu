"""Ranking metrics and statistical tests."""
import math

import numpy as np
from scipy import stats


def ndcg_at_k(ranked, relevant, k=10):
    dcg = sum(1 / math.log2(i + 2) for i, d in enumerate(ranked[:k]) if d in relevant)
    ideal = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), k)))
    return dcg / ideal if ideal else 0.0


def mrr_at_k(ranked, relevant, k=10):
    for i, d in enumerate(ranked[:k]):
        if d in relevant:
            return 1 / (i + 1)
    return 0.0


def recall_at_k(ranked, relevant, k):
    return len(set(ranked[:k]) & relevant) / len(relevant)


def bootstrap_ci(values, n=2000, seed=42, alpha=0.05):
    rng = np.random.default_rng(seed)
    values = np.asarray(values)
    means = rng.choice(values, size=(n, len(values)), replace=True).mean(axis=1)
    return float(np.quantile(means, alpha / 2)), float(np.quantile(means, 1 - alpha / 2))


def holm(pvalues):
    """Holm–Bonferroni adjusted p-values (same order as input)."""
    m = len(pvalues)
    order = np.argsort(pvalues)
    adjusted = np.empty(m)
    running = 0.0
    for rank, i in enumerate(order):
        running = max(running, (m - rank) * pvalues[i])
        adjusted[i] = min(1.0, running)
    return adjusted.tolist()


def wilcoxon(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if np.allclose(a, b):
        return 1.0, 0.0
    res = stats.wilcoxon(a, b, zero_method="wilcox")
    # matched-pairs rank-biserial correlation as effect size
    d = a - b
    d = d[d != 0]
    ranks = stats.rankdata(np.abs(d))
    r = (ranks[d > 0].sum() - ranks[d < 0].sum()) / ranks.sum()
    return float(res.pvalue), float(r)
