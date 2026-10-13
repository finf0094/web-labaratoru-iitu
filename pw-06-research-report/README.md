# Practical Work 6 — Writing a Research Report (small-scale project)

**Тема отчёта:** *Retrieval Quality, Poisoning Exposure and MCP Integration Overhead for a Kazakh-Language Agentic AI Platform: A Small-Scale Experimental Study* — малый реальный эксперимент в рамках общей темы (агентная AI-платформа с agent loop, MCP и RAG).

| Путь | Содержание |
|---|---|
| `NameSurname_GroupNumber_PW6.docx` | Готовый отчёт (имя файла — как требует задание) |
| [`student.json`](student.json) | **Впишите сюда своё имя и группу** — они подставятся во весь текст, подписи, графики и водяной знак |
| [`report/`](report/) | Текст отчёта по частям: введение, методология, результаты, обсуждение, заключение, литература, приложения |
| [`experiment/`](experiment/) | Код эксперимента, результаты (`results/`), рисунки (`figures/`) |
| [`explanation.md`](explanation.md) | Шпаргалка для защиты |

## Требования задания → где выполнено

| Требование | Как выполнено |
|---|---|
| 5 задач, каждая ≥ 1 страницы | Разделы 1–5 (Introduction, Methodology, Results, Discussion, Conclusion) |
| ≥ 2 визуальных элемента на задачу, Name_Surname в каждом | Введение: табл. 1, рис. 1–2; Методология: табл. 2, рис. 3; Результаты: табл. 3–8, рис. 4–7; Обсуждение: табл. 9, рис. 8; Заключение: табл. 10, панель executive summary + текстовое поле с именем |
| ≥ 10 источников во введении, IEEE | 20+ источников во введении; список литературы в IEEE |
| Summary 5–7 предложений в конце каждой задачи | Есть в каждом разделе |
| A4, поля 20 мм, Times New Roman 12 / заголовки 14, одинарный интервал, по ширине | Шаблон `common/reference-pw6.docx` |
| Appendices | A — воспроизведение, B — шаблоны guardrail, C — атаки, D — схема MCP-инструмента, E — таблица по предметам, F — этика |

## Как подставить своё имя и пересобрать

1. Откройте `student.json`: `{"name_surname": "Aibek_Nurlanov", "group": "SE-2203"}`.
2. Из корня репозитория: `./build.sh pw-06` → появится `AibekNurlanov_SE-2203_PW6.docx`; рисунки перерисуются с вашим именем (нужен `pip install matplotlib`).
3. В Word обновите оглавление (*References → Update Table*).

## Как повторить эксперимент

```bash
pip install scipy scikit-learn matplotlib mcp
cd pw-06-research-report/experiment
bash run_all.sh        # скачает KazQAD (git clone, ~400 МБ), ~6 минут на 4 ядрах
```

Все числа в отчёте берутся из `experiment/results/*.json`; данные — открытый датасет KazQAD (ISSAI, CC BY-SA 4.0), без участников и персональных данных.
