# 4. Discussion

## 4.1 Alignment with the hypotheses

: Table 9. Hypotheses versus observed results – Name_Surname

| Hypothesis | Expected | Observed | Verdict |
|------------|------------------------|------------------------------|-----------|
| H1a | Hybrid RRF has the highest nDCG@10 | Prefix-5 BM25 is highest (0.473); RRF is 0.014 lower (*r* = −0.12) but has the highest Recall@100 | Not supported |
| H1b | Sub-word representations beat word-level BM25 | Prefix-5: +0.102 (supported); character n-grams: −0.044 (not supported) | Partly supported |
| H2a | Lexical retrievers expose the agent in > 50 % of attacks | 96.5–100 % (full copy), 69–95 % (partial copy) | Supported |
| H2b | Guardrail TPR ≥ 90 % with FPR < 1 % | 100 % explicit, 0 % paraphrased (60 % overall); FPR 0.354 % | Not supported overall |
| H3 | MCP overhead < 10 ms per call | Median 3.0 ms, p95 5.0 ms | Supported |

## 4.2 Interpretation of the retrieval results (RQ1)

The clearest finding is that **simple morphology-aware truncation is the most effective option for Kazakh** in this setting. Truncating words to five characters maps inflected forms of the same stem — for example, case and possessive forms of a noun — onto one index term, so a question and a passage that use different suffixes still match. This mirrors the result for Turkish, another agglutinative Turkic language, where prefix truncation was as effective as elaborate stemmers [@can2008]. The 27 % relative improvement in nDCG@10 over word-level BM25 is large compared with typical differences between ranking functions, which suggests that vocabulary mismatch caused by inflection is the main obstacle for lexical retrieval in Kazakh.

Character n-grams were expected to capture the same morphology more flexibly, but they performed worse than both BM25 variants at the top of the ranking while achieving high Recall@100 (0.825). A plausible explanation is that cosine TF-IDF over many overlapping n-grams lacks BM25's term-frequency saturation and length normalisation, so it finds the right *neighbourhood* of passages but orders them less precisely. This also explains the result for the hybrid run: reciprocal rank fusion works best when it combines runs of comparable quality that make different errors [@cormack2009]. Here the n-gram run was weaker at the top ranks, so fusion slightly diluted the precision of prefix-5 BM25 while still adding a few relevant passages deeper in the list — hence the highest Recall@100. For an agent that passes only five to ten passages to the model, prefix-5 BM25 is preferable; for a two-stage pipeline with a reranker, the hybrid list is a better candidate pool.

LSA performed very poorly. Unsupervised 256-dimensional vectors merge many topics into the same dimensions and cannot distinguish the precise facts asked in exam questions; the original LSA work targeted small collections and synonymy rather than factoid retrieval over 100 000 passages [@deerwester1990]. The result should not be generalised to modern neural dense retrievers, which are trained on question–passage pairs and can outperform BM25 [@karpukhin2020]; such models were outside the scope of this small-scale study.

Compared with the literature, the absolute values are higher than KazQAD's published best baseline (nDCG@10 = 0.389) [@yeshpanov2024kazqad], but the comparison is not direct: the sub-corpus contains about eight times fewer passages, which makes the task easier. The *ranking* of methods, rather than the absolute level, is the transferable result.

## 4.3 Interpretation of the security results (RQ2)

The poisoning experiment shows that **a retriever that is good at finding relevant text is equally good at finding attacker text that imitates the question**. Lexical methods reward word overlap, and an attacker who copies the likely question into a page obtains near-perfect overlap; with full copying, the poisoned passage was ranked first in up to 99.5 % of attacks and also pushed relevant passages down (nDCG@10 of prefix-5 BM25 fell from 0.499 to 0.355 for the attacked questions). The apparent robustness of LSA is not a virtue: it rarely surfaced poisoned passages because it rarely surfaced any matching passage. These findings converge with Greshake et al. [@greshake2023]: retrieved content must be treated as untrusted input, because the retrieval step does not filter it.

The guardrail illustrates both the value and the limit of pattern filters. It caught every explicit "ignore previous instructions" style payload in English, Russian and Kazakh, which shows that multilingual patterns are feasible and cheap. However, it missed every paraphrased payload that expressed the same malicious intent without trigger words, which supports the OWASP guidance that prompt injection cannot be solved by input filtering alone [@owasp2025llm]. The false alarms were also instructive: almost all came from e-mail addresses in Wikipedia pages about French and Italian municipalities, which contain official contact details. A rule that is a strong signal in one context (an instruction to send data to an address) is a normal fact in another, so the guardrail's flags should inform the agent and its policies rather than silently delete content.

## 4.4 Interpretation of the integration results (RQ3)

Exposing retrieval through MCP added about 3 ms per call — the cost of serialising the request and the 10 KB response as JSON-RPC messages and passing them through a pipe. This is small compared with the time an LLM needs to generate a response, so in an agent loop the protocol is not a bottleneck. The one-off start-up cost (2.5 s) matters only for short-lived processes and can be avoided by keeping the server running. The finding supports the architectural choice made in the research plan: MCP can be the single integration layer for tools without a measurable penalty for users. The response size, rather than latency, is the more important cost, because every retrieved character becomes input tokens for the model; truncating passages and returning flags alongside them, as done here, keeps the payload controlled.

## 4.5 Unexpected results

Three results contradicted expectations: the hybrid run did not outperform its best component; character n-grams were worse than word-level BM25; and LSA was almost unusable. Methodological explanations (fusion of unequal runs, missing saturation and length normalisation in TF-IDF, too few latent dimensions) and contextual explanations (short factoid questions with distinctive named entities, which favour exact stem matching) are plausible. Statistically, the very large sample makes even small differences significant — the hybrid-versus-prefix-5 difference is significant but its effect size is small (*r* = −0.12), so the two methods are practically close at the top of the ranking.

## 4.6 Limitations

* **Internal validity.** Parameters were taken from the literature without tuning; tuned parameters might change the ranking of close methods (hybrid vs prefix-5).
* **External validity.** One dataset and one domain (school-exam questions over Wikipedia); results may differ for university regulations or business documents, and for Russian or mixed-language corpora.
* **Sample representativeness.** A 100 000-passage sub-corpus was used instead of 825 309 passages, which raises absolute scores; KazQAD judgements may also favour lexical methods if candidate passages were found with lexical search during annotation.
* **Measurement.** RQ2 measured exposure, not attack success: whether an LLM would follow the injected instruction was not tested. Attack payloads and guardrail patterns were written by the same researcher, and paraphrased payloads were deliberately free of trigger words.
* **Scope.** No pretrained neural embedding models and no LLM were used, so the study does not show how modern dense retrievers or the full agent loop would behave.
* **Bias and power.** Power was very high for RQ1 (1 929 paired questions); RQ2 used 40 cases per payload variant, so detection rates per variant have wide confidence intervals; latency was measured on one machine with stdio transport, not over the network.

## 4.7 Future work

Next steps are: (1) add multilingual neural embedding models and a cross-encoder reranker on top of the hybrid candidate pool; (2) repeat the study on the full corpus and on Russian and English university documents; (3) place an LLM in the loop to measure attack *success*, and compare defences such as isolation of untrusted content, least-privilege tools and human approval of actions; (4) replace the pattern guardrail with a learned multilingual injection classifier and evaluate it on independently written attacks; (5) measure MCP overhead over the streamable HTTP transport in a networked deployment.

![Figure 8. Logic model of implications – Name_Surname](../experiment/figures/fig8_logic_model.png){width=95%}

**Summary.** The results partly confirm and partly contradict the hypotheses. Morphology-aware prefix truncation is the strongest retriever for Kazakh questions, in line with evidence for Turkish, while fusion with a weaker character n-gram run and unsupervised LSA do not help at the top of the ranking. Lexical retrievers surface attacker passages that imitate the question almost always, so retrieval offers no protection and retrieved content must be treated as untrusted. Pattern-based guardrails catch explicit injections in three languages but not paraphrases, and their false alarms depend on context. MCP integration adds only a few milliseconds per call, supporting it as the platform's integration layer. The main constraints are the single dataset, the reduced corpus, the absence of neural retrievers and of an LLM in the loop, and the researcher-written attacks.
