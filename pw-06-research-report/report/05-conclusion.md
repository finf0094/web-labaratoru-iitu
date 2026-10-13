# 5. Conclusion

## 5.1 Recap of the main findings

This small-scale study asked how the retrieval tool of a Kazakh-language agentic AI platform should be built so that it is effective, does not silently expose the agent to attacks and can be integrated through the Model Context Protocol. For **RQ1**, BM25 with prefix-5 truncation was the most effective retriever for 1 929 Kazakh exam questions (nDCG@10 = 0.473), clearly ahead of word-level BM25 (0.371); hybrid fusion with character n-grams gave the best recall at depth 100 but not the best top-ranked results, and unsupervised LSA was not usable. For **RQ2**, lexical retrievers placed attacker passages that imitate the question in the top-5 results in 96.5–100 % of attacks, and a multilingual pattern guardrail caught all explicit but none of the paraphrased injections. For **RQ3**, MCP added a median of 3.0 ms per call.

## 5.2 Contributions

*Academic:* controlled, reproducible evidence for Kazakh — an under-studied agglutinative language — that light stemming by truncation brings large gains, that rank fusion helps only when its components are comparably strong, and that retrieval effectiveness and exposure to poisoning are two sides of the same mechanism. *Practical:* an evidence-based default configuration for the platform's retrieval tool, a realistic picture of what pattern guardrails can achieve, a measured cost of MCP integration, and an open pipeline (data preparation, retrievers, attack simulation, MCP server, statistics) that other teams can rerun.

## 5.3 Recommendations

: Table 10. Recommendations derived from the results – Name_Surname

| Priority | Recommendation | Evidence |
|-------|---------------------------------------------------------|-----------------------|
| 1 | Use prefix-5 BM25 as the default first-stage retriever for Kazakh documents; keep the hybrid list as a candidate pool for a future reranker | RQ1: Tables 4–5 |
| 2 | Treat every retrieved passage and tool output as untrusted: mark it as data, attach guardrail flags, and never let it change the agent's instructions | RQ2: Table 6 |
| 3 | Do not rely on pattern filters alone; combine them with least-privilege tools, human approval of irreversible actions and learned detectors | RQ2: Table 7 |
| 4 | Use MCP as the single tool-integration layer; keep servers running and limit response size rather than worrying about protocol latency | RQ3: Table 8 |
| 5 | Next research: neural multilingual retrievers, the full corpus, Russian/English documents and an LLM in the loop to measure attack success | Section 4.7 |

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

## 5.4 Executive summary panel

::: {.panel}
+---------------------------------------------------------------------------------------------------+
| **Executive summary — Kazakh-language agentic AI platform: retrieval, poisoning, MCP**            |
|                                                                                                   |
| **Question.** How should the retrieval tool of an agentic AI platform for Kazakh be built so      |
| that it is effective, safe and cheap to integrate?                                                |
|                                                                                                   |
| **Data and method.**                                                                              |
|                                                                                                   |
| - KazQAD: 1 929 real UNT exam questions; 100 000 Kazakh Wikipedia passages (reproducible, seed 42)|
| - Five retrievers, 200 simulated attacks × 2 strategies, a multilingual guardrail, an MCP server  |
| - Paired statistics: bootstrap CIs, Friedman, Wilcoxon with Holm correction                       |
|                                                                                                   |
| **Key findings.**                                                                                 |
|                                                                                                   |
| - Prefix-5 BM25 is best: nDCG@10 = 0.473 vs 0.371 for word-level BM25 (+27 %)                     |
| - Hybrid RRF: best Recall@100 (0.859) but not better at the top; LSA unusable (0.032)             |
| - Poisoned passages reach the top-5 in 96.5–100 % of attacks (69–95 % with partial copying)       |
| - Guardrail: 100 % of explicit injections (EN/RU/KZ), 0 % of paraphrased; 0.35 % false alarms     |
| - MCP adds a median of 3.0 ms per tool call (3.8 → 6.8 ms)                                        |
|                                                                                                   |
| **Recommendations.**                                                                              |
|                                                                                                   |
| - Default to prefix-5 BM25; keep the hybrid pool for reranking                                    |
| - Treat retrieved text as untrusted; layer defences beyond pattern filters                        |
| - Adopt MCP as the integration layer; control response size                                       |
|                                                                                                   |
| **Limitations.** One dataset, reduced corpus, no neural retrievers, no LLM in the loop.           |
+---------------------------------------------------------------------------------------------------+
:::

::: {.watermark}
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

**Summary.** The report followed one line of argument: an agentic platform for Kazakh depends on its retrieval tool, so that tool must be chosen by evidence on effectiveness, security exposure and integration cost. The experiment showed that morphology-aware prefix truncation gives the best Kazakh retrieval, that the same lexical matching makes the agent highly exposed to planted content, and that MCP integration is inexpensive. Pattern guardrails help against explicit attacks but are insufficient alone. The contributions are a reproducible evaluation pipeline and a concrete default configuration for the platform. The recommendations follow directly from the results and point to neural retrieval, larger and more diverse corpora and LLM-in-the-loop security testing as the next steps. Together, these findings close the small-scale study and provide the empirical basis for the full research plan of the thesis.
