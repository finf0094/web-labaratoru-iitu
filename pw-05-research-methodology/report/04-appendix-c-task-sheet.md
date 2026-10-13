# Appendix C. Developer task sheet and benchmark specification

## C.1. Developer task sheet (given to participants)

**Your goal.** Connect three tools to an AI agent so that all acceptance tests pass, first in **App 1** (a command-line LangGraph agent) and then in **App 2** (a FastAPI chat service in a separate repository with its own agent). You will do this twice: once with **native LangChain tools** (`@tool` functions inside the application) and once with an **MCP server** (the tools live in a separate server that both applications connect to). The order and the tool set are given on your personal card. Time limit: **40 minutes per condition.**

**What is prepared for you.** A repository with the two applications, a mock back-end service (FastAPI, synthetic data) with documented HTTP endpoints, the model endpoint (OpenAI-compatible API, already configured), pytest acceptance tests and a short "cheat sheet" for `@tool`, the `mcp` SDK and `langchain-mcp-adapters`.

| Tool (set A) | Equivalent (set B) | What it does | Arguments → result |
|------------------|------------------|----------------------------|----------------------------|
| `get_timetable` | `get_exam_schedule` | Returns the classes (exams) of a group on a date | `group: str`, `date: YYYY-MM-DD` → list of entries |
| `create_ticket` | `book_room` | Creates an IT help-desk ticket (books a room) in the mock service | `title: str`, `description: str`, `priority: low/normal/high` (`room: str`, `start`, `end`) → id |
| `search_documents` | `search_news` | Keyword search over a small set of university regulations (news) | `query: str`, `limit: int = 3` → titles and short snippets |

**Rules.** You may use the documentation and the cheat sheet; do not use AI coding assistants; say aloud what you are doing (think-aloud). Tell the observer when you think you are done — the work counts as **done** only when `pytest` shows all tests green.

**Acceptance tests (for each application).**

1. Each tool is visible to the agent with a name, a one-sentence description and a JSON schema of arguments.
2. Calling each tool directly with valid arguments returns the expected result from the mock service.
3. Invalid arguments (e.g. a wrong date format) return a clear error message instead of crashing the agent.
4. Three scripted agent requests ("What classes does group SE-2203 have on 3 March?", "Create a high-priority ticket: projector in room 305 is broken", "Find the rule about retaking exams") result in the correct tool call and a correct final state of the mock service.

**What is measured (automatically, you do not need to do anything).**

| Measure | How it is obtained |
|------------------|--------------------------------------------------------|
| Time to done, App 1 and App 2 | Timestamps of the first edit and of the first all-green pytest run (logged by the test runner) |
| Lines of code | `git diff --stat` of your changes, excluding tests and configuration of the starter repository |
| Failed test runs | Number of pytest runs with at least one failing test |
| Problems observed | Observer's think-aloud notes (category and minute) |
| Usability | Questionnaire (Appendix B) after each condition |

## C.2. Benchmark task suite (agent experiment, RQ2)

**Tools available to the agent.** *5-tool condition:* `get_timetable`, `get_exam_schedule`, `create_ticket`, `book_room`, `search_documents`. *20-tool condition:* the same 5 plus 15 plausible "distractor" tools from the same domains (e.g. `get_teacher_contacts`, `update_ticket`, `cancel_booking`, `list_rooms`, `search_news`, `get_canteen_menu`). In the **native** condition the tools are `@tool` functions; in the **MCP** condition exactly the same functions, names, descriptions and schemas are exposed by an MCP server and loaded with `MultiServerMCPClient` (stdio transport).

| Task type | Example instruction | Expected behaviour | Tasks |
|--------------|--------------------------------|------------------------------|--------|
| Single tool | "Show the timetable of group SE-2203 for 3 March 2027." | `get_timetable(group="SE-2203", date="2027-03-03")` | 40 |
| Two tools in sequence | "Book a room for the make-up class of SE-2203 right after their last class on Friday." | `get_timetable` → `book_room` with the computed time | 30 |
| Argument extraction | "The projector in 305 is dead again and the lecture starts in 10 minutes!" | `create_ticket` with priority `high` and room in the description | 30 |
| No tool needed | "What does MCP stand for?" | No tool call; direct answer | 20 |
| **Total** | 5 domains: timetable, exams, help desk, rooms, documents | | **120** |

**Format of one task (JSON).**

| Field | Type | Description |
|----------------|-----------|----------------------------------------------------|
| `id`, `type`, `domain` | string, enum | Unique identifier; task type and domain (for stratification) |
| `instruction` | text | Natural-language request given to the agent |
| `expected_calls` | list | Tool names with expected argument values (exact or normalised, e.g. dates) |
| `expected_state` | JSON | Final state of the mock service (e.g. a ticket with given fields exists) |
| `notes` | text | Who wrote and who validated the task |

**Conditions and runs.** 2 methods (native, MCP) × 2 tool counts (5, 20) × 120 tasks × 3 runs × 2 models = **2,880 agent runs**. Each run writes a trace: condition, model and library versions, every step (tool name, arguments, result, latency, tokens) and the outcome (accuracy label, task success). Temperature 0; the system prompt and tool descriptions are identical in all conditions. Every task is written by the researcher and checked by a second person (clear instruction, single correct answer).
