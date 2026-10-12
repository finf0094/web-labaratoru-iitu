---
title: "Agentic AI Platforms: Demonstration of Citation Management"
author: "Generated from the Zotero library export (output/zotero-library.json)"
lang: en-US
---

# From language models to agents

Large language models can solve new tasks from a few examples given in the prompt [@brown2020], and prompting them to produce intermediate reasoning steps further improves their performance [@wei2022]. Surveys describe how such models are "augmented" with reasoning, retrieval and tools [@mialon2023] and how they become autonomous agents with planning, memory and action modules [@wang2024survey; @xi2025].

# Retrieval-augmented generation

Retrieval-augmented generation combines a generator with a retriever over a document index [@lewis2020], typically using dense passage retrieval [@karpukhin2020]. Later work lets the model decide when to retrieve and critique its own output [@asai2024], while surveys summarise the growing family of RAG techniques [@fan2024]. However, models do not use long contexts uniformly [@liu2024lost].

# Tools, the agent loop and evaluation

The ReAct pattern interleaves reasoning and actions in a loop [@yao2023react]; models can also learn when to call tools [@schick2023] and how to use thousands of real APIs [@qin2024; @patil2024]. Verbal self-reflection helps agents recover from errors [@shinn2023]. Benchmarks show that agents remain unreliable on realistic multi-step tasks [@liu2024agentbench; @yao2025tau], and RAG pipelines can be evaluated with automated metrics [@es2024].

# Security and the Model Context Protocol

Indirect prompt injection allows attackers to control LLM-integrated applications through retrieved data [@greshake2023], and the Model Context Protocol introduces new threats across the life cycle of tool servers [@hou2026].

# Bibliography {.unnumbered}

::: {#refs}
:::
