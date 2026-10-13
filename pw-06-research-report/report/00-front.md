---
title: "Practical Work 6. Writing a Research Report"
subtitle: "Retrieval for Retrieval-Augmented Generation (RAG) in Kazakh: A Small-Scale Comparison of Simple Search Methods on KazQAD"
author: "Student: Name_Surname  ·  Group: GroupNumber  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-US
abstract: |
  Retrieval-augmented generation (RAG) lets a large language model answer from an organisation's own documents: a retriever finds relevant passages and the model writes the answer from them. The quality of the answer therefore depends on the retriever. This small-scale project compares five simple retrieval methods for Kazakh — BM25 over words, BM25 over words truncated to five characters (prefix-5), TF-IDF over character n-grams, latent semantic analysis (LSA) and hybrid reciprocal rank fusion (RRF) — on the open KazQAD dataset (1 929 exam questions, 100 000 passages of Kazakh Wikipedia). Prefix-5 BM25 achieved the best nDCG@10 (0.473 vs 0.371 for word-level BM25), hybrid RRF the best Recall@100 (0.859), and LSA performed poorly (0.032). Passing 20 instead of 5 passages to the model raised recall from 0.53 to 0.71 for the best method. BM25 needed less than 2 ms per question. The results suggest prefix-5 BM25 with 5–20 passages as a simple, fast default retriever for a Kazakh-language AI platform. **Keywords:** retrieval-augmented generation, RAG, Kazakh language, BM25, information retrieval, KazQAD.
---
