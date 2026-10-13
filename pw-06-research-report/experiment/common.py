"""Shared loading helpers."""
import json
import pickle
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA, CACHE, RESULTS = HERE / "data", HERE / "cache", HERE / "results"
METHODS = ["BM25 (word)", "BM25 (prefix-5)", "TF-IDF (char 3-5)", "LSA (dense 256-d)", "Hybrid RRF"]


def load_corpus():
    docs = [json.loads(l) for l in open(DATA / "subcorpus.jsonl", encoding="utf-8")]
    return docs, [f"{d['title']}. {d['text']}" for d in docs]


def load_topics():
    topics = [l.split("\t") for l in (DATA / "test_topics.tsv").read_text(encoding="utf-8").splitlines()]
    qrels = {}
    for qid, _, docid, rel in (l.split("\t") for l in
                               (DATA / "test_qrels.tsv").read_text(encoding="utf-8").splitlines()):
        if rel == "1":
            qrels.setdefault(qid, set()).add(docid)
    return topics, qrels


def subject(qid):
    return "".join(c for c in qid if c.isalpha())[:3]


def build_models(texts):
    """Fit (or load from cache) the four base retrievers."""
    from retrievers import BM25, LSA, CharTfidf, prefix5, words
    CACHE.mkdir(exist_ok=True)
    path = CACHE / "models.pkl"
    if path.exists():
        return pickle.loads(path.read_bytes())
    models, build_time = {}, {}
    for name, factory in [("BM25 (word)", lambda: BM25(words)),
                          ("BM25 (prefix-5)", lambda: BM25(prefix5)),
                          ("TF-IDF (char 3-5)", CharTfidf),
                          ("LSA (dense 256-d)", LSA)]:
        t0 = time.perf_counter()
        models[name] = factory().fit(texts)
        build_time[name] = time.perf_counter() - t0
        print(f"built {name} in {build_time[name]:.1f}s", flush=True)
    path.write_bytes(pickle.dumps((models, build_time)))
    return models, build_time
