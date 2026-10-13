# Practical Work 5 — Research Plan and Methodology

**Тема:** Tools for LLM Agents — Connecting Tools to an AI Platform through the Model Context Protocol (MCP) and LangChain.

Простая практическая тема: как лучше подключать инструменты (tools) к LLM-агенту — нативно через `@tool` в LangChain или через отдельный MCP-сервер, загружаемый в агента через `langchain-mcp-adapters`. Сравниваем трудозатраты разработчика, точность вызова инструментов, задержку и удобство.

| Путь | Содержание |
|---|---|
| [`report/01-methodology.md`](report/01-methodology.md) | Основной текст: введение (что такое tool, agent loop, MCP, LangChain) и пункты 1–8 задания |
| [`report/02-appendix-a-interview-guide.md`](report/02-appendix-a-interview-guide.md) | Приложение A: гайд интервью с разработчиками (12 вопросов) |
| [`report/03-appendix-b-questionnaire.md`](report/03-appendix-b-questionnaire.md) | Приложение B: анкета SUS (10 пунктов) + TAM (простота и полезность, 8 пунктов) |
| [`report/04-appendix-c-task-sheet.md`](report/04-appendix-c-task-sheet.md) | Приложение C: задание для разработчиков (инструменты, acceptance-тесты, что измеряется) и спецификация набора из 120 задач для агента |
| [`report/05-appendix-d-consent.md`](report/05-appendix-d-consent.md) | Приложение D: форма информированного согласия |
| [`report/99-references.md`](report/99-references.md) | Список литературы (IEEE, формируется из `common/references.json`) |
| [`tools/sample_size.py`](tools/sample_size.py) | Расчёт объёмов выборки (paired t-test, McNemar, точность разности долей, p95) |
| [`explanation.md`](explanation.md) | Шпаргалка для защиты (простыми словами) |
| `pw-05-research-methodology.docx` | Готовый отчёт в Word |

## Соответствие пунктам задания

| Пункт задания | Раздел отчёта |
|---|---|
| 1) Research questions / hypotheses | 1 — пробелы в литературе, таблица RQ1–RQ4, H1–H4, метрики |
| 2) Research design (qualitative / quantitative / mixed + обоснование) | 2 — mixed methods (в основном количественный, explanatory sequential), тип исследования по лекции, обоснование: validity, reliability, feasibility |
| 3) Target population and sample | 3 — разработчики (24–36, power analysis), 120 задач (McNemar), 1000 замеров задержки, 12–15 интервью; Latin square; ограничения обобщаемости |
| 4) Data collection methods | 4 — таблица методов с обоснованием |
| 5) Data collection instruments + pilot testing | 5, приложения A–D |
| 6) Data collection process (timeline, logistics, ethics) | 6 — график ноябрь 2026 – апрель 2027, логистика, этика |
| 7) Data analysis methods | 7 — количественный, качественный анализ, интеграция, прозрачность |
| 8) Summary of the methodology | 8 — включая критерии хорошего исследования (systematic, logical, empirical, replicable) и ограничения |

## Запуск расчёта выборки

```bash
python3 pw-05-research-methodology/tools/sample_size.py
```

Нужен только Python ≥ 3.8, сторонние библиотеки не требуются. Все числа в разделе 3 отчёта совпадают с выводом скрипта.

Сборка отчёта: `./build.sh pw-05`.
