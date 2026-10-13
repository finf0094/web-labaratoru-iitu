# 5. Conclusion

## 5.1 Recap

This study asked which simple retrieval method should be used in the RAG component of a Kazakh-language AI platform, how many passages should be given to the model and how fast retrieval is. On 1 929 real exam questions, BM25 with words truncated to five letters was the most accurate method (nDCG@10 = 0.473, 27 % better than plain BM25). Passing 10–20 passages captures most relevant information (71 % recall at 20). All BM25 searches took under 2 ms.

**Answers to the research questions.** *RQ1:* the most accurate method is BM25 with prefix-5 truncation; the hybrid is close at the top and better deeper in the list, while character n-grams and LSA are weaker. *RQ2:* the model should receive 10–20 passages; five passages miss almost half of the relevant information, while one hundred passages make the prompt long for a small gain. *RQ3:* lexical search is fast enough for interactive use; only the character n-gram index is noticeably slower to build.

**What this means for the AI platform.** In the platform designed in this course, the retriever is offered to the language model as a search tool. The results show that this tool can start with a very simple, transparent and cheap configuration — an inverted index with five-letter tokens — that runs on an ordinary server without a GPU and can be rebuilt in seconds when documents change. More complex components, such as neural embedding models and rerankers, can be added later and compared against this baseline using the same pipeline. This order of work — first a strong simple baseline, then measured improvements — reduces cost and risk for organisations that are only starting to use AI.

## 5.2 Contributions

*Academic:* evidence that simple prefix truncation handles Kazakh morphology very effectively and that rank fusion helps only when its components are equally strong. *Practical:* a tested default configuration for the platform's RAG retriever and an open, one-command pipeline that can be rerun on new documents.

The study also shows a way of working that is useful beyond this topic: open data, fixed settings taken from the literature, paired statistical tests and one command that reproduces every number. Other students and developers can reuse the pipeline to test retrieval on their own Kazakh or Russian documents.

**Limitations to keep in mind.** The conclusions are based on a reduced corpus of Wikipedia passages and school-exam questions, on simple methods only, and on retrieval quality rather than final answer quality. They should be confirmed on the platform's real documents before deployment.

## 5.3 Recommendations

: Table 8. Recommendations from the results – Name_Surname

| Priority | Recommendation | Based on |
|-------|---------------------------------------------------------|-----------------------|
| 1 | Use BM25 with prefix-5 truncation as the default retriever for Kazakh documents | RQ1, Tables 4–5 |
| 2 | Pass 10–20 passages to the LLM; use 50–100 only together with a reranker | RQ2, Figure 5 |
| 3 | Keep the hybrid list as the candidate pool when a reranker is added | RQ1–RQ2 |
| 4 | Do not use unsupervised LSA; test modern neural embeddings next | RQ1, Section 4.2 |
| 5 | Re-evaluate on the platform's real documents (regulations, syllabi) and measure answer quality | Section 4.5 |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

## 5.4 Executive summary panel

::: {.panel}
+---------------------------------------------------------------------------------------------------+
| **Executive summary — Retrieval for RAG in Kazakh (KazQAD, small-scale study)**                   |
|                                                                                                   |
| **Question.** Which simple search method should the AI platform use to find Kazakh passages for   |
| RAG, how many passages should the model get, and how fast is it?                                  |
|                                                                                                   |
| **Data and method.**                                                                              |
|                                                                                                   |
| - 1 929 real UNT exam questions; 100 000 Kazakh Wikipedia passages (KazQAD, open data)            |
| - 5 methods: BM25 word, BM25 prefix-5, char n-grams, LSA, hybrid RRF                              |
| - Measures: nDCG@10, MRR@10, Recall@5/20/100, time; Friedman and Wilcoxon tests                   |
|                                                                                                   |
| **Key findings.**                                                                                 |
|                                                                                                   |
| - Best: BM25 prefix-5, nDCG@10 = 0.473 (+27 % over word BM25, 0.371)                              |
| - Hybrid RRF: 0.459 at the top, but best Recall@100 (0.859)                                       |
| - LSA does not work for this task (0.032)                                                         |
| - Recall of the best method: 53 % at 5 passages, 71 % at 20, 85 % at 100                          |
| - BM25 search: under 2 ms per question                                                            |
|                                                                                                   |
| **Recommendations.**                                                                              |
|                                                                                                   |
| - Default retriever: BM25 with prefix-5 truncation                                                |
| - Give the model 10–20 passages; more only with a reranker                                        |
| - Next: neural embeddings, reranking, real university documents                                   |
|                                                                                                   |
| **Limitations.** Reduced corpus, one domain, no neural models, answers not evaluated.             |
+---------------------------------------------------------------------------------------------------+
:::

::: {.watermark}
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Summary.** The report followed one line of argument: RAG answers are only as good as the retrieved passages, so the retriever for Kazakh must be chosen by evidence. A real experiment on 1 929 exam questions showed that BM25 with five-letter truncation is the most accurate and very fast option, and that 10–20 passages give the model most of the relevant information. Fusion with a weaker method and unsupervised LSA did not help at the top of the ranking. These results give the AI platform a simple, tested default configuration. The next steps — neural embeddings, reranking and evaluation on real university documents — follow directly from the limitations of this study.
