"""Step 2 (RQ1). Retrieval effectiveness and efficiency on KazQAD test topics.

Outputs: results/retrieval_per_query.csv, results/retrieval_summary.json
"""
import csv
import json
import time

import numpy as np
from scipy import stats

from common import METHODS, RESULTS, build_models, load_corpus, load_topics, subject
from metrics import bootstrap_ci, holm, mrr_at_k, ndcg_at_k, recall_at_k, wilcoxon
from retrievers import rrf, top_k

DEPTH, BATCH = 100, 128


def main():
    docs, texts = load_corpus()
    docids = [d["docid"] for d in docs]
    topics, qrels = load_topics()
    topics = [t for t in topics if t[0] in qrels]
    queries = [t[1] for t in topics]
    models, build_time = build_models(texts)

    runs, latency = {}, {}
    for name, model in models.items():
        ranked, t0 = [], time.perf_counter()
        for i in range(0, len(queries), BATCH):
            ranked.extend(top_k(model.scores(queries[i:i + BATCH]), DEPTH).tolist())
        latency[name] = (time.perf_counter() - t0) / len(queries) * 1000
        runs[name] = ranked
    t0 = time.perf_counter()
    runs["Hybrid RRF"] = rrf([runs["BM25 (prefix-5)"], runs["TF-IDF (char 3-5)"]], k=60, depth=DEPTH)
    latency["Hybrid RRF"] = latency["BM25 (prefix-5)"] + latency["TF-IDF (char 3-5)"] + \
        (time.perf_counter() - t0) / len(queries) * 1000

    rows, per_method = [], {m: {"ndcg10": [], "mrr10": [], "r5": [], "r20": [], "r100": []} for m in METHODS}
    for qi, (qid, text) in enumerate(topics):
        rel = qrels[qid]
        for m in METHODS:
            ranked = [docids[d] for d in runs[m][qi]]
            vals = {"ndcg10": ndcg_at_k(ranked, rel), "mrr10": mrr_at_k(ranked, rel),
                    "r5": recall_at_k(ranked, rel, 5), "r20": recall_at_k(ranked, rel, 20),
                    "r100": recall_at_k(ranked, rel, 100)}
            for k, v in vals.items():
                per_method[m][k].append(v)
            rows.append({"qid": qid, "subject": subject(qid), "method": m, **vals})

    RESULTS.mkdir(exist_ok=True)
    with open(RESULTS / "retrieval_per_query.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    summary = {"n_topics": len(topics), "methods": {}}
    for m in METHODS:
        s = {}
        for k, v in per_method[m].items():
            lo, hi = bootstrap_ci(v)
            s[k] = {"mean": float(np.mean(v)), "ci95": [lo, hi]}
        s["latency_ms_per_query"] = latency[m]
        s["build_time_s"] = build_time.get(m)
        s["by_subject_ndcg10"] = {sub: float(np.mean([r["ndcg10"] for r in rows
                                                      if r["method"] == m and r["subject"] == sub]))
                                  for sub in sorted({subject(t[0]) for t in topics})}
        summary["methods"][m] = s

    chi2, p = stats.friedmanchisquare(*[per_method[m]["ndcg10"] for m in METHODS])
    summary["friedman_ndcg10"] = {"chi2": float(chi2), "p": float(p), "df": len(METHODS) - 1}
    pairs = [("Hybrid RRF", m) for m in METHODS if m != "Hybrid RRF"] + \
            [("BM25 (prefix-5)", "BM25 (word)"), ("TF-IDF (char 3-5)", "BM25 (word)"),
             ("TF-IDF (char 3-5)", "BM25 (prefix-5)")]
    tests = [wilcoxon(per_method[a]["ndcg10"], per_method[b]["ndcg10"]) for a, b in pairs]
    adj = holm([p for p, _ in tests])
    summary["pairwise_wilcoxon_ndcg10"] = [
        {"a": a, "b": b, "mean_diff": float(np.mean(per_method[a]["ndcg10"]) - np.mean(per_method[b]["ndcg10"])),
         "p": p, "p_holm": pa, "rank_biserial_r": r}
        for (a, b), (p, r), pa in zip(pairs, tests, adj)]
    summary["no_relevant_in_top100"] = {m: int(sum(1 for v in per_method[m]["r100"] if v == 0)) for m in METHODS}
    (RESULTS / "retrieval_summary.json").write_text(json.dumps(summary, indent=1))
    for m in METHODS:
        s = summary["methods"][m]
        print(f"{m:20s} nDCG@10={s['ndcg10']['mean']:.3f} MRR@10={s['mrr10']['mean']:.3f} "
              f"R@5={s['r5']['mean']:.3f} R@20={s['r20']['mean']:.3f} R@100={s['r100']['mean']:.3f} "
              f"lat={s['latency_ms_per_query']:.1f}ms")
    print(json.dumps(summary["friedman_ndcg10"]), json.dumps(summary["pairwise_wilcoxon_ndcg10"], indent=0))


if __name__ == "__main__":
    main()
