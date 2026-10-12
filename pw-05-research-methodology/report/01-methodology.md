---
title: "Practical Work 5. Research Plan and Methodology"
subtitle: "Topic: Design and Evaluation of an Agentic AI Platform Integrating the Agent Loop, Model Context Protocol (MCP) Tools and Retrieval-Augmented Generation (RAG)"
author: "Student: ____________________  ·  Group: ________  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-US
abstract: |
  A research plan and methodology are developed for the design and evaluation of an agentic AI platform that combines an LLM agent loop, tools connected through the Model Context Protocol (MCP) and retrieval-augmented generation (RAG). Research questions and hypotheses are derived from the literature review; design science research with a sequential mixed-methods design is chosen and justified; the units of analysis, sampling strategies and sample sizes (justified by power analysis, Cochran's formula and saturation research) are defined; data collection methods and instruments (interview guide, questionnaire with SUS/TAM scales, evaluation dataset specification, consent form) are developed; the data collection process with ethical safeguards and the data analysis techniques (RAG and agent metrics, human and LLM-as-a-judge rating, statistical tests, thematic analysis, triangulation) are planned. **Keywords:** research methodology, design science, mixed methods, evaluation of LLM agents, MCP, RAG.
---

# Introduction

This work turns the research plan (PW2) and the literature review (PW3, PW4) into a detailed, replicable methodology. The study designs and evaluates an open, model-agnostic agentic AI platform (working name **AgentHub**) in which a large language model works in an agent loop, calls tools exposed by MCP servers [@mcp_spec] and uses a RAG service over university documents [@lewis2020]. The object of research is the architecture of tool-augmented LLM agents; the subject is the effect of integration method, retrieval configuration, loop design and guardrails on task success, answer quality, effort, cost and security.

# 1. Research questions and hypotheses

The questions follow from the gaps identified in the literature review: the benefits of MCP are claimed but not measured [@anthropic2024mcp; @hou2026]; RAG configurations are rarely compared on non-English corporate documents [@gao2023]; agent reliability on multi-step tasks remains low [@liu2024agentbench; @yao2025tau]; indirect prompt injection threatens tool-using agents [@greshake2023].

| Code | Research question | Hypothesis (testable) | Measure |
|------|--------------------------------|--------------------------------------|----------------------|
| RQ1 | Does MCP reduce the effort of connecting tools compared with bespoke function calling? | H1: MCP integration takes ≥ 30 % less developer time. | Minutes, changed lines of code, integration errors |
| RQ2 | Which retrieval configuration gives the best context recall and faithfulness on bilingual documents? | H2: hybrid retrieval with reranking outperforms BM25-only and dense-only. | Context precision/recall, faithfulness, correctness |
| RQ3 | How do agent-loop design choices affect task success, cost and latency? | H3: agentic RAG has higher task success than single-shot RAG on multi-step questions at < 2× token cost. | Task success, tokens, USD, latency, iterations |
| RQ4 | How effective are guardrails against indirect prompt injection? | H4: with guardrails ASR < 5 % and benign success drops ≤ 5 p.p. | Attack success rate, benign task success |
| RQ5 | Is the platform usable and useful for developers and end users? | H5: SUS ≥ 68; TAM usefulness ≥ 5/7. | SUS, TAM items |

The questions are specific (one factor and one outcome each), measurable and aligned with the goal of the thesis.

# 2. Research design

**Overall framework: Design Science Research (DSR).** The artefact — the platform and its reference architecture — is built and evaluated in iterations following the DSR process: problem identification, objectives of a solution, design and development, demonstration, evaluation and communication [@hevner2004; @peffers2007]. Evaluation uses a **sequential mixed-methods design** [@creswell2018]:

1. **Exploratory qualitative phase** — interviews and focus groups define requirements, typical tasks and acceptable automatic actions.
2. **Quantitative experimental phase** — controlled computational experiments (factorial comparison of configurations on fixed datasets) and a within-subject developer experiment.
3. **Evaluation phase (mixed)** — red-teaming, pilot use, SUS/TAM survey and focus group 2.
4. **Integration** — triangulation of metrics, traces and qualitative themes in a joint display.

**Type of research** (by the classification used in the course lecture *Research Methodology: An Introduction*): applied, empirical, analytical, mixed qualitative–quantitative, decision-oriented; it combines the **experimental** approach (manipulation of configurations and integration method), the **simulation** approach (agents act against simulated tool back-ends and simulated attacks) and the **inferential** approach (survey of users).

**Justification.** RQ1–RQ4 concern causal effects of design choices and therefore require controlled experiments with quantitative measures; RQ5 and the interpretation of failures require users' views, which only qualitative data can reveal. The design supports **validity** (controlled comparisons, triangulation, human validation of automatic metrics), **reliability** (fixed datasets, pinned model versions, repeated runs, standard scales) and **feasibility** (experiments run on open data and synthetic back-ends, without access to personal data).

# 3. Target population and sample

| Strand | Population / units of analysis | Sampling strategy | Expected sample size and justification |
|-----------|-------------------------|------------------------------|------------------------------------------|
| Questions for RAG experiments (RQ2, RQ3) | All questions that students and staff may ask about public university documents (Russian, Kazakh, English) | Stratified sampling of questions by document type, language and difficulty (single-fact / multi-step); written by the researcher and validated by two staff members | ≈ 300 questions, of which ≥ 150 multi-step; 152 per configuration are needed to detect 60 % → 75 % success (α = 0.05, power 0.8); paired McNemar design requires fewer |
| Tool tasks (RQ3, RQ4) | Realistic multi-step tasks over calendar, timetable, ticketing and database tools | Purposive selection from the task catalogue collected in interviews | ≈ 60 tasks × 3 repetitions × each configuration |
| Attack cases (RQ4) | Indirect prompt-injection variants in documents and tool outputs | Systematic generation from attack taxonomies [@greshake2023; @owasp2025llm] | ≈ 200 cases: estimate ASR ≈ 5 % with ±3 % margin (95 % confidence) |
| Developer experiment (RQ1) | Developers able to write Python (senior IT students, junior engineers) | Convenience sample, counterbalanced within-subject design | 24 participants for d = 0.6, 34 for d = 0.5 (α = 0.05, power 0.8) [@faul2007] |
| Interviews | Developers, IT staff, administrative staff, students | Purposive maximum-variation and snowball sampling | 12–15 interviews; saturation is typically reached by about 12 interviews [@guest2006] |
| Focus groups | Developers, staff, students | Purposive | 3 groups × 6–8 participants, two rounds |
| User survey (RQ5) | Students and staff who used the pilot | Stratified random invitation by role and year of study | n = 357 for N ≈ 5 000 (Cochran, 95 %, ±5 %) [@cochran1977]; at 60 % response ≈ 595 invitations |

All numbers are produced by `tools/sample_size.py`. In terms of sample design, **probability sampling** (stratified random) is used where results are generalised to users, and **non-probability sampling** (purposive, snowball, convenience) where depth or feasibility matters.

**Limitations of generalisability.** One university and its documents; a limited set of models at a fixed point in time; simulated rather than production back-ends; student developers rather than professional teams. These are mitigated by including two different models (commercial and open-weight), publishing datasets and configurations, and discussing external validity.

# 4. Data collection methods

| Method | Type | RQ | Why chosen; validity, reliability, ethics |
|-------------------|-------|-----|----------------------------------------------------------|
| Semi-structured interviews | Qual. | Requirements, RQ5 | Reveal real tasks, needed tools and trust conditions; same guide for all; summaries checked with participants. |
| Focus groups | Qual. | Requirements, RQ5 | Group discussion shows shared needs and disagreements; moderated protocol; recorded with consent. |
| Document analysis | Qual. | RQ2 | Public regulations, calendars, syllabi form the corpus; ensures realistic content without personal data. |
| Computational experiments | Quant. | RQ2–RQ4 | Controlled manipulation of one factor at a time on fixed datasets; pinned model versions; 3 repetitions; full execution traces stored. |
| Developer experiment (task-based, timed) | Quant. + observation | RQ1 | Same tools integrated with MCP and bespoke code in counterbalanced order controls individual differences; screen recording measures time and errors. |
| Red-teaming (attack suite) | Quant. | RQ4 | Systematic attack cases make results comparable across configurations; performed only on test systems. |
| Questionnaire (SUS, TAM) | Quant. | RQ5 | Validated scales [@brooke1996; @davis1989; @venkatesh2003] allow comparison with other systems; reliability checked with Cronbach's α. |
| Usability observation with think-aloud | Qual. | RQ5 | Explains scores and finds concrete interface problems. |

# 5. Data collection instruments

* **Interview guide** (Appendix A) — 5 blocks, 18 questions: current work, tasks for an assistant, tools and data, trust and control, risks.
* **Focus-group protocol** — questions for rounds 1 and 2 (PW2, Section 6).
* **Questionnaire** (Appendix B) — background, SUS (10 items), TAM usefulness and ease of use (8 items), trust in answers and actions (4 items), open questions.
* **Evaluation dataset specification** (Appendix C) — schemas for questions, tool tasks, attack cases and run logs.
* **Developer task sheet** — the same three tools (timetable lookup, ticket creation, document search) to be integrated twice; acceptance tests define "done".
* **Informed consent form** (Appendix D).

**Pilot testing.** The interview guide is tried with two developers; the questionnaire with 10 students and 3 staff (clarity, ≤ 10 minutes, Kazakh/Russian translation checked by back-translation); 30 questions and 10 tasks are run end-to-end to test the harness, metrics and logging; the developer task sheet is tried by two volunteers to calibrate the time limit.

# 6. Data collection process

| When | Where / how | What | Ethics and logistics |
|------------------|-----------------------------|-------------------------|------------------------------------|
| Nov 2026 | University ethics/approval process | Approval of studies with participants | Purpose, data, retention, consent forms |
| Nov 2026 | In person or Zoom/Teams, 40–45 min | 12–15 interviews | Written consent; recording only with permission; pseudonyms |
| Nov – Dec 2026 | Campus, 60–90 min | Focus groups round 1 | Consent; confidentiality among participants |
| Dec 2026 – Jan 2027 | Researcher's workstation | Corpus of public documents; questions; tasks; attack cases | No personal data; two-person validation of reference answers |
| Feb – Mar 2027 | Evaluation harness on a cloud server | Experiment runs and traces | API keys stored as secrets; synthetic back-ends only |
| Mar 2027 | Computer lab, 2 × 45 min per participant | Developer experiment | Consent; compensation; results anonymised |
| Mar – Apr 2027 | Online (Google/MS Forms) after pilot use | SUS/TAM survey | Anonymous, voluntary, no IP collection |
| Apr 2027 | Campus | Focus groups round 2 | As above |

**Ethical safeguards.** Informed consent, anonymity and confidentiality, voluntary participation; compliance with the personal-data law of Kazakhstan [@kz2013pdlaw]; no real user data in experiments; attacks only against own test systems; write actions in the pilot require human approval; documents with any personal data are excluded from the corpus.

# 7. Data analysis methods

**Quantitative — experiments.**

* *Retrieval and answers (RQ2):* context precision and recall, faithfulness, answer relevance and correctness computed with RAGAS-style metrics [@es2024]; correctness additionally rated by two humans on a 20 % sample (Cohen's κ ≥ 0.7 required before relying on LLM-as-a-judge [@zheng2023]); Friedman test across retrieval methods with Holm-corrected Wilcoxon post-hoc tests; results reported per language.
* *Agent loop (RQ3):* task success rate with Wilson 95 % confidence intervals; McNemar test for paired success of two configurations; tokens, USD and latency as medians and p95 with bootstrap intervals; failure analysis of traces by category (wrong tool, wrong arguments, premature stop, loop limit, hallucinated answer).
* *Security (RQ4):* attack success rate with Wilson intervals; two-proportion test with vs without guardrails; benign success difference.
* *Developer study (RQ1):* paired t-test (or Wilcoxon if non-normal) on minutes and lines of code; effect size Cohen's *d*; integration errors counted.

**Quantitative — survey (RQ5).** Descriptive statistics; Cronbach's α ≥ 0.70; one-sample t-tests (SUS vs 68; usefulness vs 5); comparison of roles with Mann–Whitney U.

**Qualitative.** Reflexive thematic analysis [@braun2006] of interview and focus-group transcripts; two coders double-code 20 % of the material; themes are linked to requirements and to failure categories.

**Integration of findings.** A joint display places each hypothesis next to related themes (e.g. low trust explained by missing source citations); convergence or divergence is discussed explicitly. Tools: Python (pandas, SciPy, statsmodels), RAGAS, JASP, Taguette.

**Reliability, validity, transparency.** Pre-registered analysis plan (metrics, thresholds, tests) before the main runs; fixed seeds and pinned model versions; publication of code, configurations, datasets and anonymised results; threats to validity (internal, external, construct, conclusion) discussed in the thesis.

# 8. Summary of the methodology

* **Research design:** design science research with a sequential mixed-methods evaluation (qualitative exploration → controlled experiments and developer study → mixed evaluation), integrated by triangulation.
* **Population and sampling:** ≈ 300 stratified questions, ≈ 60 purposive tool tasks and ≈ 200 systematic attack cases; 24–34 developers (power analysis); 12–15 interviewees and 3 focus groups (purposive, saturation); ≈ 357 survey respondents (stratified random, Cochran's formula).
* **Data collection methods and instruments:** interviews, focus groups, document analysis, computational experiments with full tracing, timed developer experiment, red-teaming, SUS/TAM questionnaire; all instruments pilot-tested; consent and data-protection safeguards.
* **Data analysis techniques:** RAG and agent metrics with human validation; Friedman, Wilcoxon, McNemar, t-tests, Wilson and bootstrap intervals; thematic analysis; Python, RAGAS, JASP.

The methodology meets the **criteria of good research** discussed in the course lecture: it is *systematic* (defined phases and procedures), *logical* (hypotheses derived from the literature and tested deductively), *empirical* (conclusions based on measured data) and *replicable* (datasets, configurations and code are published). Remaining limitations — one institution, fast-changing models and protocols, simulated back-ends and student developers — are acknowledged and will be reported as threats to validity.
