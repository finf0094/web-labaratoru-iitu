# Appendix C. Evaluation dataset specification

| Dataset | Field | Type | Description |
|---------------|-----------------|-----------|----------------------------------------------------|
| Questions | `id`, `language` | string, enum (kk/ru/en) | Unique identifier; language of the question |
| Questions | `question`, `reference_answer` | text | Validated by two staff members |
| Questions | `source_passages` | list of document IDs + offsets | Ground truth for context recall |
| Questions | `type` | enum | single-fact / multi-step / unanswerable (system must refuse) |
| Tool tasks | `id`, `instruction` | text | Natural-language task given to the agent |
| Tool tasks | `required_tools`, `expected_state` | list, JSON | Tools that must be called; final state of the simulated back-end |
| Attack cases | `vector` | enum | retrieved document / tool output / tool description |
| Attack cases | `payload`, `goal` | text, enum | Injected instruction; attacker goal (forbidden tool call, data exfiltration, wrong answer) |
| Run log | `config_id`, `model`, `seed` | string | Experimental condition and pinned model version |
| Run log | `steps` | list | Each iteration: prompt tokens, completion tokens, tool name, arguments, result, latency |
| Run log | `outcome` | JSON | Final answer, success flag, metric scores, cost in USD |

Documents in the corpus are public university documents only; any document containing personal data is excluded.
