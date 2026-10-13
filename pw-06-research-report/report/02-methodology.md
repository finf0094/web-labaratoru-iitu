# 2. Methodology

## 2.1 Research design

A **quantitative, computational experiment** was chosen. All retrieval methods answered the same set of questions (a within-subjects design where questions play the role of subjects), so the methods can be compared with paired statistical tests. The design fits the research questions because accuracy, recall and speed are numbers that can be measured directly and objectively. No people were involved, because the study evaluates a software component, not a user experience. In the terms of the course lecture on research methodology, the study is applied, empirical and quantitative and uses the *experimental* approach: one factor — the retrieval method — is changed while everything else stays the same.

: Table 2. Design of the study – Name_Surname

| RQ | Independent variable | Dependent variables | Instrument | Analysis |
|-----|--------------------|---------------------|----------------|---------------------|
| RQ1 | Retrieval method (5 levels) | nDCG@10, MRR@10 | KazQAD questions and judgements | Mean, 95 % bootstrap CI, Friedman test, Wilcoxon + Holm, effect size *r* |
| RQ2 | Number of passages *k* (5, 20, 100) | Recall@k | Same | Mean recall by *k* |
| RQ3 | Retrieval method | Search time per question, index build time | Timer in the script | Mean time |

## 2.2 Sample

**Questions.** All 1 929 questions of the KazQAD test set were used [@yeshpanov2024kazqad]. They are real questions of the Unified National Testing (UNT) exam in five subjects: Kazakh history (659), biology (379), literature (368), geography (346) and world history (177). Every question has at least one passage marked relevant by annotators (2 718 relevant judgements, 1.41 per question). Using the whole test set avoids sampling error and gives high statistical power.

**Passages.** The full corpus has 825 309 passages. To keep the project small and runnable on a normal computer, a sub-corpus of **100 000 passages** was built: all 2 660 passages judged for the test questions plus 97 340 randomly selected other passages (random seed 42; passages shorter than 40 characters were skipped). The average passage has 39 words and the average question 7 words.

**Ethics.** No people and no personal data were involved. KazQAD is open data (licence CC BY-SA 4.0) and is cited in this report.

## 2.3 Materials and instruments

* **Retrieval methods** (Python, scikit-learn, SciPy [@pedregosa2011]):
  1. *BM25 (word)* — classic BM25 over lower-cased words (k1 = 0.9, b = 0.4) [@robertson2009];
  2. *BM25 (prefix-5)* — the same, but every word is cut to its first five letters, so different forms of one word match [@can2008];
  3. *TF-IDF (char 3–5)* — similarity over 3–5-letter pieces of words;
  4. *LSA (dense, 256 dimensions)* — passages compressed into 256-number vectors [@deerwester1990];
  5. *Hybrid RRF* — the rankings of methods 2 and 3 merged with reciprocal rank fusion (k = 60) [@cormack2009].
  Settings were taken from the cited sources and were not tuned on the test questions.
* **Quality measures.** *nDCG@10* — how good the first 10 results are, giving more credit to relevant passages at the top (0 = nothing useful, 1 = perfect); *MRR@10* — how high the first relevant passage is; *Recall@k* — the share of relevant passages found in the top *k*.
* **Computer.** 4 CPU cores, 15 GB RAM, Linux, Python 3.13.

**Reliability and validity.** The code is deterministic and uses fixed random seeds, so rerunning it gives the same quality numbers; times may vary slightly with computer load. Validity rests on KazQAD's manual relevance judgements. The metric code was checked against hand-calculated examples (`test_metrics.py`).

## 2.4 Procedures

The procedure (Figure 3) has six steps, all run by one command `bash run_all.sh` in about three minutes:

1. Download KazQAD from GitHub (`prepare_data.py`).
2. Build the 100 000-passage sub-corpus and compute dataset statistics.
3. Build the five retrievers.
4. For every question, retrieve the top-100 passages with each method and record the time (`run_retrieval.py`).
5. Compute the quality measures and the statistical tests.
6. Save results as CSV/JSON files and draw the figures (`make_figures.py`).

No separate pilot was needed because no questionnaire or interview was used and no parameter was tuned.

![Figure 3. Flowchart of research procedures – Name_Surname](../experiment/figures/fig3_flowchart.png){width=80%}

## 2.5 Data analysis

For each method, averages over the 1 929 questions were calculated with 95 % bootstrap confidence intervals (2 000 resamples). The Friedman test checked whether the five methods differ overall in nDCG@10. Seven pairwise comparisons used the Wilcoxon signed-rank test, which suits paired data that are not normally distributed, with Holm correction for multiple comparisons; the rank-biserial correlation *r* shows the size of each difference (about 0.1 small, 0.3 medium, 0.5 large). Recall was compared across *k* = 5, 20 and 100, and speed as the average time per question.

**Summary.** The study is a quantitative computational experiment in which five retrieval methods answer the same 1 929 Kazakh exam questions. A 100 000-passage sub-corpus keeps the project small while including every judged passage. The methods use standard settings from the literature, and quality is measured with nDCG@10, MRR@10 and Recall@k. Six scripted steps produce all results with one command, and fixed seeds make them repeatable. Bootstrap intervals, the Friedman test and Holm-corrected Wilcoxon tests with effect sizes are used for analysis. Data and code are open, so the study can be replicated exactly.
