---
title: "Laboratory Work 1. Review and Analysis of the Subject Area of the Research (Development)"
subtitle: "Topic: Design and Evaluation of an Agentic AI Platform Integrating the Agent Loop, Model Context Protocol (MCP) Tools and Retrieval-Augmented Generation (RAG)"
author: "Student: Kulush Askhat  ·  Group: IT1CCO-2402IS  ·  Instructor: ____________________"
date: "International Information Technology University (IITU), Almaty, 2026"
lang: en-US
abstract: |
  The subject area of agentic AI platforms is examined: systems in which a large language model (LLM) works in an agent loop, calls external tools — increasingly through the Model Context Protocol (MCP) — and answers from organisational documents using retrieval-augmented generation (RAG). The main elements of the subject area are described and the main problem is identified: the lack of an open, measurable and secure way to combine these components for organisations, especially with Kazakh- and Russian-language data. Five analogues are reviewed: ISSAI KazLLM and Oylan (Kazakhstan), the OpenAI agent platform (USA), Microsoft Foundry Agent Service and Copilot Studio (USA), LangChain/LangGraph (USA) and Dify (USA). The analogues are classified by origin, business model, deployment and purpose and compared using five criteria. **Keywords:** AI agents, agent loop, Model Context Protocol, tool calling, retrieval-augmented generation, AI platform, comparative analysis.
---

# Aim and objectives

**Aim of the work:** to study the subject area of the selected research, identify its main elements and the existing problem, and apply the methods of analysis, comparison and classification to examine existing analogous solutions.

**Objectives:** (1) select a research topic; (2) define the subject area; (3) describe its main elements; (4) identify the existing problem; (5) find and describe five analogues; (6) classify them; (7) carry out a comparative analysis; (8) formulate conclusions.

**Research methods used:** *analysis* — the subject area is divided into objects, processes, participants and data (Table 1); *synthesis* — the findings are combined into a single problem statement (Section 2.2); *comparison* — the analogues are compared by five criteria (Table 4); *classification* — the analogues are grouped by common characteristics (Table 3).

# 1. Task 1. Selection of the research topic

**Selected topic (diploma project topic):** *Design and Evaluation of an Agentic AI Platform Integrating the Agent Loop, Model Context Protocol (MCP) Tools and Retrieval-Augmented Generation (RAG).*

The topic concerns the **development of a software platform** and the **investigation of technologies**: an LLM runs in an agent loop (reason → call a tool → observe the result → continue) [@yao2023react; @wang2024survey]; tools and data sources are connected through the open Model Context Protocol [@anthropic2024mcp; @mcp_spec]; and answers are grounded in organisational documents through RAG [@lewis2020]. The platform is intended for organisations such as universities and small and medium-sized enterprises in Kazakhstan.

# 2. Task 2. Description of the subject area

## 2.1 Main elements

The subject area is the **design and operation of LLM-based agent systems in organisations**. An *agent loop* repeatedly calls the model; when the model requests a *tool* (a function described by a name, a natural-language description and a JSON schema), the platform executes it and returns the result to the model. In MCP, a *host* application contains *clients* that connect to *servers*; servers expose tools, resources and prompts in a standard way, so one server can be reused by many applications [@mcp_spec; @hou2026]. A *RAG pipeline* splits documents into chunks, converts them into vectors (embeddings), stores them in an index and retrieves the most relevant chunks for each query [@lewis2020; @gao2023].

: Table 1 — Main elements of the subject area

| Element | Description |
|----------------|--------------------------------------------------------------------------|
| Field of activity | Applied artificial intelligence and software engineering of LLM-based information systems; digital services of universities, businesses and public bodies. |
| Main objects | LLM (commercial API model or open-weight model); agent; agent loop; tool; MCP host, client and server; RAG pipeline (document, chunk, embedding, vector index, retriever, reranker); knowledge base; conversation session; guardrail/policy; execution trace; evaluation dataset. |
| Main processes | Ingestion and indexing of documents; handling a user request; retrieval of relevant chunks; reasoning and planning; tool selection and invocation; observation of tool results; human approval of risky actions; generation of the final answer with sources; tracing and logging; connecting a new tool (developing/registering an MCP server); evaluation of quality, cost and latency; updating knowledge and models. |
| Participants or users | End users (students, employees, customers); developers and AI engineers; knowledge owners (departments that maintain documents); IT and security administrators; management; providers of models, tools and MCP servers. |
| Data used | Documents (PDF, DOCX, web pages) in Kazakh, Russian and English; embeddings; tool schemas (JSON Schema); tool inputs and outputs; conversation history; traces and logs; evaluation questions and reference answers; token usage, cost and latency metrics; access policies. |
| Information systems currently applied | General chat assistants used ad hoc; vendor agent platforms (OpenAI, Microsoft Foundry); open-source frameworks (LangChain/LangGraph) and low-code platforms (Dify); domestic LLMs and assistants (ISSAI KazLLM/Oylan, AlemLLM, eGov GPT). |
| Existing problem | Tools and data are integrated separately for each vendor; RAG pipelines are built ad hoc; agents are unreliable on multi-step tasks; quality, cost and security are rarely measured together; tool-using agents are exposed to prompt injection; support for Kazakh-language data and on-premise deployment is limited. |

## 2.2 Existing scientific and practical problem

*Practical problem.* Organisations adopt AI quickly but struggle to move from experiments to production: according to a 2025 global survey, most organisations already use AI in at least one business function, but only a minority are scaling AI agents [@singla2025]. In Kazakhstan, the state promotes AI through the Concept for the development of artificial intelligence for 2024–2029 [@kz2024aiconcept] and the Law "On Artificial Intelligence" adopted in November 2025 [@kz2025ailaw; @omirgazy2025]; government services are already delivered through an LLM-based assistant [@birbayeva2026]. Universities and SMEs, however, have no open reference platform that connects LLMs to their documents and systems in a controlled way.

*Scientific problem.* RAG improves factuality [@lewis2020], tool use extends what models can do [@yao2023react; @schick2023], and MCP standardises tool integration and has been widely adopted since 2024 — it is now governed by the Agentic AI Foundation of the Linux Foundation [@anthropic2025aaif; @lf2025aaif]. Yet agents remain unreliable on realistic tasks [@yao2025tau; @liu2024agentbench], tool-using systems are vulnerable to indirect prompt injection [@greshake2023], MCP introduces new threats [@hou2026], and evidence for Kazakh-language data is scarce [@togmanov2025].

**Problem statement (synthesis):** *there is no open, model-agnostic platform — with an evaluated reference architecture — that combines an agent loop, MCP-based tools and RAG over Kazakh/Russian/English organisational documents, and that measures task success, answer faithfulness, integration effort, cost and security together.*

# 3. Task 3. Review of existing analogues

Five analogues were selected: one domestic and four international solutions, covering a national LLM and assistant, two commercial cloud agent platforms, an open-source developer framework and an open-source low-code platform.

**Analogue 1 — ISSAI KazLLM and Oylan** (Kazakhstan). Developed by the Institute of Smart Systems and Artificial Intelligence (ISSAI) of Nazarbayev University, Astana. Purpose: national language models and an AI assistant for Kazakh, Russian and English. KazLLM was released on 10 December 2024 in 8B and 70B versions based on Llama 3.1, trained on more than 150 billion tokens in Kazakh, Russian, English and Turkish; the weights are published under a non-commercial licence [@issai2024kazllm; @hf_kazllm; @nakispekova2024]. Oylan is a multimodal assistant (text, speech, images); its third version, presented in December 2025, adds web search, reasoning and RAG and is available through an API and a playground [@issai2025oylan]. Target users: citizens, researchers, developers, organisations. Information about MCP support or tools for building custom agents was not found.

**Analogue 2 — OpenAI agent platform** (USA). Developed by OpenAI. Purpose: building agents on OpenAI models. The Responses API and the open-source Agents SDK (March 2025) provide built-in web search, file search and computer use, multi-agent handoffs, guardrails and tracing [@openai2025newtools]; MCP is supported in the Agents SDK and, since May 2025, as remote MCP servers in the Responses API [@openai_agentssdk; @openai2025responses; @wiggers2025openai]. File search uses hosted vector stores for RAG. AgentKit (October 2025) added a visual Agent Builder, ChatKit and evaluation tools [@openai2025agentkit]; OpenAI states that Agent Builder and Evals will no longer be available from 30 November 2026 [@openai_agentbuilder]. Target users: developers and companies. Access: cloud service, pay-per-token.

**Analogue 3 — Microsoft Foundry Agent Service and Copilot Studio** (USA). Developed by Microsoft. Purpose: enterprise agents on Azure. Foundry Agent Service became generally available in May 2025 [@ms2025foundryga]; it offers tools such as web search, file search, code interpreter, functions, OpenAPI tools, MCP and Azure AI Search [@ms_foundry_overview]; at Ignite 2025 the platform was renamed Microsoft Foundry and knowledge grounding (Foundry IQ) and multi-agent workflows were added [@ms2025foundryignite]. Copilot Studio, the low-code tool, made MCP generally available on 29 May 2025 [@ms2025copilotmcp]. Target users: enterprises, developers, citizen developers. Access: Azure cloud, payment for model tokens and tools.

**Analogue 4 — LangChain / LangGraph** (USA). Developed by LangChain, Inc. Purpose: open-source framework for building stateful agents and RAG applications in Python and JavaScript/TypeScript. LangGraph 1.0 was released on 22 October 2025 [@langchain2025lg1]; MCP servers are connected through the open-source `langchain-mcp-adapters` library [@langchain_mcpadapters]; RAG is built from retriever and vector-store components; LangSmith provides tracing, evaluation and deployment, with a free developer tier [@langsmith]. Target users: developers. Access: open source, self-hosted or managed cloud; works with any model provider.

**Analogue 5 — Dify** (USA). Developed by LangGenius, Inc. Purpose: open-source low-code platform for LLM applications and agents. Main functions: visual workflow and agent builder, RAG knowledge base and pipeline, plugin marketplace, logging; since version 1.6.0 (July 2025) Dify both calls external MCP servers and publishes its own applications as MCP servers [@dify2025mcp]. Licence: Dify Open Source License (Apache 2.0 with additional conditions, e.g. a commercial licence is needed for multi-tenant SaaS) [@dify_license]; cloud plans from a free sandbox to paid team plans, or self-hosting [@dify_pricing]. Target users: developers, product teams, non-programmers.

: Table 2 — General description of the analogues

| No. | Name | Developer and country | Purpose | Main functions | Source |
|------|----------------|------------|--------------|-----------------------------|----------|
| 1 | ISSAI KazLLM and Oylan | ISSAI, Nazarbayev University, Kazakhstan | National LLMs and AI assistant for Kazakh, Russian, English | 8B/70B open-weight models (non-commercial); multimodal assistant with web search, reasoning, RAG; API and playground | [@issai2024kazllm; @issai2025oylan; @hf_kazllm] |
| 2 | OpenAI agent platform (Responses API, Agents SDK, AgentKit) | OpenAI, USA | Building agents on OpenAI models | Agent loop, handoffs, guardrails, tracing; web/file search; remote MCP; vector stores; visual builder (until Nov 2026) | [@openai2025newtools; @openai2025responses; @openai2025agentkit] |
| 3 | Microsoft Foundry Agent Service, Copilot Studio | Microsoft, USA | Enterprise agents on Azure | Agent service with tools (search, code, OpenAPI, MCP); Azure AI Search / Foundry IQ grounding; multi-agent workflows; low-code builder with MCP | [@ms2025foundryga; @ms2025foundryignite; @ms2025copilotmcp] |
| 4 | LangChain / LangGraph (+ LangSmith) | LangChain, Inc., USA | Open-source framework for agents and RAG | Stateful graph-based agent loop; MCP adapters; retrievers and vector stores; tracing and evaluation | [@langchain2025lg1; @langchain_mcpadapters; @langsmith] |
| 5 | Dify | LangGenius, Inc., USA | Open-source low-code LLM app and agent platform | Visual workflows and agents; knowledge base (RAG); plugins; two-way MCP; logging | [@dify2025mcp; @dify_license; @dify_pricing] |

# 4. Task 4. Classification of the analogues

The analogues were classified by origin, business model, deployment, maturity and purpose; an additional criterion is the *level of abstraction* (model/assistant, cloud platform, code framework, low-code platform).

: Table 3 — Classification of the analogues

| Name of the analogue | Category | Basis for classification |
|------------------|------------------------------|----------------------------------------|
| ISSAI KazLLM and Oylan | Domestic; non-commercial research development (open weights, non-commercial licence); cloud assistant + locally deployable models; operational assistant, research-driven models; specialised (Kazakh-language AI) | Created by a university institute; focus on national languages; level: model and assistant |
| OpenAI agent platform | International; commercial; cloud; operational; general-purpose agent platform | Proprietary models and hosted tools billed per use; open-source SDK; level: cloud platform |
| Microsoft Foundry / Copilot Studio | International; commercial; cloud; operational; general-purpose enterprise platform | Azure services with enterprise integration; level: cloud platform + low-code |
| LangChain / LangGraph | International; open-source (with commercial LangSmith services); local or cloud; operational; general-purpose developer framework | MIT-licensed libraries; model-agnostic; level: code framework |
| Dify | International; open-source with licence restrictions and paid cloud plans; local or cloud; operational; general-purpose low-code platform | Self-hostable; visual builder; level: low-code platform |

**Summary of classification:** one domestic and four international solutions; two commercial cloud platforms (OpenAI, Microsoft), two open-source, self-hostable solutions (LangGraph, Dify) and one national research-driven solution (ISSAI). Four of five are general-purpose agent platforms; the domestic one is specialised in Kazakh-language AI rather than agent building.

# 5. Task 5. Comparative analysis of the analogues

Five comparison criteria were chosen according to the goal of the future platform: (1) agent loop and orchestration, (2) tool integration through MCP, (3) built-in RAG / knowledge base, (4) observability, evaluation and guardrails, (5) access conditions, local deployment and Kazakh-language support.

: Table 4 — Comparative analysis of the analogues ("+" available, "–" not available, "±" partially available, "No data" — reliable information not found)

| Criterion | ISSAI KazLLM / Oylan | OpenAI platform | Microsoft Foundry / Copilot Studio | LangChain / LangGraph | Dify |
|--------------|-------------|-------------|-------------|-------------|-------------|
| 1. Agent loop and orchestration | ± (assistant with reasoning and web search; no agent builder documented) | + (Agents SDK, handoffs) | + (agents, multi-agent workflows) | + (stateful graphs, multi-agent) | + (visual workflows and agents) |
| 2. Tool integration through MCP | No data | + (Agents SDK; remote MCP in Responses API) | + (MCP tool; Copilot Studio GA) | + (MCP adapters) | + (client and server, two-way) |
| 3. Built-in RAG / knowledge base | ± (RAG inside the assistant; no user knowledge base documented) | + (file search, vector stores) | + (file search, Azure AI Search, Foundry IQ) | ± (components; assembled by the developer) | + (knowledge base and pipeline) |
| 4. Observability, evaluation, guardrails | No data | + (tracing, guardrails; Evals UI discontinued from 30 Nov 2026) | ± (tracing, enterprise controls) | + (LangSmith tracing and evaluation) | ± (application logs) |
| 5. Access, local deployment, Kazakh language | + Kazakh; open weights but non-commercial | Paid cloud; no on-premise; model-dependent Kazakh quality | Paid Azure cloud; no on-premise | Free, self-hosted, any model (incl. local) | Free self-hosted (licence limits) or paid cloud; any model |

**1. Common characteristics.** All analogues use LLMs as the reasoning core, provide some form of tool use or web search, and support retrieval over documents. Four of five support MCP, which confirms that MCP has become the de facto standard for tool integration [@wiggers2025openai; @wiggers2025google].

**2. Main differences.** They differ in level of abstraction (model vs platform vs framework), business model (commercial cloud vs open source), deployment (cloud-only vs self-hosted), and in how much of RAG and evaluation is built in.

**3. Broadest range of functions.** The commercial platforms — OpenAI and Microsoft Foundry — provide the widest set of built-in components (agent loop, hosted tools, RAG, MCP, tracing); among open solutions, the combination of LangGraph and LangSmith offers the most complete developer tooling, and Dify offers the most complete low-code environment.

**4. Identified limitations.** (a) Cloud platforms lock users into one vendor and require sending data abroad, which conflicts with data-protection requirements [@kz2013pdlaw]; (b) platform features change quickly (e.g. discontinuation of Agent Builder), creating dependency risks; (c) evaluation of quality, cost and security is not provided as a unified, reproducible methodology; (d) protection against prompt injection through retrieved content and tools is left to the developer [@greshake2023; @owasp2025llm]; (e) the domestic solution focuses on language models and an assistant, not on an open agent platform with MCP; (f) open frameworks require significant engineering effort to assemble a secure end-to-end solution.

# 6. Task 6. Conclusion

The subject area covers LLM-based agent systems that reason in a loop, call tools — increasingly through the Model Context Protocol — and answer from organisational documents using RAG. The main problem is the lack of an open, model-agnostic platform with an evaluated architecture that combines these components securely and supports Kazakh- and Russian-language data. Five analogues were analysed. Classification showed one domestic research-driven solution (ISSAI KazLLM/Oylan), two commercial cloud platforms (OpenAI, Microsoft Foundry) and two open-source solutions (LangGraph, Dify). The comparison showed that commercial platforms offer the richest built-in functions but create vendor lock-in and data-residency issues; open-source tools are flexible and self-hostable but require assembly and lack a unified evaluation method; the domestic solution offers strong Kazakh-language models but no open agent-building platform. Useful features for the future project are: the Agents SDK pattern of an agent loop with guardrails and tracing, MCP as the single integration layer (as in Dify's two-way support), LangSmith-style tracing and evaluation, built-in knowledge bases, and the possibility to plug in national models such as KazLLM for on-premise deployment.

# References {.unnumbered}

::: {#refs}
:::
