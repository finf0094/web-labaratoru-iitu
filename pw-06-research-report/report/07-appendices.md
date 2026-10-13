# Appendices {.unnumbered}

## Appendix A. How to reproduce the study

All code is in `pw-06-research-report/experiment/`. Requirements: Python ≥ 3.10, `pip install scipy scikit-learn matplotlib`, Git, about 1 GB of disk space.

```
cd pw-06-research-report/experiment
bash run_all.sh          # download data → retrieval experiment → figures → checks (≈ 3 min)
```

| File | Purpose |
|---------------------|-------------------------------------------------|
| `prepare_data.py` | Downloads KazQAD and builds the 100 000-passage sub-corpus |
| `retrievers.py` | The five retrieval methods (BM25, prefix-5, char n-grams, LSA, RRF) |
| `metrics.py` | nDCG, MRR, Recall, bootstrap CI, Wilcoxon, Holm correction |
| `run_retrieval.py` | Runs the experiment and saves `results/*.json`, `results/*.csv` |
| `make_figures.py` | Draws all figures |
| `test_metrics.py` | Checks the metric code against hand-calculated examples |

## Appendix B. nDCG@10 by subject

: Table B1. nDCG@10 by subject and method – Name_Surname

| Method | Biology (379) | Geography (346) | Kazakh history (659) | Literature (368) | World history (177) |
|-----------|-------|-------|-------|-------|-------|
| BM25 (word) | 0.363 | 0.328 | 0.405 | 0.345 | 0.401 |
| BM25 (prefix-5) | 0.484 | 0.422 | 0.501 | 0.448 | 0.502 |
| TF-IDF (char 3-5) | 0.370 | 0.269 | 0.336 | 0.315 | 0.343 |
| LSA (dense 256-d) | 0.021 | 0.031 | 0.047 | 0.019 | 0.029 |
| Hybrid RRF | 0.481 | 0.403 | 0.481 | 0.442 | 0.477 |

## Appendix C. Example of prefix-5 truncation

| Word in text | Meaning | After prefix-5 |
|-----------------|-----------------------|--------|
| кітап | book | кітап |
| кітаптар | books | кітап |
| кітаптарымыздан | from our books | кітап |
| Қазақстан | Kazakhstan | қазақ |
| Қазақстанның | of Kazakhstan | қазақ |

All forms of one stem become the same index term, so a question and a passage with different endings still match. The side effect is that some different words share a prefix (e.g. *қазақ* "Kazakh" and *Қазақстан*), which is acceptable for search.

## Appendix D. Ethics statement

The study involved no human participants and no personal data. KazQAD is used under the CC BY-SA 4.0 licence with attribution. Therefore no consent forms, survey instruments or interview protocols were needed for this computational study.
