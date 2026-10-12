---
title: "Practical Work 3. Literature Review Techniques"
subtitle: "Topic: Design and Evaluation of an Agentic AI Platform Integrating the Agent Loop, Model Context Protocol (MCP) Tools and Retrieval-Augmented Generation (RAG)"
author: "Student: ____________________  ·  Group: ________  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-US
abstract: |
  The literature on tool-augmented large language model (LLM) agents, retrieval-augmented generation (RAG) and the Model Context Protocol (MCP) was searched, filtered and summarised. Academic databases and preprint servers were queried with Boolean search strings, and the results were extended by citation analysis and backward/forward snowballing. Inclusion and exclusion criteria were applied, and 12 key papers were summarised in a review matrix (authors, research question, methodology, findings, limitations, relevance, conclusions, links). The review shows that RAG and tool use substantially extend LLM capabilities, but that agents remain unreliable on multi-step tasks, retrieval quality depends strongly on configuration and language, evaluation methods are not standardised, and tool-using agents are vulnerable to indirect prompt injection. MCP is widely adopted in practice but barely studied empirically. Gaps are categorised as theoretical, methodological, data-related and application-based, and concrete research directions are derived. **Keywords:** literature review, LLM agents, agent loop, tool use, retrieval-augmented generation, Model Context Protocol, research gaps.
---

# Objective and outcome

**Objective:** to learn how to search, filter and summarise academic literature on the research topic.
**Outcome:** a summarised literature review (Section e) and a categorised list of research gaps (Section d).

**Questions that guide the review** (from the research plan, PW2):

* RQ-L1. How do LLMs use external knowledge (retrieval) and external tools, and how is the agent loop organised?
* RQ-L2. How are RAG systems and agents evaluated, and how reliable are they?
* RQ-L3. What risks (security, prompt injection) arise when agents are connected to tools and data, including through MCP?

# a. Search for relevant articles and papers

## a.1 Databases and sources

| Source | Why it is used |
|------------------|--------------------------------------------------------------|
| ACL Anthology | Main NLP venues (ACL, EMNLP, NAACL, EACL, TACL): retrieval, RAG, evaluation |
| NeurIPS / ICLR proceedings, OpenReview | Machine-learning venues where most agent and tool-use papers appear |
| ACM Digital Library | KDD, CCS/AISec (security of LLM applications), SIGIR (information retrieval) |
| IEEE Xplore | IEEE TPAMI, IEEE Transactions on Big Data (vector search), software-engineering conferences |
| SpringerLink, ScienceDirect | Survey articles in journals (e.g. *Frontiers of Computer Science*) |
| arXiv (cs.CL, cs.AI, cs.CR) | Very recent preprints — essential for MCP (introduced in November 2024) |
| Scopus, Google Scholar | Citation counts, "cited by" lists, alerts for new work |
| Official documentation | MCP specification and vendor documentation (grey literature, used only for technical facts) |

## a.2 Keywords, synonyms and Boolean search strings

| Concept | Keywords and synonyms |
|----------|------------------------------------------------------------------|
| Model | "large language model", LLM, "language model", "foundation model" |
| Retrieval | "retrieval-augmented generation", RAG, "dense retrieval", "hybrid search", "vector database", reranking |
| Agents and tools | "LLM agent", "language agent", "autonomous agent", "tool use", "tool learning", "function calling", "API calls", ReAct |
| Protocol | "Model Context Protocol", MCP, "tool integration", "agent interoperability" |
| Evaluation and risk | benchmark, evaluation, faithfulness, hallucination, "prompt injection", security |

Example query strings:

1. `("retrieval-augmented generation" OR RAG) AND ("large language model" OR LLM) AND (survey OR evaluation)`
2. `("tool use" OR "tool learning" OR "function calling") AND ("language model" OR LLM) AND (agent*)`
3. `("LLM agent" OR "language agent") AND (benchmark OR evaluation) AND ("multi-step" OR interactive)`
4. `"Model Context Protocol" OR (MCP AND ("tool integration" OR agent*))`
5. `("prompt injection") AND ("LLM-integrated" OR agent* OR "tool use")`
6. `("dense retrieval" OR "hybrid retrieval" OR BM25) AND (multilingual OR Russian OR Kazakh)`

## a.3 Citation analysis and snowballing

* **Foundational, highly cited papers** were identified by sorting results by citations: RAG [@lewis2020], dense passage retrieval [@karpukhin2020], chain-of-thought prompting [@wei2022], ReAct [@yao2023react], Toolformer [@schick2023].
* **Backward snowballing:** reference lists of surveys on LLM agents [@wang2024survey; @xi2025], augmented language models [@mialon2023] and RAG [@gao2023; @fan2024] were scanned for empirical studies.
* **Forward snowballing:** "cited by" lists of ReAct, Toolformer and RAG led to recent work on tool benchmarks [@qin2024; @yao2025tau], self-reflective retrieval [@asai2024], RAG evaluation [@es2024], prompt injection [@greshake2023] and MCP [@hou2026].

# b. Filtering techniques

| Filter | Rule |
|---------------|------------------------------------------------------------------------|
| Date | Priority to 2020–2025 (the field changes rapidly); earlier works only if foundational (e.g. BM25 [@robertson2009]) |
| Type | Peer-reviewed journal articles and papers of core conferences (NeurIPS, ICLR, ACL/EMNLP/EACL, KDD, ACM CCS workshops); systematic surveys; arXiv preprints only for MCP and very recent topics, marked as preprints |
| Scope (title/abstract) | LLMs using retrieval or tools; agent loops; evaluation of RAG/agents; security of tool-using LLMs. Excluded: robotics-only agents, pure model-training papers without tools/retrieval, marketing articles |
| Quality | Core-ranked venues; papers with public code/data preferred; high citation count relative to age |
| Relevance to RQs | Method or result must inform RQ-L1, RQ-L2 or RQ-L3 |

**Screening flow of this review.** Records from the queries and snowballing were screened by title (≈ 40 candidate records retained), then by abstract and methodology (≈ 25 retained as relevant), and 12 papers were selected for the detailed matrix so that each research question and theme (retrieval, tool use, agent loop, evaluation, security, MCP) is covered by at least two studies. Other relevant papers are used in the discussion.

# c. Summary of key findings (review matrix)

: Table 1 — Review matrix, part 1: question, method and key findings

| No. | Authors, year | Research question | Methodology / framework | Key findings and main results |
|-------|--------------|----------------------|----------------------------|----------------------------------|
| 1 | Lewis et al., 2020 [@lewis2020] | Can a generator combined with a retrievable non-parametric memory improve knowledge-intensive NLP tasks? | Seq2seq generator (BART) + dense retriever over a Wikipedia vector index, trained end-to-end; RAG-Sequence and RAG-Token variants | State-of-the-art results on several open-domain QA tasks at the time; generations more specific and factual than a parametric-only model; knowledge can be updated by replacing the index |
| 2 | Karpukhin et al., 2020 [@karpukhin2020] | Can dense representations alone beat sparse retrieval for open-domain QA? | Dual BERT encoders trained on question–passage pairs with in-batch negatives; comparison with BM25 | Dense retrieval outperformed a strong BM25 baseline by about 9–19 % absolute in top-20 passage accuracy and improved end-to-end QA |
| 3 | Yao et al., 2023 [@yao2023react] | Does interleaving reasoning traces with actions improve LLM problem solving? | Few-shot prompting of a large LLM in a *thought → action → observation* loop; QA/fact verification with a Wikipedia API and interactive decision tasks | ReAct reduced hallucination compared with reasoning-only prompting and outperformed imitation/reinforcement-learning baselines on interactive tasks by large absolute margins; traces are interpretable |
| 4 | Schick et al., 2023 [@schick2023] | Can an LM learn by itself when and how to call tools? | Self-supervised annotation of API calls (calculator, QA, search, translation, calendar); keep calls that reduce loss; fine-tune a 6.7 B model | Tool use improved zero-shot performance on many tasks, often competitive with much larger models, without losing language-modelling ability |
| 5 | Qin et al., 2024 [@qin2024] | How can open models learn to use thousands of real-world APIs? | ToolBench instruction dataset over 16 000+ REST APIs; depth-first search decision tree for solution paths; automatic evaluator; API retriever | Fine-tuned open model approached the tool-use ability of a strong proprietary model and generalised to unseen APIs; retrieval of relevant APIs is needed when tools are many |
| 6 | Shinn et al., 2023 [@shinn2023] | Can agents improve through verbal self-reflection instead of weight updates? | Agent writes reflections on failures into episodic memory and retries; decision-making, reasoning and coding tasks | Reflection substantially improved success; e.g. 91 % pass@1 on a coding benchmark, above the base model |
| 7 | Liu N. F. et al., 2024 [@liu2024lost] | How well do LLMs use information placed in long input contexts? | Controlled experiments varying the position of the relevant document in multi-document QA and key–value retrieval | Performance is highest when relevant information is at the beginning or end and drops when it is in the middle, even for long-context models |
| 8 | Asai et al., 2024 [@asai2024] | Can an LM decide when to retrieve and critique its own output? | Training with special reflection tokens for retrieval on demand and self-critique (Self-RAG) | Outperformed strong LLMs and standard RAG on QA, reasoning and fact verification; improved factuality and citation accuracy |
| 9 | Es et al., 2024 [@es2024] | How can RAG pipelines be evaluated without human reference annotations? | Framework of LLM-based metrics: faithfulness, answer relevance, context relevance; validation against human judgements | Metrics agreed well with human assessments and allow fast, reference-free evaluation of RAG configurations |
| 10 | Yao et al., 2025 [@yao2025tau] | How reliable are tool-calling agents in realistic interactions with users and domain policies? | Benchmark with simulated users, domain APIs and policy documents (retail, airline); pass^k reliability metric | Even state-of-the-art function-calling agents solved fewer than half of the tasks and were inconsistent across repeated trials |
| 11 | Greshake et al., 2023 [@greshake2023] | Can attackers control LLM-integrated applications through data the model retrieves? | Threat taxonomy and practical attacks on real applications (search-augmented chat, code assistants, tool-using agents) | Indirect prompt injection enables data theft, manipulation of answers and misuse of tools; no reliable mitigation existed |
| 12 | Hou et al., 2026 [@hou2026] | What is the landscape of MCP and what security threats does it introduce? | Analysis of MCP architecture, server life cycle (creation, operation, update) and ecosystem; threat analysis | MCP is rapidly adopted as a standard interface between agents and tools; each life-cycle phase has specific security and privacy risks (e.g. malicious or spoofed servers, tool poisoning); research directions proposed |

: Table 2 — Review matrix, part 2: limitations, relevance, conclusions and links

| No. | Limitations / scope | Relevance to this research | Conclusions of the authors | Link |
|-------|----------------------|-----------------------|---------------------|------------------|
| 1 | Wikipedia only; single retrieval step; requires fine-tuning | Baseline RAG design for the platform's knowledge service | Hybrid parametric + non-parametric memory is effective for knowledge-intensive tasks | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) |
| 2 | Needs training pairs; domain shift; BM25 remains strong in some settings | Motivates comparison of sparse, dense and hybrid retrieval (H2) | Dense retrieval can replace or complement sparse retrieval | [doi:10.18653/v1/2020.emnlp-main.550](https://doi.org/10.18653/v1/2020.emnlp-main.550) |
| 3 | Prompting only; limited tools; errors propagate in long loops | Basis of the platform's agent loop (think–act–observe) | Reasoning and acting are synergistic | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| 4 | Tools used independently, no chaining or interaction | Shows value of tools; platform instead uses runtime function calling | LMs can teach themselves to use tools | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) |
| 5 | Synthetic instructions; evaluator based on an LLM | Tool retrieval is needed when many MCP tools are connected (RQ3) | Open models can master many real APIs | [arXiv:2307.16789](https://arxiv.org/abs/2307.16789) |
| 6 | Extra iterations increase cost; needs a success signal | Reflection step is one loop variant tested in RQ3 | Verbal feedback is a cheap alternative to fine-tuning | [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) |
| 7 | English benchmarks; specific models | Justifies reranking and limiting the number of chunks (RQ2) | Long contexts are not used uniformly | [doi:10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638) |
| 8 | Requires training a model with special tokens | Supports "retrieval on demand" — agentic RAG (H3) | Adaptive retrieval and self-critique improve quality | [arXiv:2310.11511](https://arxiv.org/abs/2310.11511) |
| 9 | LLM judges can be biased; English data | Main evaluation metrics for RQ2 | Automated RAG evaluation is feasible | [doi:10.18653/v1/2024.eacl-demo.16](https://doi.org/10.18653/v1/2024.eacl-demo.16) |
| 10 | Two domains; simulated users | Evaluation design with tasks, policies and repeated trials (RQ3) | Agents need better consistency and rule following | [OpenReview](https://openreview.net/forum?id=roNSXZpUDN) |
| 11 | Early-2023 systems; attacks evolve | Attack suite and guardrails (RQ4) | Retrieved content must be treated as untrusted | [doi:10.1145/3605764.3623985](https://doi.org/10.1145/3605764.3623985) |
| 12 | Fast-changing ecosystem; mostly analytical, limited empirical measurement | Direct basis for MCP integration and its threat model (RQ1, RQ4) | MCP needs security mechanisms and empirical study | [doi:10.1145/3796519](https://doi.org/10.1145/3796519) |

**Summary of methodologies and frameworks.** Most studies are *quantitative experiments* on benchmarks: training or prompting models and comparing configurations [@lewis2020; @karpukhin2020; @yao2023react; @schick2023; @asai2024]. A second group builds *benchmarks and evaluation frameworks* [@qin2024; @es2024; @yao2025tau]. Security work uses *threat modelling and demonstration attacks* [@greshake2023; @hou2026]. Conceptual frameworks include the agent architecture of profile–memory–planning–action modules [@wang2024survey] and the view of LLMs as "augmented language models" with reasoning and tools [@mialon2023]. Design-oriented research on complete platforms, as opposed to individual techniques, is rare.

# d. Gaps and unresolved issues

: Table 3 — Categorised research gaps

| Category | Gap identified in the reviewed literature | Evidence |
|-------------|-----------------------------------------------------------------|--------------|
| Theoretical | No agreed architectural model of an agent platform that unifies the loop, tools, retrieval, memory and guardrails; surveys describe components separately. | [@wang2024survey; @xi2025; @mialon2023] |
| Methodological | Evaluation is fragmented: different benchmarks and metrics; single runs despite non-determinism; cost and latency rarely reported together with quality. | [@liu2024agentbench; @yao2025tau; @es2024] |
| Methodological | LLM-as-a-judge metrics are used widely but their agreement with humans on domain data is seldom checked. | [@zheng2023; @es2024] |
| Data-related | Benchmarks are mostly English and Wikipedia-based; little evidence for Russian/Kazakh institutional documents. | [@lewis2020; @karpukhin2020; @liu2024lost] |
| Application-based | Benefits of the Model Context Protocol (integration effort, reliability) are claimed but not measured empirically. | [@hou2026; @anthropic2024mcp] |
| Application-based / security | Defences against indirect prompt injection in tool-using agents are not proven; MCP adds new attack surfaces. | [@greshake2023; @hou2026; @owasp2025llm] |
| Application-based | When retrieval should be a tool inside the loop (agentic RAG) rather than a fixed pre-step is unclear for real organisational tasks. | [@asai2024; @yao2023react] |

**Inconsistencies.** Dense retrieval clearly beats BM25 in some studies [@karpukhin2020], while sparse retrieval remains competitive in others and hybrid methods are recommended by surveys [@gao2023]. Reported agent success rates vary widely because tasks, tools and metrics differ [@liu2024agentbench; @yao2025tau]. Self-reflection improves success in some tasks [@shinn2023] but adds cost and is not always beneficial.

**Future research directions and multidisciplinary insights.** (1) Reference architectures validated by design-science evaluation; (2) standardised, repeated, cost-aware evaluation; (3) multilingual RAG for low-resource languages such as Kazakh; (4) security engineering (least privilege, isolation of untrusted content) applied to agents; (5) human–computer interaction research on trust, transparency of agent actions and human approval of tool calls.

# e. Organisation and presentation of the literature review

## e.1 Outline (thematic organisation)

1. Introduction — scope and relevance.
2. Theme 1: retrieval-augmented generation — from RAG to adaptive retrieval.
3. Theme 2: tool use and the agent loop — from ReAct and Toolformer to large-scale tool learning and reflection.
4. Theme 3: evaluation and reliability of RAG and agents.
5. Theme 4: security and the Model Context Protocol.
6. Gaps related to the research questions; conclusion.

## e.2 Literature review

**Introduction.** LLMs are powerful but limited by fixed training data and the inability to act. Two lines of research address these limits: retrieval of external knowledge and the use of external tools, combined in *agents* that repeatedly reason and act [@mialon2023; @wang2024survey]. This review covers 2020–2025 research relevant to designing a platform that integrates both through a standard protocol.

**Theme 1: Retrieval-augmented generation.** RAG combines a generator with a retriever over a document index and improves factuality on knowledge-intensive tasks [@lewis2020]. Dense retrieval with dual encoders can outperform term-matching methods such as BM25 [@karpukhin2020; @robertson2009], and approximate nearest-neighbour indexes make it scalable [@malkov2020; @johnson2021]. Surveys describe the evolution from "naive" to "advanced" and "modular" RAG with query rewriting, hybrid search and reranking [@gao2023; @fan2024]. Models, however, do not use long contexts uniformly [@liu2024lost], which motivates careful selection and ordering of retrieved passages. Self-RAG shows that retrieval can be triggered on demand and its results critiqued by the model [@asai2024].

**Theme 2: Tool use and the agent loop.** Chain-of-thought prompting showed that intermediate reasoning improves performance [@wei2022]; ReAct interleaves such reasoning with actions in a loop, grounding the model in external observations [@yao2023react]. Toolformer showed that a model can learn when to call tools [@schick2023], and ToolLLM scaled tool learning to thousands of real APIs, highlighting the need to retrieve relevant tools [@qin2024]. Reflexion added verbal self-reflection between attempts [@shinn2023]. Multi-agent frameworks compose several such agents [@wu2024]. In industry, these ideas are implemented through function-calling APIs, and MCP standardises how tools are described and called across clients [@mcp_spec].

**Theme 3: Evaluation and reliability.** Benchmarks show that agents still fail frequently: AgentBench reports a large gap between commercial and open models across interactive environments [@liu2024agentbench], and τ-bench shows that even the best tool-calling agents solve fewer than half of realistic tasks and are inconsistent across repeated trials [@yao2025tau]. For RAG, RAGAS proposes reference-free metrics of faithfulness and relevance [@es2024], and LLM-as-a-judge methods are popular but require validation against humans [@zheng2023].

**Theme 4: Security and MCP.** Retrieved documents and tool outputs can contain hidden instructions that hijack the model — indirect prompt injection [@greshake2023]. Industry guidance lists prompt injection, excessive agency and insecure output handling among the main risks of LLM applications [@owasp2025llm]. MCP, adopted rapidly since its release [@anthropic2024mcp], introduces risks across the server life cycle such as malicious servers and poisoned tool descriptions [@hou2026].

**Gaps related to the research questions.** For RQ-L1, the effect of standardised tool integration (MCP) on effort and reliability has not been measured. For RQ-L2, evaluations rarely combine quality, cost and repeated runs, and almost never use Russian/Kazakh institutional documents. For RQ-L3, defences against indirect prompt injection in MCP-based agents lack empirical evaluation.

# h. Conclusion of the literature review

**Overall trends.** Research has moved from retrieval-augmented models (2020) and reasoning-and-acting prompts (2022–2023) to large-scale tool learning, self-reflective agents, realistic benchmarks and, since 2024–2025, standard protocols and security of agent ecosystems. Recurring themes are the importance of retrieval quality, the fragility of multi-step tool use and the need for rigorous evaluation.

**Connection to the research questions and hypotheses.** The literature supports H2 (retrieval configuration matters; hybrid search and reranking are recommended), motivates H3 (retrieval on demand inside the loop) and H4 (untrusted content must be isolated), and shows that H1 (benefits of MCP) and the bilingual setting are open questions.

**Gaps and further study.** Missing are: an integrated, evaluated platform architecture; standardised, repeated and cost-aware evaluation; evidence for Russian/Kazakh documents; empirical evaluation of MCP; tested defences against prompt injection in tool-using agents.

**How the planned study fills the gaps — concrete steps.**

1. Build a reference platform: agent loop service, MCP client, MCP servers for documents, timetable, calendar and tickets, RAG service with BM25, dense and hybrid retrieval plus reranking, guardrails and full tracing.
2. Compare retrieval configurations on ≈ 300 bilingual questions with RAGAS-style metrics validated by human raters (H2).
3. Compare single-shot RAG with agentic RAG and loop variants (reflection, iteration limits, number of tools) on multi-step tasks, with 3 repeated runs and cost/latency reporting (H3).
4. Measure developer effort of MCP vs bespoke integration in a within-subject experiment (H1).
5. Run an attack suite of ≈ 200 indirect-injection cases with and without guardrails (H4); measure usability and acceptance (H5).

**Significance.** The review shows that the building blocks of agentic AI are well studied individually, but their integration into a secure, evaluable platform — especially through MCP and for non-English institutional data — is not. The planned study contributes a validated reference architecture and an evaluation protocol for this integration.

# References {.unnumbered}

::: {#refs}
:::
