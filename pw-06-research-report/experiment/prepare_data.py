"""Step 1. Download KazQAD (if needed) and build the evaluation sub-corpus.

KazQAD (Yeshpanov et al., 2024, CC BY-SA 4.0) is cloned from GitHub into data/KazQAD.
The sub-corpus contains every passage judged for the test topics (relevant and
non-relevant) plus randomly sampled distractor passages from the full corpus,
100 000 passages in total. Output: data/subcorpus.jsonl, data/test_topics.tsv,
data/test_qrels.tsv, results/dataset_stats.json.

Usage: python3 prepare_data.py [--size 100000] [--seed 42]
"""
import argparse
import gzip
import json
import random
import subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
REPO = DATA / "KazQAD"
IR = REPO / "data" / "information-retrieval"


def ensure_repo():
    if not IR.exists():
        DATA.mkdir(exist_ok=True)
        subprocess.run(["git", "clone", "--depth", "1", "https://github.com/IS2AI/KazQAD", str(REPO)],
                       check=True)


def read_corpus():
    for part in sorted((IR / "corpus").glob("*.jsonl.gz")):
        with gzip.open(part, "rt", encoding="utf-8") as f:
            for line in f:
                yield json.loads(line)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=100_000)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    ensure_repo()

    topics = [l.rstrip("\n").split("\t") for l in
              (IR / "topics" / "kazqad-topics-v1.0-kk-test.tsv").read_text(encoding="utf-8").splitlines()]
    qrels = [l.split("\t") for l in
             (IR / "qrels" / "kazqad-qrels-v1.0-test.tsv").read_text(encoding="utf-8").splitlines()]
    judged = {d for _, _, d, _ in qrels}

    # Reservoir sampling of distractors in one pass over the 800k-passage corpus.
    rng = random.Random(args.seed)
    kept, reservoir, seen, total = {}, [], 0, 0
    n_distractors = args.size - len(judged)
    for doc in read_corpus():
        total += 1
        text = doc["text"].strip()
        if doc["docid"] in judged:
            kept[doc["docid"]] = doc
            continue
        if len(text) < 40:  # skip empty/markup-only passages as distractors
            continue
        seen += 1
        if len(reservoir) < n_distractors:
            reservoir.append(doc)
        else:
            j = rng.randrange(seen)
            if j < n_distractors:
                reservoir[j] = doc
    docs = list(kept.values()) + reservoir
    rng.shuffle(docs)

    with open(DATA / "subcorpus.jsonl", "w", encoding="utf-8") as f:
        for d in docs:
            f.write(json.dumps({"docid": d["docid"], "title": d["title"], "text": d["text"]},
                               ensure_ascii=False) + "\n")
    (DATA / "test_topics.tsv").write_text("\n".join("\t".join(t) for t in topics), encoding="utf-8")
    (DATA / "test_qrels.tsv").write_text("\n".join("\t".join(q) for q in qrels), encoding="utf-8")

    rel = [q for q in qrels if q[3] == "1"]
    per_topic = Counter(q[0] for q in rel)
    subjects = Counter("".join(c for c in t[0] if c.isalpha())[:3] for t in topics)
    stats = {
        "full_corpus_passages": total,
        "subcorpus_passages": len(docs),
        "judged_passages_in_subcorpus": len(kept),
        "judged_passages_missing": len(judged - set(kept)),
        "distractor_passages": len(reservoir),
        "test_topics": len(topics),
        "relevant_judgements": len(rel),
        "nonrelevant_judgements": len(qrels) - len(rel),
        "mean_relevant_per_topic": round(len(rel) / len(per_topic), 3),
        "topics_by_subject": dict(sorted(subjects.items())),
        "mean_question_length_words": round(sum(len(t[1].split()) for t in topics) / len(topics), 2),
        "mean_passage_length_words": round(sum(len(d["text"].split()) for d in docs) / len(docs), 2),
        "seed": args.seed,
    }
    (HERE / "results").mkdir(exist_ok=True)
    (HERE / "results" / "dataset_stats.json").write_text(json.dumps(stats, indent=1, ensure_ascii=False))
    print(json.dumps(stats, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
