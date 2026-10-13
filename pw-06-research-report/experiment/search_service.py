"""Retrieval service used both directly (in-process) and through the MCP server."""
import pickle

from common import CACHE, load_corpus
from guardrail import detect
from retrievers import BM25, prefix5, top_k


class SearchService:
    def __init__(self):
        path = CACHE / "bm25_prefix5_service.pkl"
        if path.exists():
            self.docs, self.model = pickle.loads(path.read_bytes())
        else:
            self.docs, texts = load_corpus()
            self.model = BM25(prefix5).fit(texts)
            CACHE.mkdir(exist_ok=True)
            path.write_bytes(pickle.dumps((self.docs, self.model)))

    def search(self, query: str, k: int = 5) -> list[dict]:
        scores = self.model.scores([query])
        hits = top_k(scores, k)[0]
        out = []
        for i in hits:
            d = self.docs[i]
            out.append({"docid": d["docid"], "title": d["title"], "text": d["text"][:500],
                        "score": round(float(scores[0, i]), 4),
                        "untrusted_content_flags": detect(d["text"])})
        return out
