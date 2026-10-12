---
author: Generated from the Zotero library export (output/zotero-library.json)
bibliography: /home/user/web-labaratoru-iitu/pw-04-citation-and-literature-review/output/zotero-library.json
csl: /home/user/web-labaratoru-iitu/common/csl/chicago-notes-bibliography.csl
lang: en-US
subtitle: "Citation style: Chicago Manual of Style 17th ed. (notes and bibliography)"
title: "Agentic AI Platforms: Demonstration of Citation Management"
---

# From language models to agents

Large language models can solve new tasks from a few examples given in the prompt,[^1] and prompting them to produce intermediate reasoning steps further improves their performance.[^2] Surveys describe how such models are “augmented” with reasoning, retrieval and tools[^3] and how they become autonomous agents with planning, memory and action modules.[^4]

# Retrieval-augmented generation

Retrieval-augmented generation combines a generator with a retriever over a document index,[^5] typically using dense passage retrieval.[^6] Later work lets the model decide when to retrieve and critique its own output,[^7] while surveys summarise the growing family of RAG techniques.[^8] However, models do not use long contexts uniformly.[^9]

# Tools, the agent loop and evaluation

The ReAct pattern interleaves reasoning and actions in a loop;[^10] models can also learn when to call tools[^11] and how to use thousands of real APIs.[^12] Verbal self-reflection helps agents recover from errors.[^13] Benchmarks show that agents remain unreliable on realistic multi-step tasks,[^14] and RAG pipelines can be evaluated with automated metrics.[^15]

# Security and the Model Context Protocol

Indirect prompt injection allows attackers to control LLM-integrated applications through retrieved data,[^16] and the Model Context Protocol introduces new threats across the life cycle of tool servers.[^17]

# Bibliography {#bibliography .unnumbered}

Asai, Akari, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. “Self-RAG: Learning to Retrieve, Generate, and Critique Through Self-Reflection.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. <https://arxiv.org/abs/2310.11511>.

Brown, Tom B., Benjamin Mann, Nick Ryder, et al. “Language Models Are Few-Shot Learners.” *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, 1877–901.

Es, Shahul, Jithin James, Luis Espinosa Anke, and Steven Schockaert. “RAGAs: Automated Evaluation of Retrieval Augmented Generation.” *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations*, 2024, 150–58. <https://doi.org/10.18653/v1/2024.eacl-demo.16>.

Fan, Wenqi, Yujuan Ding, Liangbo Ning, et al. “A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models.” *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24)* (New York, NY), 2024, 6491–501. <https://doi.org/10.1145/3637528.3671470>.

Greshake, Kai, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario Fritz. “Not What You’ve Signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.” *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec ’23)* (New York, NY), 2023, 79–90. <https://doi.org/10.1145/3605764.3623985>.

Hou, Xinyi, Yanjie Zhao, Shenao Wang, and Haoyu Wang. “Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions.” *ACM Transactions on Software Engineering and Methodology* 35, no. 10 (2026): 302. <https://doi.org/10.1145/3796519>.

Karpukhin, Vladimir, Barlas Oguz, Sewon Min, et al. “Dense Passage Retrieval for Open-Domain Question Answering.” *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2020, 6769–81. <https://doi.org/10.18653/v1/2020.emnlp-main.550>.

Lewis, Patrick, Ethan Perez, Aleksandra Piktus, et al. “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.” *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, 9459–74. <https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html>.

Liu, Nelson F., Kevin Lin, John Hewitt, et al. “Lost in the Middle: How Language Models Use Long Contexts.” *Transactions of the Association for Computational Linguistics* 12 (2024): 157–73. <https://doi.org/10.1162/tacl_a_00638>.

Liu, Xiao, Hao Yu, Hanchen Zhang, et al. “AgentBench: Evaluating LLMs as Agents.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. <https://arxiv.org/abs/2308.03688>.

Mialon, Grégoire, Roberto Dessì, Maria Lomeli, et al. “Augmented Language Models: A Survey.” *Transactions on Machine Learning Research*, 2023. <https://openreview.net/forum?id=jh7wH2AzKK>.

Patil, Shishir G., Tianjun Zhang, Xin Wang, and Joseph E. Gonzalez. “Gorilla: Large Language Model Connected with Massive APIs.” *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, 2024, 126544–65. <https://doi.org/10.52202/079017-4020>.

Qin, Yujia, Shihao Liang, Yining Ye, et al. “ToolLLM: Facilitating Large Language Models to Master 16000+ Real-World APIs.” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024. <https://arxiv.org/abs/2307.16789>.

Schick, Timo, Jane Dwivedi-Yu, Roberto Dessì, et al. “Toolformer: Language Models Can Teach Themselves to Use Tools.” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023. <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>.

Shinn, Noah, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. “Reflexion: Language Agents with Verbal Reinforcement Learning.” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023, 8634–52. <https://doi.org/10.52202/075280-0377>.

Wang, Lei, Chen Ma, Xueyang Feng, et al. “A Survey on Large Language Model Based Autonomous Agents.” *Frontiers of Computer Science* 18, no. 6 (2024): 186345. <https://doi.org/10.1007/s11704-024-40231-1>.

Wei, Jason, Xuezhi Wang, Dale Schuurmans, et al. “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.” *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022, 24824–37. <https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html>.

Xi, Zhiheng, Wenxiang Chen, Xin Guo, et al. “The Rise and Potential of Large Language Model Based Agents: A Survey.” *Science China Information Sciences* 68 (2025): 121101. <https://doi.org/10.1007/s11432-024-4222-0>.

Yao, Shunyu, Noah Shinn, Pedram Razavi, and Karthik R. Narasimhan. “Τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains.” *The Thirteenth International Conference on Learning Representations (ICLR 2025)*, 2025. <https://openreview.net/forum?id=roNSXZpUDN>.

Yao, Shunyu, Jeffrey Zhao, Dian Yu, et al. “ReAct: Synergizing Reasoning and Acting in Language Models.” *The Eleventh International Conference on Learning Representations (ICLR 2023)*, 2023. <https://openreview.net/forum?id=WE_vluYUL-X>.

[^1]: Tom B. Brown et al., “Language Models Are Few-Shot Learners,” *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, 1877–901.

[^2]: Jason Wei et al., “Chain-of-Thought Prompting Elicits Reasoning in Large Language Models,” *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 2022, 24824–37, <https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html>.

[^3]: Grégoire Mialon et al., “Augmented Language Models: A Survey,” *Transactions on Machine Learning Research*, 2023, <https://openreview.net/forum?id=jh7wH2AzKK>.

[^4]: Lei Wang et al., “A Survey on Large Language Model Based Autonomous Agents,” *Frontiers of Computer Science* 18, no. 6 (2024): 186345, <https://doi.org/10.1007/s11704-024-40231-1>; Zhiheng Xi et al., “The Rise and Potential of Large Language Model Based Agents: A Survey,” *Science China Information Sciences* 68 (2025): 121101, <https://doi.org/10.1007/s11432-024-4222-0>.

[^5]: Patrick Lewis et al., “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks,” *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 2020, 9459–74, <https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html>.

[^6]: Vladimir Karpukhin et al., “Dense Passage Retrieval for Open-Domain Question Answering,” *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 2020, 6769–81, <https://doi.org/10.18653/v1/2020.emnlp-main.550>.

[^7]: Akari Asai et al., “Self-RAG: Learning to Retrieve, Generate, and Critique Through Self-Reflection,” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024, <https://arxiv.org/abs/2310.11511>.

[^8]: Wenqi Fan et al., “A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models,” *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24)* (New York, NY), 2024, 6491–501, <https://doi.org/10.1145/3637528.3671470>.

[^9]: Nelson F. Liu et al., “Lost in the Middle: How Language Models Use Long Contexts,” *Transactions of the Association for Computational Linguistics* 12 (2024): 157–73, <https://doi.org/10.1162/tacl_a_00638>.

[^10]: Shunyu Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models,” *The Eleventh International Conference on Learning Representations (ICLR 2023)*, 2023, <https://openreview.net/forum?id=WE_vluYUL-X>.

[^11]: Timo Schick et al., “Toolformer: Language Models Can Teach Themselves to Use Tools,” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023, <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>.

[^12]: Yujia Qin et al., “ToolLLM: Facilitating Large Language Models to Master 16000+ Real-World APIs,” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024, <https://arxiv.org/abs/2307.16789>; Shishir G. Patil et al., “Gorilla: Large Language Model Connected with Massive APIs,” *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, 2024, 126544–65, <https://doi.org/10.52202/079017-4020>.

[^13]: Noah Shinn et al., “Reflexion: Language Agents with Verbal Reinforcement Learning,” *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 2023, 8634–52, <https://doi.org/10.52202/075280-0377>.

[^14]: Xiao Liu et al., “AgentBench: Evaluating LLMs as Agents,” *The Twelfth International Conference on Learning Representations (ICLR 2024)*, 2024, <https://arxiv.org/abs/2308.03688>; Shunyu Yao et al., “Τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains,” *The Thirteenth International Conference on Learning Representations (ICLR 2025)*, 2025, <https://openreview.net/forum?id=roNSXZpUDN>.

[^15]: Shahul Es et al., “RAGAs: Automated Evaluation of Retrieval Augmented Generation,” *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations*, 2024, 150–58, <https://doi.org/10.18653/v1/2024.eacl-demo.16>.

[^16]: Kai Greshake et al., “Not What You’ve Signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection,” *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec ’23)* (New York, NY), 2023, 79–90, <https://doi.org/10.1145/3605764.3623985>.

[^17]: Xinyi Hou et al., “Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions,” *ACM Transactions on Software Engineering and Methodology* 35, no. 10 (2026): 302, <https://doi.org/10.1145/3796519>.
