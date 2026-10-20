"""Runs the chunking experiment and writes results/summary.json and results/per_question.csv.

Usage: python3 run_experiment.py [--data data/SQuAD-explorer/dataset]
"""
import argparse
import csv
import json
import math
import subprocess
import time
from pathlib import Path

import numpy as np
from scipy import stats

from chunking import STRATEGIES, load_squad
from retrieval import BM25

HERE = Path(__file__).resolve().parent
DEPTH, BATCH = 40, 512
BUDGETS = [100, 200, 400, 800, 1600]


def ensure_data(path):
    if not Path(path, "dev-v1.1.json").exists():
        repo = HERE / "data" / "SQuAD-explorer"
        subprocess.run(["git", "clone", "--depth", "1", "https://github.com/rajpurkar/SQuAD-explorer",
                        str(repo)], check=True)
        return repo / "dataset"
    return Path(path)


def bootstrap(values, n=2000, seed=42):
    rng = np.random.default_rng(seed)
    v = np.asarray(values, dtype=float)
    means = np.array([rng.choice(v, len(v)).mean() for _ in range(n)])
    return [float(np.quantile(means, .025)), float(np.quantile(means, .975))]


def mcnemar(a, b):
    a, b = np.asarray(a, bool), np.asarray(b, bool)
    n01, n10 = int((~a & b).sum()), int((a & ~b).sum())
    if n01 + n10 == 0:
        return 1.0, n01, n10
    chi2 = (abs(n01 - n10) - 1) ** 2 / (n01 + n10)
    return float(stats.chi2.sf(chi2, 1)), n01, n10


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(HERE / "data" / "SQuAD-explorer" / "dataset"))
    args = ap.parse_args()
    articles, questions = load_squad(ensure_data(args.data))
    queries = [q for q, _, _ in questions]
    print(f"{len(articles)} articles, {len(questions)} dev questions", flush=True)

    summary = {"n_articles": len(articles), "n_questions": len(questions),
               "corpus_words": int(sum(len(a.text.split()) for a in articles)), "strategies": {}}
    ranks_all = {}
    for name, make in STRATEGIES.items():
        t0 = time.perf_counter()
        chunks = make(articles)
        model = BM25().fit([f"{articles[c.article].title}. {c.text}" for c in chunks])
        build = time.perf_counter() - t0
        by_article = {}
        for ci, c in enumerate(chunks):
            by_article.setdefault(c.article, []).append(ci)
        relevant, split = [], 0
        for _, ai, golds in questions:
            rel = {ci for ci in by_article[ai]
                   if any(chunks[ci].start <= s and e <= chunks[ci].end for s, e in golds)}
            relevant.append(rel)
            split += not rel
        t0 = time.perf_counter()
        top = np.vstack([model.search(queries[i:i + BATCH], DEPTH) for i in range(0, len(queries), BATCH)])
        latency = (time.perf_counter() - t0) / len(queries) * 1000
        ranks = []
        for row, rel in zip(top, relevant):
            r = next((i + 1 for i, ci in enumerate(row) if ci in rel), 0)
            ranks.append(r)
        ranks = np.array(ranks)
        ranks_all[name] = ranks
        sizes = np.array([c.n_words for c in chunks])
        hit = lambda k: (ranks > 0) & (ranks <= k)
        s = {"n_chunks": len(chunks), "mean_chunk_words": float(sizes.mean()),
             "index_build_s": build, "latency_ms": latency,
             "answer_split_rate": split / len(questions)}
        for k in (1, 3, 5, 10, 20):
            h = hit(k)
            s[f"hit@{k}"] = {"mean": float(h.mean()), "ci95": bootstrap(h)}
        rr = np.where((ranks > 0) & (ranks <= 10), 1 / np.maximum(ranks, 1), 0)
        s["mrr@10"] = {"mean": float(rr.mean()), "ci95": bootstrap(rr)}
        s["context_words@5"] = float(sizes.mean() * 5)
        s["budget_hit"] = {}
        for B in BUDGETS:
            k = min(DEPTH, int(B // sizes.mean()))  # chunks that fit into the word budget
            s["budget_hit"][str(B)] = {"k": k, "hit": float(hit(k).mean()) if k else None}
        summary["strategies"][name] = s
        print(f"{name:24s} chunks={len(chunks):7d} words={sizes.mean():6.1f} split={s['answer_split_rate']:.3f} "
              f"hit@1={s['hit@1']['mean']:.3f} hit@5={s['hit@5']['mean']:.3f} hit@20={s['hit@20']['mean']:.3f} "
              f"mrr={s['mrr@10']['mean']:.3f} lat={latency:.2f}ms build={build:.1f}s", flush=True)

    tests = []
    for size in (50, 100, 200, 400):
        a, b = f"Fixed-{size}", f"Fixed-{size} +25% overlap"
        p, n01, n10 = mcnemar((ranks_all[a] > 0) & (ranks_all[a] <= 5), (ranks_all[b] > 0) & (ranks_all[b] <= 5))
        tests.append({"a": a, "b": b, "metric": "hit@5", "p": p, "only_b": n01, "only_a": n10})
    for a, b in [("Paragraph", "Fixed-100"), ("Paragraph", "Fixed-200"), ("Fixed-100", "Fixed-200")]:
        p, n01, n10 = mcnemar((ranks_all[a] > 0) & (ranks_all[a] <= 5), (ranks_all[b] > 0) & (ranks_all[b] <= 5))
        tests.append({"a": a, "b": b, "metric": "hit@5", "p": p, "only_b": n01, "only_a": n10})
    m = len(tests)
    order = np.argsort([t["p"] for t in tests])
    running = 0
    for rank, i in enumerate(order):
        running = max(running, (m - rank) * tests[i]["p"])
        tests[i]["p_holm"] = min(1.0, running)
    summary["mcnemar_tests"] = tests

    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / "summary.json").write_text(json.dumps(summary, indent=1))
    with open(HERE / "results" / "per_question.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["question_id", "strategy", "rank_of_first_relevant_chunk"])
        for name, ranks in ranks_all.items():
            w.writerows((i, name, int(r)) for i, r in enumerate(ranks))
    for t in tests:
        print(t)


if __name__ == "__main__":
    main()
