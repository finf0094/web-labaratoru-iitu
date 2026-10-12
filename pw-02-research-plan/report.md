---
title: "Practical Work 2. Research Plan Development"
subtitle: "Topic: Design and Evaluation of an Agentic AI Platform Integrating the Agent Loop, Model Context Protocol (MCP) Tools and Retrieval-Augmented Generation (RAG)"
author: "Student: ____________________  ·  Group: ________  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-US
abstract: |
  A research plan is developed for the design and evaluation of an agentic AI platform in which a large language model (LLM) works in an agent loop, calls external tools exposed through the Model Context Protocol (MCP) and uses retrieval-augmented generation (RAG) over organisational documents. The plan defines the problem and its importance, the goal, five research questions with testable hypotheses, operational definitions of the core concepts, methods of data collection, analysis and validation, the required resources, research issues (constraints, variables, assumptions, ethics), the research structure, the testing strategy, a focus-group design, the budget and the schedule. An additional stage — security and responsible-AI assurance — is proposed. **Keywords:** research plan, AI agents, agent loop, Model Context Protocol, tool calling, retrieval-augmented generation, AI platform.
---

# Overview of the study plan

| Item of the study plan | Content for this project |
|-------------------------|------------------------------------------------------------------|
| **Purpose** (1–2 lines) | To design, build and evaluate an open, model-agnostic AI platform in which an LLM agent loop uses tools connected through MCP and a RAG service over university documents, and to measure how these components affect task success, answer quality, integration effort, cost and security. |
| **Problem** | Organisations want AI assistants that answer questions from their own documents *and* perform actions in their systems. Today every model-to-tool integration is written separately for each vendor, RAG pipelines are built ad hoc, agent loops fail unpredictably, and there is no agreed method to evaluate quality, cost and security (e.g. prompt injection through retrieved documents or tool outputs). |
| **Core concepts (operational definitions)** | See Section 2.4 — *agent loop*, *tool*, *MCP server*, *RAG*, *task success*, *faithfulness*, *context recall*, *integration effort*, *attack success rate*, *usability*. |
| **General method** | Design Science Research [@hevner2004; @peffers2007] with mixed-methods evaluation: requirements interviews → platform design and prototype → controlled experiments on benchmark task suites → developer study → security red-teaming → usability/acceptance study. |
| **Detailed methods** | Semi-structured interviews and focus groups with developers, IT staff and end users; construction of a bilingual (Russian/Kazakh/English) question set from public university documents; computational experiments with alternative RAG and agent-loop configurations; within-subject developer experiment (MCP vs bespoke integration); attack suite for indirect prompt injection [@greshake2023]; SUS and TAM questionnaires [@brooke1996; @davis1989]. |
| **Data quantification** | Task success (0/1 per task), answer correctness and faithfulness (0–1, RAGAS-style metrics [@es2024]), context precision/recall (0–1), latency (s), cost (tokens and USD per task), number of agent-loop iterations, integration effort (minutes and lines of code), attack success rate (%), SUS (0–100), TAM items (1–7). |

## Type of research and research process

Following the classification of research types and the research process presented in the course lecture *Research Methodology: An Introduction*, the planned study is characterised as follows.

| Basis of classification | Type of this study | Reason |
|-------------------|-----------------|-------------------------------------------------------|
| Descriptive vs analytical | Mainly **analytical** | Hypotheses about the effect of design choices are tested on collected data |
| Applied vs fundamental | **Applied** | Produces a working platform design for a practical problem of organisations |
| Qualitative vs quantitative | **Mixed** | Interviews and focus groups + experiments and statistical analysis |
| Conceptual vs empirical | **Empirical** | Conclusions are based on measurements of the prototype |
| Environment | **Laboratory** and **simulation** research, with a short **field** pilot | Controlled experiments on task suites; simulated attacks; pilot use by students and staff |
| Purpose | **Hypothesis-testing** (with an exploratory phase) | Tests causal effects of MCP, RAG configuration, loop design and guardrails |
| Orientation | **Decision-oriented** | Results guide architectural decisions of organisations adopting AI agents |

**Mapping to the research process.** (1) Formulating the research problem → Section 1; (2) extensive literature survey → LW1, PW3, PW4; (3) developing hypotheses → Section 2.3; (4) preparing the research design → Sections 2.5 and 4, PW5; (5) determining sample design → PW5; (6) collecting the data and (7) execution of the project → Sections 4 and 8; (8) analysis of data and (9) hypothesis testing → Section 5; (10) generalisations and interpretation and (11) preparation of the report → thesis chapters (Section 4.2).

# 1. Identify and define the problem

## 1.1 Problem statement

Large language models can follow instructions, but on their own they cannot see an organisation's current documents or act in its systems. Two techniques address this: **retrieval-augmented generation (RAG)**, which adds retrieved passages to the model's context [@lewis2020], and **tool use**, in which the model decides to call external functions and continues reasoning with their results [@yao2023react; @schick2023]. Running these steps repeatedly — think, call a tool, observe, decide again — is the **agent loop** that underlies modern AI agents [@wang2024survey].

In practice three problems appear:

1. **Integration problem (practical gap).** Every tool or data source has to be wired separately to every model vendor's function-calling format. The **Model Context Protocol (MCP)**, an open protocol introduced in November 2024, standardises how applications expose tools, resources and prompts to LLM clients [@anthropic2024mcp; @mcp_spec], but its effect on integration effort and reliability has not been measured systematically.
2. **Quality problem (scientific gap).** RAG quality depends on many choices — chunking, sparse vs dense retrieval, reranking, how retrieval is triggered — and on the language of documents. Models may ignore relevant passages placed in the middle of long contexts [@liu2024lost]. Evidence for Russian- and Kazakh-language corporate documents is scarce.
3. **Reliability and security problem.** Agents fail on multi-step tasks [@liu2024agentbench; @yao2025tau], and content returned by retrieval or tools can carry *indirect prompt injections* that hijack the agent [@greshake2023]; MCP adds new attack surfaces such as malicious tool descriptions [@hou2026].

## 1.2 Importance of the problem

* **For organisations (universities, SMEs, public bodies in Kazakhstan):** a reusable platform reduces the cost of building AI assistants, avoids vendor lock-in and allows sensitive data to stay on own servers in line with the personal-data law [@kz2013pdlaw].
* **For the scientific community:** controlled evidence on how MCP, RAG design and agent-loop design affect quality, cost and security, including bilingual (Russian/Kazakh) data.
* **For industry:** a reference architecture and an evaluation protocol that developers can reproduce; aligned with the national AI development agenda [@kz2024aiconcept].

# 2. Research plan

## 2.1 Goal

To design and empirically evaluate an open, model-agnostic agentic AI platform that combines an agent loop, MCP-based tool integration and a RAG service, and to determine which design choices maximise task success and answer faithfulness while keeping cost, latency and security risks acceptable.

## 2.2 Research questions

* **RQ1 (integration).** Does connecting tools through MCP reduce developer effort and integration errors compared with bespoke, provider-specific function calling?
* **RQ2 (retrieval).** Which RAG configuration — sparse (BM25), dense, or hybrid retrieval with reranking — gives the best context recall and answer faithfulness on a bilingual university document corpus?
* **RQ3 (agent loop).** How do agent-loop design choices (retrieval as a tool vs single-shot RAG, maximum number of iterations, self-reflection step, number and quality of tool descriptions) affect task success, cost and latency?
* **RQ4 (security).** How effective are guardrails (tool allow-lists, human approval of write actions, isolation of untrusted content) against indirect prompt injection delivered through retrieved documents and MCP tool outputs?
* **RQ5 (acceptance).** Do developers and end users perceive the platform as usable and useful?

## 2.3 Hypotheses

* **H1.** Integrating a new tool through MCP takes at least 30 % less developer time than a bespoke integration (paired t-test or Wilcoxon, α = 0.05).
* **H2.** Hybrid retrieval with reranking achieves higher context recall and faithfulness than BM25-only and dense-only retrieval (Friedman test with post-hoc Wilcoxon tests).
* **H3.** On multi-step questions, an agent that uses retrieval as a tool inside the loop ("agentic RAG") has a higher task success rate than single-shot RAG (McNemar test), at a cost increase of less than 2× tokens per task.
* **H4.** With guardrails enabled, the attack success rate of indirect prompt injection falls below 5 %, while benign task success decreases by no more than 5 percentage points.
* **H5.** The platform's mean SUS score is ≥ 68 and the mean perceived usefulness (TAM) is ≥ 5 on a 7-point scale.

## 2.4 Operational definitions of core concepts

| Concept | Operational definition and measurement |
|-----------------|-------------------------------------------------------------------------|
| Agent loop | Repeated cycle *model call → (optional) tool call → observation appended to context* until the model returns a final answer or the iteration limit is reached; measured by number of iterations per task. |
| Tool | A function with a name, natural-language description and JSON-Schema input that the model can request; executed by the platform, not by the model. |
| MCP server | A process that exposes tools, resources and prompts via the Model Context Protocol (JSON-RPC over stdio or streamable HTTP) [@mcp_spec]. |
| RAG | Retrieval of top-*k* document chunks for a query and their insertion into the model context before generation [@lewis2020]. |
| Task success | Binary: the final answer or final system state matches the reference defined for the task (checked automatically or by two raters). |
| Faithfulness | Share of claims in the answer that are supported by the retrieved context (0–1) [@es2024]. |
| Context precision / recall | Share of retrieved chunks that are relevant / share of reference facts present in retrieved chunks (0–1). |
| Integration effort | Minutes and changed lines of code needed to make a new tool usable by the agent and pass its acceptance test. |
| Attack success rate (ASR) | Share of injected test cases in which the agent performs the attacker's instruction (e.g. calls a forbidden tool or leaks data). |
| Cost / latency | Input + output tokens and USD per task; wall-clock seconds from request to final answer. |
| Usability / acceptance | SUS score (0–100) [@brooke1996]; mean of TAM perceived usefulness and ease-of-use items (1–7) [@davis1989]. |

## 2.5 Methods of data collection, analysis and validation

1. **Literature review and analogue analysis** (LW1, PW3, PW4).
2. **Interviews and focus groups** with developers, IT staff and potential end users to collect requirements and typical tasks; thematic analysis [@braun2006].
3. **Dataset construction:** a bilingual question set (≈ 300 questions with reference answers and source passages, of which ≥ 150 require several retrieval steps) from public IITU documents (regulations, academic calendar, syllabi, FAQ), a task suite (≈ 60 multi-step tasks requiring 2–5 tool calls, e.g. "find the deadline in the regulation and create a calendar reminder") and an attack suite (≈ 200 injection cases).
4. **Computational experiments:** the same tasks are run under different configurations (retrieval method, loop design, guardrails, two LLMs — a commercial API model and an open-weight model served locally); each configuration is repeated 3 times to account for model randomness.
5. **Developer experiment:** participants integrate the same tools with MCP and with bespoke code (counterbalanced order).
6. **Security red-teaming:** a suite of indirect-prompt-injection cases embedded in documents and tool outputs, following known attack patterns [@greshake2023; @owasp2025llm].
7. **Usability and acceptance study:** SUS/TAM questionnaires after a short pilot.

Validation: automatic metrics are checked against human ratings on a 20 % sample (Cohen's κ); LLM-as-a-judge scores [@zheng2023] are used only after agreement with human raters is confirmed.

## 2.6 Resources

| Type | Resources |
|---------|------------------------------------------------------------------------|
| Software | Python 3.12; official MCP SDK; FastAPI; PostgreSQL with pgvector or Qdrant; BM25 implementation; a multilingual embedding model and reranker; Docker; Git/GitHub; Zotero; RAGAS; JASP for statistics; Taguette/NVivo for qualitative coding. |
| Models | One commercial LLM via API (tool-calling capable); one open-weight instruction model (7–14 B parameters) served locally with an OpenAI-compatible server. |
| Hardware | Developer laptop (16–32 GB RAM); rented GPU server (24–48 GB VRAM) for the open-weight model and embeddings. |
| Data | Public IITU documents (Russian, Kazakh, English); synthetic tool back-ends (calendar, ticketing, timetable, database) with test data only. |
| Access | University library databases (Scopus, IEEE Xplore, ACM DL); API keys funded by the project; permission of the IT department for the pilot. |
| People | Supervisor; 24–34 student developers for the developer experiment; 12–15 interviewees; 3 focus groups; pilot users. |

# 3. Research issues

## 3.1 Potential problems and constraints

| Issue | Risk | Mitigation |
|-------------------|---------------------------------------|-------------------------------------------|
| Non-determinism of LLMs | Results vary between runs | Fixed temperature, 3 repetitions, report means with 95 % confidence intervals |
| Model and API changes | Provider updates a model during the study | Pin model versions; record dates; include an open-weight model as a stable baseline |
| API cost | Experiments become expensive | Token budget per configuration; caching; pilot runs on small subsets first |
| Language coverage | Weak quality for Kazakh text | Multilingual embeddings; report results per language; human review of Kazakh answers |
| Data access and privacy | Personal data in documents | Only public documents and synthetic data; no real student records |
| Participant availability | Developers busy during exams | Sessions outside exam weeks; online option; small compensation |
| Evolving MCP specification | Protocol versions change | Fix one specification version for the experiments and document it |

## 3.2 Variables and assumptions

* **Independent variables:** integration method (MCP / bespoke); retrieval method (BM25 / dense / hybrid + rerank); chunk size; RAG mode (single-shot / agentic); loop settings (max iterations, reflection on/off, number of tools); guardrails (on/off); model (commercial / open-weight); question language.
* **Dependent variables:** task success, correctness, faithfulness, context precision/recall, latency, cost, iterations, integration effort, attack success rate, SUS, TAM.
* **Control variables:** prompts and tool descriptions held constant within a comparison; same hardware; same question set; same model version.
* **Assumptions:** the question set and task suite are representative of real requests; reference answers are correct (double-checked); automated metrics correlate with human judgement after calibration; participants' prior experience is balanced by counterbalancing.

## 3.3 Ethical considerations

* Informed consent of all interview, focus-group, survey and experiment participants; voluntary participation and the right to withdraw.
* No personal data in the corpus; synthetic back-ends for tools that would change data; the pilot uses read-only tools or human approval for any write action.
* Responsible AI: answers show sources; the system states when it does not know; harmful or out-of-scope requests are refused; red-teaming results are disclosed responsibly.
* Compliance with the Law of the Republic of Kazakhstan "On Personal Data and Their Protection" [@kz2013pdlaw] and alignment with AI risk-management guidance [@nist2023rmf].

# 4. Research structure

## 4.1 Stages

1. **Background study** — literature review and analysis of analogues.
2. **Requirements** — interviews, focus group 1, use-case and task catalogue.
3. **Design** — reference architecture: agent loop service, MCP client and servers, RAG service, guardrails, tracing and evaluation module.
4. **Implementation** — prototype and test back-ends; dataset construction.
5. **Experiments** — RAG configurations (H2), loop designs (H3), guardrails (H4), two models.
6. **Developer study** — MCP vs bespoke integration (H1).
7. **User evaluation** — pilot, SUS/TAM, focus group 2 (H5).
8. **Analysis and writing** — statistical tests, interpretation, thesis.

## 4.2 Structure of the thesis

| Chapter | Content | Connection |
|--------------|---------------------------------------------------|----------------------------------------|
| Introduction | Relevance, problem, goal, RQs, hypotheses, novelty | Sections 1–2 of this plan |
| 1. Literature review and analogues | LLM agents, tool use, MCP, RAG, evaluation, security; comparison of five platforms | Gaps found here define RQ1–RQ5 and the evaluation metrics |
| 2. Methodology | Design science, mixed methods, datasets, samples, instruments, analysis | Uses limitations of earlier studies to design fair comparisons |
| 3. Platform design and implementation | Requirements, architecture, MCP integration, RAG pipeline, guardrails, observability | Implements requirements from interviews and best practices from Chapter 1 |
| 4. Results and discussion | Experiment results, developer study, security, usability; threats to validity | Tests H1–H5 and compares results with earlier studies |
| Conclusion | Answers to RQs, recommendations for organisations, future work | — |
| References, appendices | Instruments, task suite, attack suite, configuration files | — |

# 5. Testing

* **Hypothesis testing.** H1 — paired t-test or Wilcoxon signed-rank test on minutes and lines of code; H2 — Friedman test across three retrieval methods with Holm-corrected post-hoc Wilcoxon tests on per-question scores; H3 — McNemar test on paired task outcomes, bootstrap confidence intervals for cost ratios; H4 — attack success rate with Wilson 95 % confidence intervals, two-proportion comparison with and without guardrails; H5 — one-sample t-tests of SUS against 68 and TAM usefulness against 5.
* **Benchmarks.** Internal question set and task suite; comparison with published agent benchmarks for orientation [@liu2024agentbench; @yao2025tau]; baselines: (a) LLM without retrieval or tools, (b) single-shot RAG, (c) bespoke function calling.
* **Software testing.** Unit tests for tools and MCP servers; contract tests of JSON schemas; integration tests of the full loop with mocked models; load test (concurrent sessions) and measurement of p50/p95 latency; security tests against the OWASP Top 10 for LLM applications [@owasp2025llm].
* **Comparison with expectations.** Retrieval and agent results are compared with values reported in the literature for similar settings [@gao2023; @es2024]; anomalies (e.g. loops that never terminate, tool-selection errors) are analysed from execution traces.

# 6. Focus group

| Element | Plan |
|---------------|-------------------------------------------------------------------------|
| Participants | Group A — 6–8 software developers (students of IT programmes and junior engineers); Group B — 6–8 IT/administrative staff who answer typical requests; Group C — 6–8 end users (students). Purposive selection with different experience levels. |
| Format | 60–90 min, moderated, recorded with consent; round 1 before development (needs, tasks, risks), round 2 after the prototype (evaluation). |
| Guiding questions (round 1) | 1) Which questions and tasks take most of your time? 2) Which documents and systems are needed to answer them? 3) Which actions may an AI assistant perform automatically and which need approval? 4) What would make you trust an answer (sources, explanations)? 5) What are your concerns (errors, privacy, security)? 6) (Developers) How do you integrate external APIs with LLMs today? |
| Guiding questions (round 2) | 1) Were the answers correct and properly sourced? 2) Was connecting a new tool via MCP clear? 3) Which failures did you notice? 4) Would you use the platform weekly? 5) What should be improved first? |
| Analysis | Transcription → coding → themes (tasks, trust, control, integration effort, risks) [@braun2006]; themes become requirements and explain quantitative results. |

# 7. Budget

Costs are estimated in KZT at an assumed rate of 500 KZT per USD; actual prices of API providers are checked before purchase.

| Item | Qty | Unit cost, KZT | Total, KZT |
|----------------------------------------------|--------|------------|-------------|
| LLM API tokens for experiments (≈ 60 M tokens incl. repetitions) | 1 | 250 000 | 250 000 |
| GPU cloud server for open-weight model and embeddings (≈ 150 h) | 150 h | 1 000 | 150 000 |
| Virtual server for the platform pilot, 4 months | 4 | 25 000 | 100 000 |
| Domain and TLS certificate | 1 | 10 000 | 10 000 |
| Participant compensation (developer study, focus groups, usability tests) | 50 | 3 000 | 150 000 |
| Transcription service (≈ 12 h of audio) | 12 h | 3 000 | 36 000 |
| Qualitative analysis software (or free Taguette) | 1 | 0–60 000 | 60 000 |
| Conference registration / publication fee | 1 | 60 000 | 60 000 |
| **Subtotal** | | | **816 000** |
| Contingency buffer (15 %) | | | 122 400 |
| **Total** | | | **≈ 938 400** |

**Possible funding sources:** university support of diploma and research projects (servers, licences), academic credits programmes of cloud and AI providers, student research grants and start-up competitions (e.g. through Astana Hub), sponsorship by an industry partner. The buffer covers price changes of APIs, extra experiment runs and additional participant sessions.

# 8. Schedule

| Phase | Period | Duration | Milestone |
|------------------------------------|------------------|-----------|-------------------------------------------|
| 1. Topic approval, literature review, analogues | Sep – Oct 2026 | 7 weeks | LW1, PW3, PW4 completed |
| 2. Methodology and instruments | Oct – Nov 2026 | 4 weeks | PW5; instruments pilot-tested |
| 3. Interviews and focus group 1 | Nov 2026 | 3 weeks | Requirements and task catalogue |
| 4. Architecture and prototype v1 | Nov 2026 – Jan 2027 | 8 weeks | Agent loop + MCP client + 3 MCP servers + RAG service (**demo by 15 Jan**) |
| 5. Dataset and task suite construction | Dec 2026 – Jan 2027 | 6 weeks (parallel) | 300 questions, 60 tasks, 200 attack cases |
| 6. Experiments (H2–H4) | Feb – Mar 2027 | 7 weeks | Results tables and traces |
| 7. Developer study (H1) | Mar 2027 | 3 weeks | Effort data |
| 8. Pilot, SUS/TAM, focus group 2 (H5) | Mar – Apr 2027 | 5 weeks | Acceptance results |
| 9. Analysis and thesis writing | Apr – May 2027 | 6 weeks | Full draft; **pre-defence in mid-May** |
| 10. Final defence | Jun 2027 | — | Defence |

Each phase includes 1–2 weeks of reserve; phases 4–5 and 6–7 overlap intentionally. If API access is delayed, experiments start with the open-weight model.

# 9. Additional stage: security and responsible-AI assurance

Because an agent can act in real systems, a separate cross-cutting stage is planned:

* **Threat modelling** of the platform (data flows between the model, MCP servers, retrieval index and users), using the OWASP Top 10 for LLM applications [@owasp2025llm] and the NIST AI RMF functions *Govern, Map, Measure, Manage* [@nist2023rmf].
* **Guardrail design:** least-privilege tool scopes, allow-lists per agent, human approval for irreversible actions, marking of untrusted content, output filtering, rate limits.
* **Observability:** every loop iteration, tool call and retrieved chunk is traced, enabling debugging and audit.
* **Reproducibility:** configuration files, prompts, model versions and seeds are versioned in Git; datasets and results are published (except sensitive cases).

# 10. Summary

The research addresses the practical and scientific problem of building AI assistants that both know an organisation's documents and act in its systems. The goal is to design and evaluate an open agentic AI platform that combines an agent loop, MCP-based tool integration and RAG. Five research questions and hypotheses cover integration effort (RQ1), retrieval quality (RQ2), agent-loop design (RQ3), security (RQ4) and acceptance (RQ5). The study is applied, empirical and analytical; it follows design science research with mixed methods: interviews and focus groups, dataset construction, controlled computational experiments, a developer experiment, red-teaming and a usability study. Risks — model non-determinism, cost, language coverage and evolving standards — have mitigation plans. The budget is about 0.94 million KZT including a 15 % buffer, and the work is scheduled from September 2026 to the defence in June 2027.

# References {.unnumbered}

::: {#refs}
:::
