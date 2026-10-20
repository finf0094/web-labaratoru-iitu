"""Okapi BM25 over chunks (k1 = 0.9, b = 0.4), sparse-matrix implementation."""
import re

import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer

TOKEN = re.compile(r"\w+")


def tokenize(text):
    return TOKEN.findall(text.lower())


class BM25:
    def __init__(self, k1=0.9, b=0.4):
        self.k1, self.b = k1, b
        self.vec = CountVectorizer(tokenizer=tokenize, lowercase=False, token_pattern=None)

    def fit(self, texts):
        tf = self.vec.fit_transform(texts).tocsr().astype(np.float32)
        n = tf.shape[0]
        dl = np.asarray(tf.sum(axis=1)).ravel()
        df = np.bincount(tf.indices, minlength=tf.shape[1])
        idf = np.log(1 + (n - df + 0.5) / (df + 0.5)).astype(np.float32)
        norm = self.k1 * (1 - self.b + self.b * dl / dl.mean())
        rows = np.repeat(np.arange(n), np.diff(tf.indptr))
        data = tf.data * (self.k1 + 1) / (tf.data + norm[rows]) * idf[tf.indices]
        self.matrix = sparse.csr_matrix((data, tf.indices, tf.indptr), shape=tf.shape).T.tocsr()
        return self

    def search(self, queries, k):
        q = self.vec.transform(queries)
        q.data[:] = 1.0
        scores = (q @ self.matrix).toarray()
        idx = np.argpartition(-scores, k, axis=1)[:, :k]
        order = np.take_along_axis(scores, idx, axis=1).argsort(axis=1)[:, ::-1]
        return np.take_along_axis(idx, order, axis=1)
