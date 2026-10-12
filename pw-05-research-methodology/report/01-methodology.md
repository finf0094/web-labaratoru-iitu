---
title: "Practical Work 5. Research Plan and Methodology"
subtitle: "Topic: Information System for Monitoring Students' Academic Performance with Machine-Learning-Based Early Warning of At-Risk Students"
author: "Student: ____________________  ·  Group: ________  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-GB
---

# Introduction

This work turns the research plan (PW2) and the literature review (PW3, PW4) into a detailed, replicable methodology. The study investigates whether an explainable machine-learning early-warning system (working name **EduRadar**), integrated with the data a Kazakhstani university already stores in its automated information system (AIS, e.g. Platonus) and learning management system (LMS, e.g. Moodle), can identify students at risk of failing a course early enough for advisors to intervene.

# 1. Research questions and hypotheses

The questions follow directly from the gaps identified in the literature review: predictive models are rarely validated outside the institution where they were built [@gasevic2016; @namoun2021], explanations and teacher use of predictions are under-studied [@herodotou2019a; @matcha2020], fairness is seldom checked [@baker2022], and there is almost no evidence from Central Asian universities with their admission-rating/FX grading model.

| Code | Research question | Hypothesis (testable) | Measure |
|---|---|---|---|
| RQ1 | Which AIS/LMS features are the strongest early predictors of course failure? | H1: grades + attendance + LMS activity give ROC-AUC ≥ 0.80 at week 7 and significantly higher AUC than grades only. | ROC-AUC, DeLong test; mean \|SHAP\| per feature |
| RQ2 | Which model gives the best recall–precision trade-off and how does quality evolve from week 2 to 8? | H2: gradient boosting has higher recall at precision ≥ 0.60 than logistic regression. | Recall, precision, F1, PR-AUC per week; Wilcoxon test over folds |
| RQ3 | Do SHAP-based explanations increase advisors' perceived usefulness and trust? | H3: TAM usefulness and trust scores are higher for the explained dashboard; SUS ≥ 68. | TAM / trust items (7-point), SUS (0–100) |
| RQ4 | Does using the system reduce failures? | H4: the share of FX/F grades in pilot groups is lower than in control groups. | FX/F rate, χ², logistic regression with prior GPA |

All questions are specific (one target population and one outcome each), measurable (numeric indicators) and aligned with the overall objective of the thesis.

# 2. Research design

**Overall framework: Design Science Research (DSR)** — the artefact (the early-warning information system) is designed, built and evaluated in iterations — combined with a **mixed-methods sequential design** [@creswell2018]:

1. **Exploratory qualitative phase** — interviews and focus groups define requirements, the operational definition of "at risk" and acceptable interventions.
2. **Quantitative modelling phase** — secondary analysis of historical institutional records and the open OULAD dataset [@kuzilek2017]; computational experiments compare models (RQ1, RQ2).
3. **Evaluation phase (mixed)** — within-subject experiment with advisors (explained vs. plain dashboard), SUS/TAM survey, second focus group (RQ3), and a one-semester quasi-experimental pilot (RQ4).
4. **Integration** — triangulation: statistical results are interpreted together with qualitative themes in a joint display.

**Justification.** Prediction quality (RQ1–RQ2) and impact (RQ4) are numerical questions and require quantitative methods; acceptance and trust (RQ3) also depend on context, workload and beliefs that only qualitative data can reveal. A mixed design therefore increases **validity** (triangulation of sources and methods), **reliability** (standardised instruments, fixed protocols, reproducible code) and **feasibility** (the modelling phase can start on open data while institutional access is being approved).

# 3. Target population and sample

| Strand | Population | Sampling strategy | Expected sample size and justification |
|---|---|---|---|
| Historical records (modelling) | All student-course enrolments of bachelor's programmes in 2021/22–2025/26 | Census (all records), stratified temporal split: earlier years → training, last year → test | Several tens of thousands of enrolments (exact number after data export); OULAD: 32 593 students, 22 module presentations [@kuzilek2017] |
| Interviews | Advisors/curators, teachers of 1st-year courses, academic office staff | Purposive maximum-variation sampling (different programmes, experience), snowball for academic office | 12–15 interviews; data saturation in comparable studies is typically reached by about 12 interviews [@guest2006] |
| Focus groups | Advisors, teachers, students (incl. students who had FX) | Purposive | 3 groups × 6–8 participants, two rounds |
| Student survey (perceptions of monitoring, privacy) | All bachelor's students of the university | Stratified random sampling by year of study and programme | n = 357 for N ≈ 5 000 (Cochran, 95 % confidence, ±5 %) [@cochran1977]; with a 60 % response rate ≈ 595 invitations (`tools/sample_size.py`) |
| Dashboard experiment (H3) | Advisors and teachers who supervise 1st/2nd-year groups | Convenience sample of all available, counterbalanced within-subject design | 34 participants for d = 0.5, 24 for d = 0.6 (α = 0.05, power 0.8) [@faul2007]; if fewer are available, results are treated as exploratory with effect sizes reported |
| Pilot (H4) | Academic groups of 1st-year bachelor's students in spring 2027 | Cluster assignment of whole groups to pilot/control, matched by programme and prior GPA | ≈ 330 student-course enrolments per arm to detect a reduction of FX/F from 20 % to 12 % (α = 0.05, power 0.8) |

**Limitations of generalisability.** One university and one national grading model; purposive qualitative samples are not statistically representative; the pilot is quasi-experimental (no individual randomisation, possible teacher effects). These are mitigated by external validation on OULAD, control variables and transparent reporting.

# 4. Data collection methods

| Method | Type | Research question | Why chosen; validity, reliability, ethics |
|---|---|---|---|
| Semi-structured interviews | Qual. | Requirements, RQ3 | Deep understanding of how risk is detected today; same guide for all (reliability); member checking of summaries (validity). |
| Focus groups | Qual. | Requirements, RQ3 | Group interaction reveals shared needs and disagreements; moderated by protocol; recorded with consent. |
| Document analysis | Qual. | RQ1 | Academic policy, grading regulations, curricula — to define the target variable correctly. |
| Secondary analysis of AIS/LMS data | Quant. | RQ1, RQ2, RQ4 | Objective behavioural and outcome data without extra burden on students; pseudonymised export; data-quality audit. |
| Computational experiments | Quant. | RQ1, RQ2 | Controlled comparison of models with fixed seeds, temporal validation and identical feature sets (reproducibility). |
| Structured questionnaire (SUS, TAM, trust) | Quant. | RQ3 | Validated scales [@brooke1996; @davis1989; @venkatesh2003] allow comparison with other systems; reliability checked with Cronbach's α. |
| Within-subject experiment + usability test (think-aloud) | Mixed | RQ3 | Each participant sees both dashboard variants in counterbalanced order — controls individual differences; think-aloud explains the scores. |
| Quasi-experimental pilot | Quant. | RQ4 | Real-world effect under normal teaching conditions; ethically acceptable because control groups receive standard support. |

# 5. Data collection instruments

* **Interview guide** (Appendix A) — 5 blocks, 18 questions: current practice, early signals, information needs, trust in algorithms, privacy.
* **Focus-group protocol** — questions for round 1 (needs) and round 2 (prototype evaluation), see PW2 Section 6.
* **Questionnaire** (Appendix B) — demographic block, SUS (10 items), TAM usefulness and ease of use (8 items), trust in the risk prediction (4 items), open questions.
* **Data extraction specification** — list of AIS/LMS fields, their types, the pseudonymisation rule (salted hash of student ID) and the weekly aggregation rules (Appendix C).
* **Informed consent form** (Appendix D).
* **Observation checklist for usability sessions** — task completion, time on task, errors, requests for help.

**Pilot testing.** All instruments are pilot-tested before full data collection: the interview guide with 2 advisors, the questionnaire with 10 students and 3 teachers (clarity, time ≤ 10 min, cultural appropriateness), and translations into Kazakh and Russian are checked with back-translation. The data extraction script is tested on one semester of one programme and the computed features are compared by hand for 50 random students.

# 6. Data collection process

| When | Where / how | What | Ethics and logistics |
|---|---|---|---|
| Nov 2026 | Online application to the university ethics committee and academic office | Approval, data-sharing agreement | Purpose limitation, list of fields, retention period |
| Nov – Dec 2026 | In person (meeting room) or Zoom/Teams, 40–45 min | 12–15 interviews | Written consent, audio recording only with permission, pseudonyms in transcripts |
| Dec 2026 | Campus, 60–90 min | Focus groups round 1 | Consent, confidentiality agreement among participants |
| Dec 2026 – Jan 2027 | IT department exports CSV from AIS/LMS to an encrypted university server | Historical data 2021/22–2025/26 | Only pseudonymised IDs; no names, IIN, contacts; access limited to the researcher and supervisor |
| Jan 2027 | Download from the official OULAD page | Open dataset | CC-BY licence; cite the dataset |
| Mar 2027 | Computer lab / online, 45 min per participant | Usability test + dashboard experiment + SUS/TAM | Consent; synthetic or pseudonymised student data shown in the prototype |
| Mar – Apr 2027 | Google Forms / MS Forms link via university e-mail | Student survey | Anonymous, voluntary, no IP collection, can stop at any time |
| Feb – May 2027 | Weekly automatic ETL from AIS/LMS | Pilot data | Advisors see risk lists only for their own groups; students are informed about the pilot and may opt out |

**Ethical safeguards.** Informed consent; anonymity and confidentiality (pseudonymisation, aggregated reporting, minimum group size of 10 in any published table); voluntary participation; compliance with the Law of the Republic of Kazakhstan "On Personal Data and Their Protection" and institutional policy; predictions are advisory and never used for sanctions [@slade2013]; data deleted one year after the defence.

# 7. Data analysis methods

**Qualitative data.** Transcripts are coded with **reflexive thematic analysis** [@braun2006] in Taguette/NVivo: familiarisation → initial codes → themes → review → definition. Two coders independently code 20 % of transcripts; disagreements are discussed and the codebook refined (reliability). Themes feed into requirements and explain quantitative results.

**Quantitative data — modelling (RQ1, RQ2).**

* Pre-processing: cleaning, weekly aggregation, missing-value indicators, scaling for linear models.
* Models: logistic regression (interpretable baseline), random forest, gradient boosting (XGBoost) [@chen2016; @pedregosa2011]; one model per prediction week w ∈ {2, 4, 6, 8}.
* Validation: temporal hold-out (last academic year) + 10-fold stratified cross-validation on training years; hyper-parameters tuned only inside training folds; class imbalance handled by class weights and threshold selection.
* Metrics: ROC-AUC, PR-AUC, recall, precision, F1, Brier score; fairness — difference in recall and false-positive rate between subgroups (gender, language of instruction, grant/paid) [@baker2022].
* Explanation: SHAP values for global feature importance (RQ1) and per-student reasons shown in the dashboard [@lundberg2017].
* Tests: DeLong test for AUC (H1); Wilcoxon signed-rank test over folds (H2).

**Quantitative data — survey, experiment, pilot (RQ3, RQ4).** Descriptive statistics (mean, SD, median, distributions); internal consistency (Cronbach's α ≥ 0.70); paired t-test or Wilcoxon test for the within-subject dashboard comparison and one-sample t-test SUS vs 68 (H3); χ² test and multilevel logistic regression (students nested in groups, prior GPA as covariate) for the pilot (H4). Effect sizes (Cohen's *d*, odds ratios) and 95 % confidence intervals are always reported. Tools: Python (pandas, scikit-learn, statsmodels), JASP.

**Integration of findings.** Explanatory integration and triangulation: a joint display table places each hypothesis next to the corresponding qualitative themes (e.g. low trust scores explained by interview comments about "black-box" predictions); convergence, complementarity or divergence is discussed explicitly.

**Reliability, validity, transparency.** Pre-registered analysis plan (hypotheses, metrics, thresholds) before the test set is opened; code and synthetic sample data in a public repository; audit trail of qualitative coding decisions; threats to validity (internal, external, construct, conclusion) discussed in the thesis.

# 8. Summary of the methodology

* **Research design:** design science research with a sequential mixed-methods design (qualitative exploration → quantitative modelling → mixed evaluation and pilot) integrated by triangulation.
* **Population and sampling:** census of historical student-course enrolments (and OULAD for external validation); purposive samples of 12–15 interviewees and 3 focus groups; stratified random survey sample of ≈ 357 students; 24–34 advisors/teachers in the dashboard experiment; ≈ 330 enrolments per arm in the cluster-assigned pilot. Sample sizes are justified by saturation research, Cochran's formula and power analysis (`tools/sample_size.py`).
* **Data collection methods and instruments:** interviews, focus groups, document analysis, secondary analysis of AIS/LMS data, computational experiments, validated SUS/TAM questionnaires, usability observation; all instruments are pilot-tested; consent, pseudonymisation and legal compliance are ensured.
* **Data analysis techniques:** thematic analysis; logistic regression, random forest and gradient boosting with temporal validation, SHAP explanations and fairness checks; DeLong, Wilcoxon, t/Mann–Whitney, χ² and multilevel logistic regression; Python and JASP.

The methodology ensures **rigour** (pre-specified hypotheses, temporal validation, standard metrics), **reliability** (validated scales, double coding, fixed seeds and published code), and **validity** (triangulation, external validation on OULAD, fairness analysis). Remaining limitations — one institution, a quasi-experimental pilot, possible incompleteness of attendance data and a small number of advisors — are acknowledged and will be reported as threats to validity together with suggestions for multi-institutional follow-up studies.
