---
author: Generated from the Zotero library export (output/zotero-library.json)
bibliography: /home/user/web-labaratoru-iitu/pw-04-citation-and-literature-review/output/zotero-library.json
csl: /home/user/web-labaratoru-iitu/common/csl/apa.csl
lang: en-US
subtitle: "Citation style: APA 7th edition"
title: "Agentic AI Platforms: Demonstration of Citation Management"
---

# From language models to agents

Large language models can solve new tasks from a few examples given in the prompt (Brown et al., 2020), and prompting them to produce intermediate reasoning steps further improves their performance (Wei et al., 2022). Surveys describe how such models are “augmented” with reasoning, retrieval and tools (Mialon et al., 2023) and how they become autonomous agents with planning, memory and action modules (Wang et al., 2024; Xi et al., 2025).

# Retrieval-augmented generation

Retrieval-augmented generation combines a generator with a retriever over a document index (Lewis et al., 2020), typically using dense passage retrieval (Karpukhin et al., 2020). Later work lets the model decide when to retrieve and critique its own output (Asai et al., 2024), while surveys summarise the growing family of RAG techniques (Fan et al., 2024). However, models do not use long contexts uniformly (N. F. Liu et al., 2024).

# Tools, the agent loop and evaluation

The ReAct pattern interleaves reasoning and actions in a loop (Yao et al., 2023); models can also learn when to call tools (Schick et al., 2023) and how to use thousands of real APIs (Patil et al., 2024; Qin et al., 2024). Verbal self-reflection helps agents recover from errors (Shinn et al., 2023). Benchmarks show that agents remain unreliable on realistic multi-step tasks (X. Liu et al., 2024; Yao et al., 2025), and RAG pipelines can be evaluated with automated metrics (Es et al., 2024).

# Security and the Model Context Protocol

Indirect prompt injection allows attackers to control LLM-integrated applications through retrieved data (Greshake et al., 2023), and the Model Context Protocol introduces new threats across the life cycle of tool servers (Hou et al., 2026).

# Bibliography {#bibliography .unnumbered}

Asai, A., Wu, Z., Wang, Y., Sil, A., & Hajishirzi, H. (2024). Self-RAG: Learning to retrieve, generate, and critique through self-reflection. *The Twelfth International Conference on Learning Representations (ICLR 2024)*. <https://arxiv.org/abs/2310.11511>

Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Askell, A., et al. (2020). Language models are few-shot learners. *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 1877–1901.

Es, S., James, J., Espinosa Anke, L., & Schockaert, S. (2024). RAGAs: Automated evaluation of retrieval augmented generation. *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: System Demonstrations*, 150–158. <https://doi.org/10.18653/v1/2024.eacl-demo.16>

Fan, W., Ding, Y., Ning, L., Wang, S., Li, H., Yin, D., Chua, T.-S., & Li, Q. (2024). A survey on RAG meeting LLMs: Towards retrieval-augmented large language models. *Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24)*, 6491–6501. <https://doi.org/10.1145/3637528.3671470>

Greshake, K., Abdelnabi, S., Mishra, S., Endres, C., Holz, T., & Fritz, M. (2023). Not what you’ve signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec ’23)*, 79–90. <https://doi.org/10.1145/3605764.3623985>

Hou, X., Zhao, Y., Wang, S., & Wang, H. (2026). Model Context Protocol (MCP): Landscape, security threats, and future research directions. *ACM Transactions on Software Engineering and Methodology*, *35*(10), Article 302. <https://doi.org/10.1145/3796519>

Karpukhin, V., Oguz, B., Min, S., Lewis, P., Wu, L., Edunov, S., Chen, D., & Yih, W. (2020). Dense passage retrieval for open-domain question answering. *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)*, 6769–6781. <https://doi.org/10.18653/v1/2020.emnlp-main.550>

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems 33 (NeurIPS 2020)*, 9459–9474. <https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html>

Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. *Transactions of the Association for Computational Linguistics*, *12*, 157–173. <https://doi.org/10.1162/tacl_a_00638>

Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., et al. (2024). AgentBench: Evaluating LLMs as agents. *The Twelfth International Conference on Learning Representations (ICLR 2024)*. <https://arxiv.org/abs/2308.03688>

Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., et al. (2023). Augmented language models: A survey. *Transactions on Machine Learning Research*. <https://openreview.net/forum?id=jh7wH2AzKK>

Patil, S. G., Zhang, T., Wang, X., & Gonzalez, J. E. (2024). Gorilla: Large language model connected with massive APIs. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, 126544–126565. <https://doi.org/10.52202/079017-4020>

Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., Lin, Y., Cong, X., Tang, X., Qian, B., et al. (2024). ToolLLM: Facilitating large language models to master 16000+ real-world APIs. *The Twelfth International Conference on Learning Representations (ICLR 2024)*. <https://arxiv.org/abs/2307.16789>

Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023). Toolformer: Language models can teach themselves to use tools. *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*. <https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html>

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *Advances in Neural Information Processing Systems 36 (NeurIPS 2023)*, 8634–8652. <https://doi.org/10.52202/075280-0377>

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., et al. (2024). A survey on large language model based autonomous agents. *Frontiers of Computer Science*, *18*(6), Article 186345. <https://doi.org/10.1007/s11704-024-40231-1>

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E. H., Le, Q. V., & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems 35 (NeurIPS 2022)*, 24824–24837. <https://proceedings.neurips.cc/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html>

Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., Zhang, M., Wang, J., Jin, S., Zhou, E., et al. (2025). The rise and potential of large language model based agents: A survey. *Science China Information Sciences*, *68*, Article 121101. <https://doi.org/10.1007/s11432-024-4222-0>

Yao, S., Shinn, N., Razavi, P., & Narasimhan, K. R. (2025). τ-bench: A benchmark for tool-agent-user interaction in real-world domains. *The Thirteenth International Conference on Learning Representations (ICLR 2025)*. <https://openreview.net/forum?id=roNSXZpUDN>

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *The Eleventh International Conference on Learning Representations (ICLR 2023)*. <https://openreview.net/forum?id=WE_vluYUL-X>
