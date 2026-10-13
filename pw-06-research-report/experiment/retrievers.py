"""Retrieval methods compared in the study (all trained only on the sub-corpus).

* BM25 (word)        — Okapi BM25 over lower-cased word tokens [Robertson & Zaragoza, 2009]
* BM25 (prefix-5)    — the same, each token truncated to its first 5 characters,
                       a light stemming for agglutinative languages [Can et al., 2008]
* TF-IDF (char 3–5)  — cosine similarity over character n-grams inside word boundaries
* LSA (dense, 256 d) — truncated SVD of word TF-IDF [Deerwester et al., 1990]; a dense
                       retriever that needs no pretrained model
* Hybrid RRF         — reciprocal rank fusion of BM25 (prefix-5) and TF-IDF (char)
                       [Cormack et al., 2009], k = 60
"""
import re

import numpy as np
from scipy import sparse
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import normalize

TOKEN = re.compile(r"\w+", re.UNICODE)


def words(text):
    return TOKEN.findall(text.lower())


def prefix5(text):
    return [t[:5] for t in words(text)]


class BM25:
    def __init__(self, tokenizer, k1=0.9, b=0.4):
        self.vec = CountVectorizer(tokenizer=tokenizer, lowercase=False, token_pattern=None)
        self.k1, self.b = k1, b

    def fit(self, texts):
        tf = self.vec.fit_transform(texts).tocsr().astype(np.float32)
        n_docs = tf.shape[0]
        dl = np.asarray(tf.sum(axis=1)).ravel()
        df = np.bincount(tf.indices, minlength=tf.shape[1])
        self.idf = np.log(1 + (n_docs - df + 0.5) / (df + 0.5)).astype(np.float32)
        norm = self.k1 * (1 - self.b + self.b * dl / dl.mean())
        rows = np.repeat(np.arange(n_docs), np.diff(tf.indptr))
        data = tf.data * (self.k1 + 1) / (tf.data + norm[rows])
        self.matrix = sparse.csr_matrix((data * self.idf[tf.indices], tf.indices, tf.indptr),
                                        shape=tf.shape).T.tocsr()  # terms x docs
        return self

    def scores(self, queries):
        q = self.vec.transform(queries)
        q.data[:] = 1.0  # binary query term weights
        return (q @ self.matrix).toarray()


class CharTfidf:
    def __init__(self):
        self.vec = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True,
                                   min_df=2, dtype=np.float32)

    def fit(self, texts):
        self.matrix = self.vec.fit_transform(texts).T.tocsr()
        return self

    def scores(self, queries):
        return (self.vec.transform(queries) @ self.matrix).toarray()


class LSA:
    def __init__(self, dim=256, seed=42):
        self.vec = TfidfVectorizer(tokenizer=prefix5, lowercase=False, token_pattern=None,
                                   sublinear_tf=True, min_df=2, dtype=np.float32)
        self.svd = TruncatedSVD(n_components=dim, random_state=seed)

    def fit(self, texts):
        x = self.vec.fit_transform(texts)
        self.doc_vecs = normalize(self.svd.fit_transform(x)).astype(np.float32)
        return self

    def scores(self, queries):
        q = normalize(self.svd.transform(self.vec.transform(queries)))
        return q @ self.doc_vecs.T


def top_k(score_matrix, k):
    """Indices of the k best documents per row, sorted by descending score."""
    idx = np.argpartition(-score_matrix, k, axis=1)[:, :k]
    order = np.take_along_axis(score_matrix, idx, axis=1).argsort(axis=1)[:, ::-1]
    return np.take_along_axis(idx, order, axis=1)


def rrf(rankings, k=60, depth=100):
    """Reciprocal rank fusion of several ranked lists (one list of doc indices per run)."""
    fused = []
    for lists in zip(*rankings):
        score = {}
        for ranked in lists:
            for r, d in enumerate(ranked[:depth]):
                score[d] = score.get(d, 0.0) + 1.0 / (k + r + 1)
        fused.append([d for d, _ in sorted(score.items(), key=lambda x: -x[1])])
    return fused
