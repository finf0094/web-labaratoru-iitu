---
title: "Practical Work 2. Research Plan Development"
subtitle: "Topic: Information System for Monitoring Students' Academic Performance with Machine-Learning-Based Early Warning of At-Risk Students"
author: "Student: ____________________  ·  Group: ________  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-GB
---

# Overview of the study plan

| Item of the study plan | Content for this project |
|---|---|
| **Purpose** (1–2 lines) | To design, build and evaluate an information system that monitors students' academic performance in real time and, using explainable machine learning, warns advisors about students at risk of failing a course early enough (by week 4–7 of a 15-week semester) to intervene. |
| **Problem** | Kazakhstani universities record grades, attendance and LMS activity in separate systems (e.g. Platonus, Moodle). Risk becomes visible only after the midterm (*rubezhnyi kontrol 1*, week 7–8) or after the final exam (grade FX/F), when it is often too late to help. Advisors have no early, explained signal and no workflow to track interventions. |
| **Core concepts (operational definitions)** | See Section 2.4 — *at-risk student*, *early*, *academic performance*, *engagement*, *prediction quality*, *explainability*, *usefulness*. |
| **General method** | Design Science Research with a sequential mixed-methods evaluation: qualitative requirements study → quantitative predictive modelling on historical and open data → prototype → usability/acceptance evaluation and a one-semester pilot. |
| **Detailed methods** | Semi-structured interviews and focus groups (advisors, teachers, students); secondary analysis of anonymised AIS/LMS records and the public OULAD dataset [@kuzilek2017]; ML experiments with logistic regression, random forest and gradient boosting [@chen2016; @pedregosa2011]; SHAP explanations [@lundberg2017]; SUS and TAM questionnaires [@brooke1996; @davis1989]; quasi-experimental pilot. |
| **Data quantification** | Grades on the 0–100 scale and letter grades (A…F); attendance as a share of attended classes; LMS activity as counts of logins/clicks/submissions per week; model quality as ROC-AUC, recall, precision, F1; usability as SUS score (0–100); acceptance as mean of 7-point Likert items; pilot outcome as pass rate and share of FX/F grades. |

# 1. Identify and define the problem

## 1.1 Problem statement

Universities in Kazakhstan work under the credit-technology system. A course grade is formed from the *admission rating* (average of two midterm controls, 60 %) and the final exam (40 %); a student with an admission rating below 50 is not admitted to the exam, and a final grade FX/F means a paid retake or, in the worst case, expulsion. All of these data are already stored in the university's automated information system (AIS) and LMS, but they are used for **reporting after the fact**, not for **prediction**.

Practical gap: existing domestic systems (e.g. Platonus) provide electronic grade books and attendance journals, but no predictive risk scoring or advisor workflow; international platforms with predictive analytics (EAB Navigate360, OU Analyse) are expensive, closed, tuned to other education systems, and not integrated with Kazakhstani AIS (see Laboratory work 1).

Scientific gap: the literature shows that LMS and grade data can predict course failure [@macfadyen2010; @conijn2017; @namoun2021], but (a) prediction quality strongly depends on the course and its instructional conditions [@gasevic2016], (b) few studies evaluate how teachers actually use predictions [@herodotou2019a], and (c) there is almost no evidence from Central Asian universities, whose grading model (midterm controls, admission rating, FX) differs from Western systems.

## 1.2 Importance of the problem

* **For students** — early help reduces the number of FX/F grades, paid retakes and dropouts.
* **For the university** — retention and graduation rates are accreditation and ranking indicators; each retained student also keeps tuition revenue.
* **For the scientific community** — the study contributes evidence on transferability of predictive learning analytics to a new national context and on the effect of explanations on advisor decisions.
* **For industry** — a reusable, open integration layer for Platonus/Moodle-type systems that local EdTech companies can adopt.

# 2. Research plan

## 2.1 Goal

To develop and empirically evaluate an explainable early-warning information system that identifies students at risk of failing a course by the middle of the semester with ROC-AUC ≥ 0.80 and is perceived by advisors as useful and usable.

## 2.2 Research questions

* **RQ1.** Which data available in a Kazakhstani university (current-control grades, attendance, LMS activity, prior GPA, demographics) are the strongest early predictors of course failure?
* **RQ2.** Which machine-learning model provides the best trade-off between recall of at-risk students and precision, and how does prediction quality change from week 2 to week 8 of the semester?
* **RQ3.** Do explanations of predictions (SHAP-based "reasons for risk") increase advisors' perceived usefulness and trust compared with a bare risk score?
* **RQ4.** Does the use of the system during one semester reduce the share of FX/F grades in pilot groups compared with control groups?

## 2.3 Hypotheses

* **H1.** A model using grades + attendance + LMS activity reaches ROC-AUC ≥ 0.80 by week 7 and significantly outperforms a model that uses grades only (DeLong test, α = 0.05).
* **H2.** Gradient boosting achieves higher recall at precision ≥ 0.60 than logistic regression (paired comparison over 10 cross-validation folds, Wilcoxon signed-rank test).
* **H3.** Advisors who see explanations report higher perceived usefulness (TAM, 7-point scale) than advisors who see only a risk score (independent t-test / Mann–Whitney U), and the system's SUS score is ≥ 68.
* **H4.** The share of FX/F grades in pilot groups is lower than in comparable control groups (χ² test / logistic regression controlling for prior GPA).

## 2.4 Operational definitions of core concepts

| Concept | Operational definition and measurement |
|---|---|
| Academic performance | Points (0–100) for current control, midterm controls 1 and 2, exam; final letter grade A–F; GPA (0–4). |
| At-risk student | Student whose final course grade is FX or F, or whose admission rating is < 50 (binary target, 1 = at risk). |
| Early prediction | Prediction made on data available up to week *w* of the semester, *w* ∈ {2, 4, 6, 8}; "early" = *w* ≤ 7 (before midterm 1 results). |
| Engagement | Weekly LMS log-ins, number of resource views, submissions on time, forum posts; attendance rate = attended / scheduled classes. |
| Prediction quality | ROC-AUC, recall (share of truly at-risk students detected), precision, F1, calibration (Brier score). |
| Explainability | Presence of top-3 feature contributions per student computed with SHAP [@lundberg2017], shown in the advisor dashboard. |
| Perceived usefulness / ease of use | Mean score of TAM items [@davis1989] on a 7-point Likert scale. |
| Usability | System Usability Scale score (0–100) [@brooke1996]. |

## 2.5 Methods of data collection, analysis and validation

1. **Literature review** (PW3, PW4) — systematic search in Scopus, IEEE Xplore, ScienceDirect, MDPI, Google Scholar.
2. **Interviews and focus groups** (qualitative) — requirements and validation of the risk definition with advisors, teachers, students; thematic analysis [@braun2006].
3. **Secondary data analysis** (quantitative) — anonymised historical records (2021/22–2025/26) from the AIS and LMS; public OULAD dataset for replication and benchmarking [@kuzilek2017].
4. **Experiments** — training and comparing models on temporal splits (train on earlier years, test on the latest year) to avoid data leakage.
5. **Prototype development** — web application (backend API, ETL from AIS/LMS, ML service, dashboard).
6. **Evaluation** — usability testing (SUS), acceptance survey (TAM), A/B comparison of dashboards with and without explanations, one-semester quasi-experimental pilot.

## 2.6 Resources

| Type | Resources |
|---|---|
| Data | Anonymised AIS (Platonus) export: grades, attendance, enrolment; Moodle logs; OULAD open dataset. |
| Software | Python 3.12, pandas, scikit-learn, XGBoost, SHAP; PostgreSQL; FastAPI / Django; React; Docker; Git/GitHub; Zotero; Google Forms; NVivo or Taguette for qualitative coding; JASP / SPSS for statistics. |
| Hardware | Developer laptop (16 GB RAM), university virtual server (4 vCPU, 16 GB RAM) for the pilot. |
| Access | Permission of the university's academic affairs office and ethics committee; databases Scopus/IEEE Xplore via the university library. |
| People | Supervisor, 2–3 advisors and 4–6 teachers for the pilot, IT department contact for data export. |

# 3. Research issues

## 3.1 Potential problems and constraints

| Issue | Risk | Mitigation |
|---|---|---|
| Access to institutional data | Legal/organisational delays in obtaining AIS export | Early request with a data-sharing agreement; fall back to OULAD for model development. |
| Data quality | Missing attendance records, inconsistent course codes, teachers filling journals late | Data-quality audit, imputation rules, "data completeness" feature, exclude courses with < 50 % completeness. |
| Class imbalance | At-risk students are typically 10–20 % | Stratified splits, class weights, threshold tuning, report precision–recall curves. |
| Participant availability | Advisors and teachers are busy during sessions | Schedule interviews outside exam weeks; short (≤ 45 min) sessions; online option. |
| Technical constraints | No public API in the AIS | CSV/Excel export + ETL; read-only database replica if allowed. |
| Concept drift | Curricula and grading rules change between years | Temporal validation; retraining every semester; monitoring of model performance. |

## 3.2 Variables and assumptions

* **Dependent variables:** at-risk status (binary), final course score (0–100); for evaluation — SUS, TAM scores, FX/F rate.
* **Independent variables:** weekly current-control points, midterm points (when available), attendance rate, LMS activity counts, timeliness of submissions, prior GPA, number of previous FX/F, study year, programme, form of study (grant/paid), language of instruction.
* **Control variables:** course, teacher, semester, group size.
* **Assumptions:** grades and attendance in the AIS are entered within one week of the class; LMS logs reflect real learning activity; the definition of risk (FX/F or admission rating < 50) is accepted by the academic office; historical patterns are reasonably stable between consecutive years.

## 3.3 Ethical considerations

* Personal data are processed in accordance with the Law of the Republic of Kazakhstan "On Personal Data and Their Protection" and university policy; only pseudonymised identifiers leave the AIS.
* Informed consent is obtained from all interview, focus-group and survey participants; participation is voluntary and can be withdrawn.
* Predictions are **advisory**: no automatic sanctions; a human advisor always makes the decision.
* Algorithmic fairness is checked across gender, language of instruction and form of study [@baker2022]; students have the right to see why they were flagged [@slade2013].
* Data are stored on university servers with role-based access and encryption; logs of who viewed which student record are kept.

# 4. Research structure

## 4.1 Stages

1. **Background study** — literature review, analysis of analogues (LW1, PW3, PW4).
2. **Requirements and problem validation** — interviews, focus group 1.
3. **Data collection and preparation** — data agreement, export, cleaning, feature engineering.
4. **Modelling** — baseline and advanced models, temporal validation, explanation.
5. **System design and development** — architecture, database, ETL, ML service, dashboard.
6. **Evaluation** — usability test, acceptance survey, focus group 2, semester pilot.
7. **Analysis and conclusion** — statistical testing of H1–H4, interpretation, thesis writing.

## 4.2 Structure of the thesis

| Chapter | Content | Connection |
|---|---|---|
| Introduction | Relevance, problem, goal, RQs, hypotheses, novelty | Based on Sections 1–2 of this plan |
| 1. Literature review and analysis of analogues | Learning analytics, EWS, ML for performance prediction, ethics; comparison of 5 systems | Gaps found here define the RQs and feature set |
| 2. Methodology | Design science + mixed methods, data, sampling, instruments, analysis | Uses gaps/limitations from Chapter 1 to choose models and evaluation metrics |
| 3. System design and implementation | Requirements, architecture, data model, ML pipeline, UI | Implements requirements from interviews and the best model from Chapter 2 experiments |
| 4. Results and discussion | Model results, usability, acceptance, pilot outcomes, threats to validity | Tests H1–H4; compares with results of earlier studies from Chapter 1 |
| Conclusion | Answers to RQs, contribution, limitations, future work | — |
| References, Appendices | Interview guide, questionnaires, consent form, code repository | — |

# 5. Testing

* **Hypothesis testing.** H1 — DeLong test for the difference of two correlated ROC-AUCs; H2 — Wilcoxon signed-rank test over 10 folds; H3 — t-test or Mann–Whitney U on TAM scores, one-sample t-test of SUS vs 68; H4 — χ² test and logistic regression with prior GPA as a covariate. Significance level α = 0.05, effect sizes reported (Cohen's *d*, odds ratio).
* **Model testing.** Benchmarks: (a) majority-class baseline, (b) rule "admission rating < 50", (c) logistic regression. Test on the most recent academic year (temporal hold-out) and on OULAD for external validity. Metrics: ROC-AUC, PR-AUC, recall, precision, F1, Brier score; fairness gap in recall between subgroups.
* **Software testing.** Unit tests for ETL and feature computation (pytest), API tests, load test of the dashboard with 10 000 students × 50 courses (Locust), security test of authentication and role-based access (OWASP Top 10 checklist), accuracy test — re-computation of 100 random students' features by hand.
* **Comparison with expectations.** Expected AUC by week 7 is 0.80–0.90 based on previous studies [@macfadyen2010; @conijn2017; @namoun2021]; deviations will be analysed per course and per programme.

# 6. Focus group

| Element | Plan |
|---|---|
| Participants | Group A — 6–8 advisors / curators; Group B — 6–8 teachers of first-year courses; Group C — 6–8 students (1st–2nd year, incl. students who previously received FX). Selected purposively from different programmes. |
| Format | 60–90 min, moderated, audio-recorded with consent; two rounds: before development (requirements) and after the prototype (evaluation). |
| Guiding questions (round 1) | 1) How do you currently find out that a student is struggling? 2) Which signals appear first? 3) What information would you need to act earlier? 4) What would make you trust or distrust an automatic risk score? 5) What actions do you take when a student is at risk? 6) What privacy concerns do you have? |
| Guiding questions (round 2) | 1) Is the risk list understandable? 2) Are the "reasons for risk" correct and useful? 3) What would you change in the dashboard? 4) Would you use it weekly? Why / why not? 5) Did a prediction surprise you? |
| Analysis | Transcription → open coding → themes (needs, trust, workload, privacy, usability) following [@braun2006]; recurring themes become requirements or change requests; results are triangulated with survey data. |

# 7. Budget

| Item | Qty | Unit cost, KZT | Total, KZT |
|---|---|---|---|
| Cloud/virtual server for pilot (4 vCPU, 16 GB RAM), 6 months | 6 | 25 000 | 150 000 |
| Domain + SSL certificate | 1 | 10 000 | 10 000 |
| Qualitative analysis software (NVivo student licence) or free Taguette | 1 | 0–60 000 | 60 000 |
| Statistical software (JASP — free; SPSS academic licence via university) | 1 | 0 | 0 |
| Participant compensation (gift cards for focus groups and usability tests) | 30 | 3 000 | 90 000 |
| Survey incentive (prize draw) | 3 | 10 000 | 30 000 |
| Transcription of interviews (auto-transcription service) | 10 h | 3 000 | 30 000 |
| Printing of consent forms and questionnaires | — | — | 10 000 |
| Conference registration / publication fee (local conference) | 1 | 50 000 | 50 000 |
| **Subtotal** | | | **430 000** |
| Contingency buffer (15 %) | | | 64 500 |
| **Total** | | | **≈ 494 500** |

**Sources of funding:** university support for diploma projects (server, software licences), departmental research budget, student research grants and competitions (e.g. university innovation contests), EdTech industry partner sponsorship. The buffer covers server overuse, extra participant sessions and delays in data collection.

# 8. Schedule

| Phase | Period | Duration | Milestone |
|---|---|---|---|
| 1. Topic approval, literature review, analogues | Sep – Oct 2026 | 7 weeks | Approved topic; LW1, PW3, PW4 completed |
| 2. Methodology and instruments | Oct – Nov 2026 | 4 weeks | PW5 methodology; interview guide and questionnaires pilot-tested |
| 3. Ethics approval and data access | Nov 2026 | 3 weeks | Signed data-sharing agreement; consent forms approved |
| 4. Interviews + focus group 1 | Nov – Dec 2026 | 4 weeks | Requirements specification |
| 5. Data preparation and modelling | Dec 2026 – Feb 2027 | 9 weeks | Best model selected, H1–H2 tested (**prototype model ready by 15 Feb**) |
| 6. System development | Jan – Mar 2027 | 10 weeks | Working prototype deployed on test server |
| 7. Evaluation: usability test, survey, focus group 2 | Mar – Apr 2027 | 5 weeks | SUS/TAM results, H3 tested |
| 8. Pilot during spring semester (weeks 1–15) | Feb – May 2027 | 15 weeks (parallel) | Pilot outcome data, H4 tested |
| 9. Thesis writing and pre-defence | Apr – May 2027 | 6 weeks | Full thesis draft (**pre-defence in mid-May**) |
| 10. Final defence | Jun 2027 | — | Defence |

Flexibility: phases 5–6 and 6–8 overlap intentionally; each phase has 1–2 weeks of reserve; if institutional data are delayed, modelling starts on OULAD and is transferred later.

# 9. Additional stage: Risk management and data management plan

Because the project depends on sensitive institutional data, an additional stage — **data management and risk monitoring** — runs through the whole project:

* **Data management plan:** what data are collected, file formats (CSV, Parquet), naming conventions, storage (encrypted university server, no personal laptops), retention period (deleted 1 year after defence), versioning of datasets and models (DVC/Git).
* **Reproducibility:** code in a Git repository, fixed random seeds, environment described with `requirements.txt` / Docker, experiment tracking (MLflow).
* **Risk register:** reviewed every two weeks with the supervisor (data access, participant drop-out, technical failures, schedule slips).
* **Dissemination:** results presented at a student conference, short paper submitted to a local journal, open-source release of non-sensitive code.

# 10. Summary

The research addresses a practical and scientific problem: Kazakhstani universities collect rich academic data but detect struggling students too late, and the literature lacks evidence on explainable early-warning systems in this context. The goal is to build and evaluate an explainable early-warning information system that predicts course failure by mid-semester (ROC-AUC ≥ 0.80) and is accepted by advisors. Four research questions and hypotheses cover predictors (RQ1), model choice and timing (RQ2), effect of explanations (RQ3) and real-world impact (RQ4). The study follows a design-science approach with sequential mixed methods: interviews and focus groups, secondary analysis of institutional and open data, ML experiments, prototype development, usability/acceptance evaluation and a one-semester pilot. Key risks — data access, data quality, imbalance and ethics — have mitigation plans. The estimated budget is about 0.5 million KZT including a 15 % buffer, and the work is scheduled from September 2026 to the defence in June 2027.

# References {.unnumbered}

::: {#refs}
:::
