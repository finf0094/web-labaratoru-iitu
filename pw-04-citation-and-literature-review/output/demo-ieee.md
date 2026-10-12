---
author: Generated from the Zotero library export (output/zotero-library.json)
bibliography: /home/user/web-labaratoru-iitu/pw-04-citation-and-literature-review/output/zotero-library.json
csl: /home/user/web-labaratoru-iitu/common/csl/ieee.csl
lang: en-US
subtitle: "Citation style: IEEE"
title: "Agentic AI Platforms: Demonstration of Citation Management"
---

# From language models to agents

Large language models can solve new tasks from a few examples given in the prompt \[1\], and prompting them to produce intermediate reasoning steps further improves their performance \[2\]. Surveys describe how such models are “augmented” with reasoning, retrieval and tools \[3\] and how they become autonomous agents with planning, memory and action modules \[4\], \[5\].

# Retrieval-augmented generation

Retrieval-augmented generation combines a generator with a retriever over a document index \[6\], typically using dense passage retrieval \[7\]. Later work lets the model decide when to retrieve and critique its own output \[8\], while surveys summarise the growing family of RAG techniques \[9\]. However, models do not use long contexts uniformly \[10\].

# Tools, the agent loop and evaluation

The ReAct pattern interleaves reasoning and actions in a loop \[11\]; models can also learn when to call tools \[12\] and how to use thousands of real APIs \[13\], \[14\]. Verbal self-reflection helps agents recover from errors \[15\]. Benchmarks show that agents remain unreliable on realistic multi-step tasks \[16\], \[17\], and RAG pipelines can be evaluated with automated metrics \[18\].

# Security and the Model Context Protocol

Indirect prompt injection allows attackers to control LLM-integrated applications through retrieved data \[19\], and the Model Context Protocol introduces new threats across the life cycle of tool servers \[20\].

# Bibliography {#bibliography .unnumbered}

\[1\] T. B. Brown *et al.*, “Language models are few-shot learners,” in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, Curran Associates, 2020, pp. 1877–1901.

\[2\] J. Wei *et al.*, “Chain-of-thought prompting elicits reasoning in large language models,” in *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, Curran Associates, 2022, pp. 24824–24837. Available: <https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html>

\[3\] G. Mialon *et al.*, “Augmented language models: A survey,” *Transactions on Machine Learning Research*, 2023, Available: <https://openreview.net/forum?id=jh7wH2AzKK>

\[4\] L. Wang *et al.*, “A survey on large language model based autonomous agents,” *Frontiers of Computer Science*, vol. 18, no. 6, Art. no. 186345, 2024, doi: [10.1007/s11704-024-40231-1](https://doi.org/10.1007/s11704-024-40231-1).

\[5\] Z. Xi *et al.*, “The rise and potential of large language model based agents: A survey,” *Science China Information Sciences*, vol. 68, Art. no. 121101, 2025, doi: [10.1007/s11432-024-4222-0](https://doi.org/10.1007/s11432-024-4222-0).

\[6\] P. Lewis *et al.*, “Retrieval-augmented generation for knowledge-intensive NLP tasks,” in *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, Curran Associates, 2020, pp. 9459–9474. Available: <https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html>

\[7\] V. Karpukhin *et al.*, “Dense passage retrieval for open-domain question answering,” in *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, Association for Computational Linguistics, 2020, pp. 6769–6781. doi: [10.18653/v1/2020.emnlp-main.550](https://doi.org/10.18653/v1/2020.emnlp-main.550).

\[8\] A. Asai, Z. Wu, Y. Wang, A. Sil, and H. Hajishirzi, “Self-RAG: Learning to retrieve, generate, and critique through self-reflection,” in *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. Available: <https://arxiv.org/abs/2310.11511>

\[9\] W. Fan *et al.*, “A survey on RAG meeting LLMs: Towards retrieval-augmented large language models,” in *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24)*, New York, NY: ACM, 2024, pp. 6491–6501. doi: [10.1145/3637528.3671470](https://doi.org/10.1145/3637528.3671470).

\[10\] N. F. Liu *et al.*, “Lost in the middle: How language models use long contexts,” *Transactions of the Association for Computational Linguistics*, vol. 12, pp. 157–173, 2024, doi: [10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638).

\[11\] S. Yao *et al.*, “ReAct: Synergizing reasoning and acting in language models,” in *The Eleventh International Conference on Learning Representations (ICLR 2023)*, 2023. Available: <https://openreview.net/forum?id=WE_vluYUL-X>

\[12\] T. Schick *et al.*, “Toolformer: Language models can teach themselves to use tools,” in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, Curran Associates, 2023. Available: <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>

\[13\] Y. Qin *et al.*, “ToolLLM: Facilitating large language models to master 16000+ real-world APIs,” in *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. Available: <https://arxiv.org/abs/2307.16789>

\[14\] S. G. Patil, T. Zhang, X. Wang, and J. E. Gonzalez, “Gorilla: Large language model connected with massive APIs,” in *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, Curran Associates, 2024, pp. 126544–126565. doi: [10.52202/079017-4020](https://doi.org/10.52202/079017-4020).

\[15\] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao, “Reflexion: Language agents with verbal reinforcement learning,” in *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, Curran Associates, 2023, pp. 8634–8652. doi: [10.52202/075280-0377](https://doi.org/10.52202/075280-0377).

\[16\] X. Liu *et al.*, “AgentBench: Evaluating LLMs as agents,” in *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. Available: <https://arxiv.org/abs/2308.03688>

\[17\] S. Yao, N. Shinn, P. Razavi, and K. R. Narasimhan, “τ-bench: A benchmark for tool-agent-user interaction in real-world domains,” in *The Thirteenth International Conference on Learning Representations (ICLR 2025)*, 2025. Available: <https://openreview.net/forum?id=roNSXZpUDN>

\[18\] S. Es, J. James, L. Espinosa Anke, and S. Schockaert, “RAGAs: Automated evaluation of retrieval augmented generation,” in *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations*, Association for Computational Linguistics, 2024, pp. 150–158. doi: [10.18653/v1/2024.eacl-demo.16](https://doi.org/10.18653/v1/2024.eacl-demo.16).

\[19\] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz, “Not what you’ve signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection,” in *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec ’23)*, New York, NY: ACM, 2023, pp. 79–90. doi: [10.1145/3605764.3623985](https://doi.org/10.1145/3605764.3623985).

\[20\] X. Hou, Y. Zhao, S. Wang, and H. Wang, “Model Context Protocol (MCP): Landscape, security threats, and future research directions,” *ACM Transactions on Software Engineering and Methodology*, vol. 35, no. 10, Art. no. 302, 2026, doi: [10.1145/3796519](https://doi.org/10.1145/3796519).
