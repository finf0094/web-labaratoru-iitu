# Appendix A. Interview guide (developers, after the experiment session)

Duration 20–25 minutes, held right after the session. Before starting: remind the participant of the purpose of the study and of confidentiality, confirm consent and permission to record audio. The participant is referred to only by the code (P01, P02, …).

**Block 1. Background (3 min)**

1. How long have you been programming in Python, and have you built anything with LLMs before (APIs, LangChain, agents)?
2. Had you heard of or used the Model Context Protocol before today?

**Block 2. Experience in the two conditions (8 min)**

3. Walk me through how you connected the tools natively with `@tool`. What was easy, what was hard?
4. Walk me through how you connected them through the MCP server. What was easy, what was hard?
5. Where did you lose the most time (setup, transport configuration, schemas, errors, tests)?
6. When you had to use the same tools in the second application, what did you have to do in each condition?

**Block 3. Agent behaviour and debugging (5 min)**

7. Did the agent call the wrong tool or pass wrong arguments during your session? How did you notice and fix it?
8. How easy was it to understand what the agent did (which tool, which arguments, which result)?

**Block 4. Preference and recommendations (6 min)**

9. Which method would you choose for a real project, and why? When would you choose the other one?
10. What would make connecting tools through MCP easier (documentation, templates, tools)?
11. What risks do you see in giving an agent access to tools through a separate server?

**Closing**

12. Is there anything important about today's tasks that we have not discussed?
