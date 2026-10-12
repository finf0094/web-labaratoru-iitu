---
author: Generated from the Zotero library export (output/zotero-library.json)
bibliography: /home/user/web-labaratoru-iitu/pw-04-citation-and-literature-review/output/zotero-library.json
csl: /home/user/web-labaratoru-iitu/common/csl/modern-language-association.csl
lang: en-US
subtitle: "Citation style: MLA 9th edition"
title: "Agentic AI Platforms: Demonstration of Citation Management"
---

# From language models to agents

Large language models can solve new tasks from a few examples given in the prompt (Brown et al.), and prompting them to produce intermediate reasoning steps further improves their performance (Wei et al.). Surveys describe how such models are “augmented” with reasoning, retrieval and tools (Mialon et al.) and how they become autonomous agents with planning, memory and action modules (Wang et al.; Xi et al.).

# Retrieval-augmented generation

Retrieval-augmented generation combines a generator with a retriever over a document index (Lewis et al.), typically using dense passage retrieval (Karpukhin et al.). Later work lets the model decide when to retrieve and critique its own output (Asai et al.), while surveys summarise the growing family of RAG techniques (Fan et al.). However, models do not use long contexts uniformly (N. F. Liu et al.).

# Tools, the agent loop and evaluation

The ReAct pattern interleaves reasoning and actions in a loop (Yao, Zhao, et al.); models can also learn when to call tools (Schick et al.) and how to use thousands of real APIs (Qin et al.; Patil et al.). Verbal self-reflection helps agents recover from errors (Shinn et al.). Benchmarks show that agents remain unreliable on realistic multi-step tasks (X. Liu et al.; Yao, Shinn, et al.), and RAG pipelines can be evaluated with automated metrics (Es et al.).

# Security and the Model Context Protocol

Indirect prompt injection allows attackers to control LLM-integrated applications through retrieved data (Greshake et al.), and the Model Context Protocol introduces new threats across the life cycle of tool servers (Hou et al.).

# Bibliography {#bibliography .unnumbered}

Asai, Akari, et al. “Self-RAG: Learning to Retrieve, Generate, and Critique Through Self-Reflection.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024, <https://arxiv.org/abs/2310.11511>.

Brown, Tom B., et al. “Language Models Are Few-Shot Learners.” *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, pp. 1877–901.

Es, Shahul, et al. “RAGAs: Automated Evaluation of Retrieval Augmented Generation.” *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations*, 2024, pp. 150–58, <https://doi.org/10.18653/v1/2024.eacl-demo.16>.

Fan, Wenqi, et al. “A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models.” *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24)* \[New York, NY\], 2024, pp. 6491–501, <https://doi.org/10.1145/3637528.3671470>.

Greshake, Kai, et al. “Not What You’ve Signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.” *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec ’23)* \[New York, NY\], 2023, pp. 79–90, <https://doi.org/10.1145/3605764.3623985>.

Hou, Xinyi, et al. “Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions.” *ACM Transactions on Software Engineering and Methodology*, vol. 35, no. 10, 302, 2026, <https://doi.org/10.1145/3796519>.

Karpukhin, Vladimir, et al. “Dense Passage Retrieval for Open-Domain Question Answering.” *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2020, pp. 6769–81, <https://doi.org/10.18653/v1/2020.emnlp-main.550>.

Lewis, Patrick, et al. “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.” *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, pp. 9459–74, <https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html>.

Liu, Nelson F., et al. “Lost in the Middle: How Language Models Use Long Contexts.” *Transactions of the Association for Computational Linguistics*, vol. 12, 2024, pp. 157–73, <https://doi.org/10.1162/tacl_a_00638>.

Liu, Xiao, et al. “AgentBench: Evaluating LLMs as Agents.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024, <https://arxiv.org/abs/2308.03688>.

Mialon, Grégoire, et al. “Augmented Language Models: A Survey.” *Transactions on Machine Learning Research*, 2023, <https://openreview.net/forum?id=jh7wH2AzKK>.

Patil, Shishir G., et al. “Gorilla: Large Language Model Connected with Massive APIs.” *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, 2024, pp. 126544–65, <https://doi.org/10.52202/079017-4020>.

Qin, Yujia, et al. “ToolLLM: Facilitating Large Language Models to Master 16000+ Real-World APIs.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024, <https://arxiv.org/abs/2307.16789>.

Schick, Timo, et al. “Toolformer: Language Models Can Teach Themselves to Use Tools.” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023, <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>.

Shinn, Noah, et al. “Reflexion: Language Agents with Verbal Reinforcement Learning.” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023, pp. 8634–52, <https://doi.org/10.52202/075280-0377>.

Wang, Lei, et al. “A Survey on Large Language Model Based Autonomous Agents.” *Frontiers of Computer Science*, vol. 18, no. 6, 186345, 2024, <https://doi.org/10.1007/s11704-024-40231-1>.

Wei, Jason, et al. “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.” *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022, pp. 24824–37, <https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html>.

Xi, Zhiheng, et al. “The Rise and Potential of Large Language Model Based Agents: A Survey.” *Science China Information Sciences*, vol. 68, 121101, 2025, <https://doi.org/10.1007/s11432-024-4222-0>.

Yao, Shunyu, Jeffrey Zhao, et al. “ReAct: Synergizing Reasoning and Acting in Language Models.” *The Eleventh International Conference on Learning Representations (ICLR 2023)*, 2023, <https://openreview.net/forum?id=WE_vluYUL-X>.

Yao, Shunyu, Noah Shinn, et al. “Τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.” *The Thirteenth International Conference on Learning Representations (ICLR 2025)*, 2025, <https://openreview.net/forum?id=roNSXZpUDN>.
