# Practical Work 6 — Writing a Research Report (small-scale project)

**Тема отчёта:** *Retrieval for Retrieval-Augmented Generation (RAG) in Kazakh: A Small-Scale Comparison of Simple Search Methods on KazQAD* — малый реальный эксперимент про RAG (поиск по документам для AI-платформы). Тема ПР5 — MCP и LangChain, они не пересекаются.

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
| ≥ 2 визуальных элемента на задачу, Name_Surname в каждом | Введение: табл. 1, рис. 1 (концепт-карта), рис. 2 (схема RAG); Методология: табл. 2, рис. 3 (блок-схема); Результаты: табл. 3–6, рис. 4–7; Обсуждение: табл. 7, рис. 8 (логическая модель); Заключение: табл. 8, панель executive summary + текстовое поле с именем |
| ≥ 10 источников во введении, IEEE | 20+ источников во введении; список литературы в IEEE |
| Summary 5–7 предложений в конце каждой задачи | Есть в каждом разделе |
| A4, поля 20 мм, Times New Roman 12 / заголовки 14, одинарный интервал, по ширине | Шаблон `common/reference-pw6.docx` |
| Appendices | A — как воспроизвести, B — результаты по предметам, C — пример prefix-5, D — этика |

## Как подставить своё имя и пересобрать

1. Откройте `student.json`: `{"name_surname": "Aibek_Nurlanov", "group": "SE-2203"}`.
2. Из корня репозитория: `./build.sh pw-06` → появится `AibekNurlanov_SE-2203_PW6.docx`; рисунки перерисуются с вашим именем (нужен `pip install matplotlib`).
3. В Word обновите оглавление (*References → Update Table*).

## Как повторить эксперимент

```bash
pip install scipy scikit-learn matplotlib
cd pw-06-research-report/experiment
bash run_all.sh        # скачает KazQAD (git clone, ~400 МБ), ~3 минуты на 4 ядрах
```

Все числа в отчёте берутся из `experiment/results/*.json`; данные — открытый датасет KazQAD (ISSAI, CC BY-SA 4.0), без участников и персональных данных.
