---
title: "Practical Work 5. Research Plan and Methodology"
subtitle: "Topic: Tools for LLM Agents — Connecting Tools to an AI Platform through the Model Context Protocol (MCP) and LangChain"
author: "Student: ____________________  ·  Group: ________  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-US
abstract: |
  A research plan and methodology are developed for a simple, practical question: what is the best way to connect tools (functions that call external systems) to an LLM agent on an AI platform — as native LangChain tools defined with the `@tool` decorator, or as a server of the Model Context Protocol (MCP) loaded into the agent with `langchain-mcp-adapters`? Four research questions with testable hypotheses are derived from gaps in the literature: developer effort when the same tools are reused in two applications, tool-call accuracy of the agent (MCP vs native tools; 5 vs 20 available tools), latency added by MCP transports (stdio and streamable HTTP), and developers' perceived usability. A mixed-methods, mainly quantitative design is chosen and justified: a within-subjects developer experiment with counterbalancing (24–36 developers, power analysis), a benchmark task suite (120 tasks × 3 runs, McNemar power analysis), a latency micro-benchmark (1,000 calls per condition), a SUS/TAM questionnaire and 12–15 semi-structured interviews with think-aloud observation (saturation). Instruments (interview guide, questionnaire, developer task sheet with benchmark specification, consent form), the data collection process with ethical safeguards and the analysis plan (paired t-test, McNemar, bootstrap confidence intervals, thematic analysis, joint display) are presented. **Keywords:** LLM agents, tool calling, function calling, Model Context Protocol, LangChain, LangGraph, research methodology, mixed methods, controlled experiment.
---

# Introduction

This work turns the research plan (PW2) and the literature review (PW3, PW4) into a detailed and replicable methodology. The topic is deliberately narrow and practical: **how tools are connected to an LLM agent on an AI platform**. A *tool* is an ordinary function (for example, "get the timetable of group X") that the language model may ask the application to run; the model receives the tool's name, description and JSON schema of its arguments and, instead of text, returns a structured *tool call* — this mechanism is called **function calling** or tool calling [@schick2023; @qin2024; @patil2024]. An **agent** repeats a simple loop: the LLM decides what to do → the application executes the requested tool → the result is returned to the LLM → the LLM continues or gives the final answer [@yao2023react; @wang2024survey; @schluntz2024].

Two common ways of connecting tools are compared:

* **Native LangChain tools.** LangChain and LangGraph are open-source Python frameworks for building agents [@langchain2025lg1; @langchain_docs]. A Python function marked with the `@tool` decorator becomes a tool that lives *inside* the agent's process; to use it in another application the code has to be copied or packaged again.
* **MCP tools.** The Model Context Protocol is an open standard that separates the tool from the agent [@anthropic2024mcp; @mcp_spec]. A **host** application (the AI platform or chat application) contains an MCP **client**, which connects to an MCP **server**; the server exposes *tools* (functions), *resources* (read-only data) and *prompts* (templates). Client and server talk JSON-RPC over a **transport**: *stdio* (the server is a local subprocess) or *streamable HTTP* (the server is a network service). Once written, one server can be used by any MCP client — a LangGraph agent, a desktop assistant or an IDE. The library `langchain-mcp-adapters` (`MultiServerMCPClient`) loads the tools of MCP servers into LangChain/LangGraph agents [@langchain_mcpadapters].

The software stack of the study is: the official `mcp` Python SDK [@mcp_python_sdk], `langchain`, `langgraph` and `langchain-mcp-adapters`, **FastAPI** for small mock back-end services with synthetic data, and **pytest** for acceptance tests. The model behind the agent is reached through an **OpenAI-compatible chat API**, so it can be a cloud model or a self-hosted open-weight model served by vLLM or Ollama [@vllm_docs; @ollama_openai]; the choice of model is a controlled variable, not the object of study. Retrieval-augmented generation (RAG) is out of scope (it is the topic of PW6).

The **object** of research is the tool layer of LLM agents; the **subject** is the effect of the tool-connection method (MCP vs native) on developer effort, tool-call accuracy, latency and usability.

# 1. Research questions and hypotheses

The questions follow from gaps found in the literature review. (1) MCP is promoted as a way to "write a tool once and use it everywhere", but this benefit is claimed rather than measured [@anthropic2024mcp; @hou2026]. (2) MCP benchmarks evaluate how well *models* use MCP servers [@luo2025; @wang2025mcpbench], and tool-use benchmarks show that accuracy falls on realistic multi-step tasks [@qin2024; @yao2025tau], but no study compares the same tools connected through MCP and natively, or measures the effect of the number of available tools in a controlled way. (3) The extra cost of the protocol layer (process or network hop) is not reported. (4) Developers' experience with MCP has not been measured with standard usability scales.

| Code | Research question | Hypothesis (testable) | Measure |
|-------------|-----------------------------|---------------------------------|--------------------|
| RQ1 (effort) | When the same three tools must be used in two different agent applications, does connecting them through an MCP server take less developer time and code than native LangChain `@tool` functions? | H1: total time to pass all acceptance tests in both applications is at least 25 % lower with MCP (paired comparison). | Minutes to "all tests green", lines of code, failed test runs |
| RQ2 (accuracy) | Does the agent choose the right tool with correct arguments equally often when tools come from MCP and when they are native, and how does accuracy change when the number of available tools grows from 5 to 20? | H2a: MCP and native tools give equivalent tool-call accuracy (95 % CI of the difference within ±5 p.p.). H2b: with 20 tools accuracy is at least 10 p.p. lower than with 5 tools. | Tool-call accuracy (right tool + correct arguments), task success |
| RQ3 (overhead) | How much latency does MCP add to one tool call (stdio and streamable HTTP) compared with an in-process LangChain tool? | H3: median overhead is below 10 ms for stdio and below 30 ms for local HTTP, i.e. below 2 % of the time of one agent step. | Milliseconds per call (median, p95); share of step time |
| RQ4 (usability) | How do developers perceive the ease of use and usefulness of connecting tools through MCP? | H4: mean SUS of the MCP workflow is ≥ 68 (above average) and not lower than for native tools. | SUS (0–100), TAM ease of use and usefulness (1–7), interview themes |

Each question is **specific** (one factor, one outcome), **measurable** (every hypothesis has a numeric threshold and a measure that can be obtained automatically or with a standard scale) and **feasible** within a master's thesis.

# 2. Research design

**Approach: mixed methods, mainly quantitative** — an *explanatory sequential* design (QUAN → qual) [@creswell2018]. The quantitative strand answers RQ1–RQ4 with numbers; a short qualitative strand then explains them (why a condition was faster or why the agent picked a wrong tool). Inside a design science frame [@hevner2004; @peffers2007] a small artefact is built — three tools implemented both as an MCP server and as native LangChain tools, plus an evaluation harness — and then evaluated.

| Component | Type | Answers | What is done |
|------------------|--------------------|-----------|----------------------------------------|
| Developer experiment | Quantitative, controlled, within-subjects | RQ1, RQ4 | Each developer integrates tools once natively and once through MCP (different but equivalent tool sets, counterbalanced order) |
| Benchmark task suite | Quantitative, computational experiment | RQ2 | The same 120 tasks are run by an agent in four conditions: native/MCP × 5/20 tools, 3 runs each, two models |
| Latency micro-benchmark | Quantitative, computational experiment | RQ3 | 1,000 calls of the same tool in-process, via MCP stdio and via MCP streamable HTTP |
| Questionnaire | Quantitative, survey | RQ4 | SUS and TAM items after each condition |
| Interviews + think-aloud | Qualitative | Explains RQ1, RQ2, RQ4 | 12–15 short interviews; think-aloud notes during the experiment |

**Type of research** (by the classification used in the course lecture *Research Methodology: An Introduction* following Kothari): **applied** (it solves a practical engineering problem), **empirical** (conclusions are based on observation and measurement), **analytical** (existing technologies are critically compared), **mixed** quantitative–qualitative and **decision-oriented** (the result helps a platform team decide how to connect tools). It uses the **experimental** approach (the connection method and the number of tools are manipulated while other factors are held constant), the **simulation** approach (agents act against mock back-end services with synthetic data) and the **inferential** approach (conclusions about developers in general are drawn from a sample).

**Justification.**

* *Why mostly quantitative:* RQ1–RQ3 ask about cause and effect ("does MCP reduce time / change accuracy / add latency?"), which requires controlled comparisons and statistical tests.
* *Why also qualitative:* numbers do not explain *why*; interviews and think-aloud reveal difficulties (configuration of transports, debugging, documentation) that inform recommendations.
* *Why within-subjects:* individual programming skill differs strongly between people; when each person works in both conditions, they serve as their own control, which removes this variation and needs fewer participants. Learning effects are controlled by counterbalancing (Section 3).
* **Validity:** the same tasks, tools, model, prompts and acceptance tests in both conditions (internal validity); established measures (SUS, TAM, tool-call accuracy as in tool-use benchmarks) (construct validity); two models and two tool sets (external validity).
* **Reliability:** pinned library and model versions, temperature 0, three runs per task, fixed hardware, automatic measurement from logs and tests, standard questionnaires with Cronbach's α.
* **Feasibility:** only open-source libraries, mock services with synthetic data (no access to real university systems or personal data), one computer lab, about two hours per participant.

# 3. Target population and sample

| Strand | Population / units of analysis | Sampling strategy | Sample size and justification |
|----------------|----------------------|--------------------------|----------------------------------------|
| Developer experiment (RQ1, RQ4) | Developers who can write Python: senior IT students, master's students and junior engineers | Convenience sample with screening (Python test task); random assignment to 4 groups of a Latin square (order × tool set) | Paired t-test, α = 0.05, power 0.80 [@faul2007]: d = 0.6 → 24, d = 0.5 → 34, d = 0.8 → 15. Plan 24 (multiple of 4), recruit 28 for ≈ 15 % dropout; 36 if resources allow |
| Benchmark task suite (RQ2) | Realistic user requests to a university AI assistant that need 0, 1 or 2 tool calls | Stratified purposive construction: 4 task types (single tool, two tools in sequence, argument extraction from text, no tool needed) × 5 domains | McNemar test for 5 vs 20 tools (drop 90 % → 80 %, discordant 12 % / 2 %): 108 tasks; plan 120 (10 % reserve). 120 × 3 runs = 360 trials per condition give a CI of ±3.3 p.p. for the MCP–native difference |
| Latency measurements (RQ3) | Single tool calls on the reference machine | All calls after 50 warm-up calls; order of conditions randomised | 1,000 calls per condition → 50 observations above the 95th percentile, enough for a stable p95 |
| Interviews (RQ1–RQ4, explanation) | Participants of the developer experiment | Purposive maximum-variation sampling: experience level, faster condition, preferred method | 12–15 interviews; saturation is typically reached by about 12 interviews in a homogeneous group [@guest2006] |

All numbers are produced by `tools/sample_size.py`. The developer sample is **non-probability** (convenience) because a full sampling frame of "all Python developers" does not exist; randomness is introduced where it matters for internal validity — in the *assignment* of participants to orders and tool sets. The task suite is constructed, not sampled from logs, because no real log of tool requests exists; stratification guarantees that all task types are covered.

**Counterbalancing (Latin square).** Group 1: native + set A → MCP + set B; group 2: MCP + set A → native + set B; group 3: native + set B → MCP + set A; group 4: MCP + set B → native + set A. Set A (`get_timetable`, `create_ticket`, `search_documents`) and set B (`get_exam_schedule`, `book_room`, `search_news`) have the same structure and difficulty, so a person never implements the same tool twice.

**Limits of generalisability.** Participants are mainly students and junior developers, not experienced teams; only Python and three simple tools; specific versions of fast-changing libraries; two models; synthetic back-ends instead of production systems; one university. Results are therefore generalisable to *similar small tool integrations by junior developers*; they are reported with these limits and with all materials published so that others can repeat the study in other settings.

# 4. Data collection methods

| Method | Type | RQ | Why chosen; validity, reliability, ethics |
|--------------------|---------|---------|------------------------------------------------|
| Timed developer experiment with acceptance tests | Quant. | RQ1 | Direct measure of effort; "done" is defined objectively by pytest tests, not by the participant's opinion; time, lines of code and test runs are logged automatically; screen recording only with consent. |
| Benchmark runs with full execution traces | Quant. | RQ2 | Every tool call (name, arguments, result) is logged, so accuracy is computed automatically and can be re-checked; same tasks in all conditions; pinned versions, temperature 0, 3 runs. |
| Latency micro-benchmark | Quant. | RQ3 | Isolates the protocol overhead from the much larger and more variable LLM time; high-resolution timer (`time.perf_counter_ns`); warm-up excludes start-up effects. |
| Questionnaire (SUS, TAM) | Quant. | RQ4 | Validated, widely used scales [@brooke1996; @davis1989; @venkatesh2003] allow comparison with other systems; filled in after each condition; anonymous codes. |
| Think-aloud observation | Qual. | RQ1, RQ4 | Participants say what they are doing during the task; the observer notes problems (e.g. "transport not configured", "schema error") that time alone does not show. |
| Semi-structured interviews | Qual. | Explains RQ1–RQ4 | Same guide for all; 20–25 minutes right after the session while experience is fresh; audio recorded only with consent; summaries checked with participants (member checking). |

# 5. Data collection instruments

* **Developer task sheet** (Appendix C) — a starter repository, the description of the tools, mock FastAPI back-ends, two target applications (App 1: a command-line LangGraph agent; App 2: a FastAPI chat service in a separate repository with its own agent), acceptance tests and a time limit of 40 minutes per condition.
* **Benchmark task-suite specification** (Appendix C, Section C.2) — format of one task: instruction, expected tool(s), expected arguments, expected final state of the mock service, task type; and the four experimental conditions.
* **Evaluation harness** — a Python script that builds the agent for each condition, runs the tasks, writes JSON traces and computes metrics; the latency script measures calls in the three modes.
* **Questionnaire** (Appendix B) — background, SUS (10 items), TAM ease of use and usefulness adapted to tool integration (8 items), open questions.
* **Interview guide** (Appendix A) — 4 blocks, 12 questions.
* **Informed consent form** (Appendix D).

**Pilot testing.** Two volunteer developers complete the full session (both conditions, questionnaire, interview); their data are not included in the analysis. The pilot checks that the instructions are clear, the 40-minute limit is realistic, set A and set B take similar time, and the tests and logging work. Twenty tasks are run end-to-end in all conditions to check the harness, the automatic accuracy labels (compared with manual labels) and that no task is trivially easy or impossible; ambiguous tasks are rewritten or replaced. The questionnaire is checked for clarity and completion time (≤ 10 minutes).

# 6. Data collection process

| When | Where / how | What | Ethics and logistics |
|------------------|-----------------------------|-------------------------|------------------------------------|
| Nov 2026 | University ethics/approval procedure | Approval of the study with participants | Purpose, data, retention, consent form submitted |
| Nov 2026 | Researcher's workstation | Tools (sets A and B) as MCP servers and as `@tool` functions; mock FastAPI services; tests; 120 tasks | Synthetic data only; versions of all libraries pinned |
| Dec 2026 | Computer lab | Pilot: 2 developers, 20 tasks | Pilot data excluded from analysis |
| Dec 2026 – Jan 2027 | Reference machine / cloud VM | Benchmark runs (120 tasks × 3 runs × 4 conditions × 2 models = 2,880 agent runs) and latency benchmark | API keys stored as secrets; cost limit per run |
| Feb – Mar 2027 | Computer lab, ≈ 2 hours per participant (2 × 40 min tasks + questionnaires + 20–25 min interview) | Developer experiment, SUS/TAM, think-aloud, interviews | Written consent; voluntary; participant codes P01…; no link to grades |
| Mar – Apr 2027 | Researcher's workstation | Transcription, coding, analysis | Recordings deleted after transcription |

**Logistics.** All lab computers have the same pre-installed environment (Python, libraries, IDE) checked by a script before each session; participants receive a prepared repository and a model API endpoint provided by the researcher (no personal accounts or payments needed); sessions are scheduled in small groups, one observer per two participants.

**Ethical safeguards.**

* *Informed consent* — participants receive the information sheet and sign the consent form (Appendix D) before the session.
* *Voluntary participation* — anyone may stop at any time without explanation; participation and results have no influence on grades; students are not recruited by their own instructors.
* *Anonymity and confidentiality* — only participant codes are used in data files; the key linking names and codes is stored separately and destroyed after the study; results are published only in aggregated form.
* *Data handling* — data are stored on an encrypted university drive with access only for the researcher and supervisor; screen and audio recordings are deleted after coding; anonymised data are kept until one year after the defence; processing follows the Law of the Republic of Kazakhstan on personal data [@kz2013pdlaw].
* *Safety of the systems* — tools act only on mock services with synthetic data; no real university systems are changed. Security of MCP (tool poisoning, prompt injection [@greshake2023; @radosevich2025]) is acknowledged as a risk but is not the object of this study.

# 7. Data analysis methods

**Quantitative analysis.**

* *RQ1 (effort):* for each participant the difference between the two conditions in total minutes (both applications), lines of code and failed test runs. Paired t-test if the differences are approximately normal (Shapiro–Wilk), otherwise the Wilcoxon signed-rank test; effect size Cohen's d~z~ with 95 % CI. Time for the first application and for reuse in the second application is reported separately (MCP may be slower for the first and faster for the second). Order and tool-set effects are checked with a linear mixed model (condition + order + tool set, random intercept for participant). Participants who do not finish within the limit receive the limit value (40 min) and are analysed in a sensitivity analysis.
* *RQ2 (reliability):* a tool call is **correct** if the right tool is chosen and all arguments match the expected values; **tool-call accuracy** = share of runs where all required calls are correct and no unnecessary call is made; **task success** = the mock service ends in the expected state. Labels are computed automatically from traces; two raters check a random 20 % sample (Cohen's κ ≥ 0.8 required). H2a: paired difference MCP − native with a 95 % bootstrap CI (resampling tasks); equivalence is accepted if the CI lies within ±5 p.p. H2b: McNemar test on task level (task solved = at least 2 of 3 runs correct), 5 vs 20 tools; as a robustness check a mixed-effects logistic regression (method × number of tools, random intercept for task). Consistency over runs is reported as pass^3^ [@yao2025tau]. Errors are classified: wrong tool, wrong arguments, missing call, unnecessary call, wrong order. Results are shown separately for each model.
* *RQ3 (overhead):* median and 95th percentile of call latency per mode with bootstrap 95 % CIs; overhead = MCP latency − in-process latency; its share of the median time of one agent step (LLM call + tool call) measured in the benchmark.
* *RQ4 (usability):* SUS score 0–100 [@brooke1996]; one-sample t-test against 68; paired Wilcoxon test MCP vs native; TAM scales as item means with Cronbach's α ≥ 0.70.

**Qualitative analysis.** Interview transcripts and think-aloud notes are analysed with reflexive thematic analysis in six steps (familiarisation, coding, generating, reviewing, defining and naming themes, writing up) [@braun2006]. A second coder independently codes 20 % of the material; differences are discussed until agreement. Expected themes include setup difficulty, debugging, reuse, documentation and trust in tool calls.

**Integration (mixed methods).** A *joint display* table places each hypothesis next to the related themes (for example, "MCP slower for the first application" next to the theme "configuring the transport was confusing"), and agreement or disagreement between the strands is discussed explicitly [@creswell2018].

**Reliability, validity and transparency.** The analysis plan (measures, thresholds, tests) is fixed before the main data collection; library and model versions, prompts, seeds and the hardware are recorded; all code, tasks, traces and anonymised data are published in the project repository; threats to validity (internal, construct, external, conclusion) are discussed in the thesis. Tools: Python (pandas, SciPy, statsmodels), pytest, JSON traces (optionally LangSmith [@langsmith]), Taguette for qualitative coding.

# 8. Summary of the methodology

* **Research design:** mixed methods, mainly quantitative (explanatory sequential QUAN → qual): a within-subjects controlled developer experiment, a benchmark task suite and a latency micro-benchmark, followed by short interviews and think-aloud analysis; integrated in a joint display.
* **Population and sampling:** 24 developers (power analysis, d = 0.6; recruit 28; up to 36), assigned at random to a counterbalanced Latin square; 120 stratified tasks × 3 runs × 4 conditions × 2 models (McNemar power analysis); 1,000 latency measurements per mode; 12–15 interviewees selected purposively for maximum variation (saturation).
* **Data collection methods and instruments:** timed tasks with pytest acceptance tests, automatic execution traces, latency script, SUS/TAM questionnaire, think-aloud protocol and interview guide; all pilot-tested; consent, voluntariness, anonymity and secure data handling ensured.
* **Data analysis techniques:** paired t-test or Wilcoxon, mixed models, McNemar, bootstrap confidence intervals and equivalence testing, Cronbach's α; reflexive thematic analysis with double coding; joint display.

**Rigour.** Validity is supported by identical tasks and tests in both conditions, counterbalancing, objective acceptance tests, validated scales and triangulation of numbers with interviews; reliability by pinned versions, repeated runs, automatic measurement and inter-rater checks. The methodology meets the **criteria of good research** from the course lecture: it is *systematic* (clear phases and procedures in a fixed order), *logical* (hypotheses are derived from literature gaps and tested deductively), *empirical* (every conclusion is based on measured data) and *replicable* (tasks, code, versions and analysis scripts are published). **Limitations:** junior developers and simple tools, a laboratory setting with time limits, fast-changing libraries and protocol versions, synthetic back-ends and only two models; security of MCP and retrieval are outside the scope. These limits are stated openly and define directions for future work.
