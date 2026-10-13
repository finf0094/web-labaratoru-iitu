# Research Methods — лабораторные и практические работы (IITU)

Все шесть работ выполнены на одну сквозную тему, чтобы они складывались в единое исследование (заготовку для дипломной работы):

> **Design and Evaluation of an Agentic AI Platform Integrating the Agent Loop, Model Context Protocol (MCP) Tools and Retrieval-Augmented Generation (RAG)**
>
> *Проектирование и оценка агентной AI-платформы с интеграцией агентного цикла (agent loop), инструментов через Model Context Protocol (MCP) и генерации с дополнением извлечённой информацией (RAG).*

Отчёты написаны на английском (как и задания). Они следуют структуре из лекционных материалов курса (*Writing a Research Report*, *How to Write an Effective Research Report*, *Research Methodology: An Introduction*): Title → Table of Contents → Abstract → основная часть → Conclusion → References → Appendices. Тип исследования классифицирован по Kothari, этапы соотнесены с research process.

## Структура репозитория

| Папка | Работа | Что внутри |
|---|---|---|
| [`lab-01-subject-area-analysis/`](lab-01-subject-area-analysis/) | **Laboratory Work 1.** Review and analysis of the subject area | Предметная область (Table 1), 5 аналогов (Table 2), классификация (Table 3), сравнительный анализ (Table 4), вывод |
| [`pw-02-research-plan/`](pw-02-research-plan/) | **Practical Work 2.** Research plan development | Проблема, цель, RQ и гипотезы, операциональные определения, методы, ресурсы, переменные, этика, структура, тестирование, фокус-группа, бюджет, график, доп. этап, summary |
| [`pw-03-literature-review-techniques/`](pw-03-literature-review-techniques/) | **Practical Work 3.** Literature review techniques | Базы данных и поисковые запросы (Boolean), фильтрация, матрица 12 статей, пробелы (gaps) по категориям, обзор, заключение |
| [`pw-04-citation-and-literature-review/`](pw-04-citation-and-literature-review/) | **Practical Work 4.** Citation styles, Zotero, literature review | Задание 1 — источники 10 типов в APA, Chicago, IEEE, MLA; задание 2 — библиотека для Zotero (RIS/BibTeX) и документы с цитатами в 4 стилях; задание 3 — обзор литературы |
| [`pw-05-research-methodology/`](pw-05-research-methodology/) | **Practical Work 5.** Research plan and methodology | RQ/гипотезы, дизайн исследования, выборка (со скриптом расчёта), методы и инструменты сбора данных, процесс, анализ, summary; приложения: гайд интервью, анкета SUS/TAM, спецификация датасетов, форма согласия |
| [`pw-06-research-report/`](pw-06-research-report/) | **Practical Work 6.** Writing a research report | Полный отчёт по малому реальному эксперименту про **RAG**: 5 методов поиска для казахского языка на датасете KazQAD (1 929 вопросов ЕНТ); Introduction, Methodology, Results, Discussion, Conclusion, References (IEEE), Appendices; код и графики; имя студента подставляется из `student.json` |
| [`common/`](common/) | Общие ресурсы | `references.json` — единая база проверенных источников (CSL-JSON); `csl/` — стили APA, Chicago, IEEE, MLA; `reference.docx` — шаблон оформления Word |
| [`build.sh`](build.sh) | Сборка | Собирает все отчёты в DOCX |

В каждой папке есть:

* исходник отчёта в Markdown (`report.md` или папка `report/` из нескольких частей), который удобно читать прямо на GitHub;
* готовый Word-файл `<папка>.docx` — его можно сдавать или распечатывать;
* свой `README.md` с кратким описанием работы;
* для ПР5 и ПР6 — `explanation.md`: шпаргалка для защиты (что рассказывать, ключевые цифры, вопросы и ответы).

## Как открыть готовые отчёты

Ничего запускать не нужно: готовые `.docx` уже лежат в папках, например `pw-02-research-plan/pw-02-research-plan.docx`. Перед сдачей впишите ФИО, группу и преподавателя на титульной части (строка `Student: ____ · Group: ____ · Instructor: ____`) и при необходимости обновите оглавление в Word (*References → Update Table*).

## Как пересобрать отчёты (Markdown → DOCX)

### 1. Установить зависимости

| Инструмент | Версия | Установка |
|---|---|---|
| Pandoc | ≥ 3.1 | Windows: `winget install --id JohnMacFarlane.Pandoc`; macOS: `brew install pandoc`; Ubuntu: `sudo apt install pandoc` или пакет с <https://pandoc.org/installing.html> |
| Python | ≥ 3.10 | <https://www.python.org/downloads/> |
| python-docx | любая | `pip install python-docx` (нужен только для пересоздания шаблона `common/reference.docx`) |

### 2. Собрать

```bash
git clone https://github.com/finf0094/web-labaratoru-iitu.git
cd web-labaratoru-iitu
./build.sh              # собрать все работы
./build.sh pw-04        # собрать только ПР4 (папки, начинающиеся с "pw-04")
```

На Windows запускайте через **Git Bash** или **WSL** (`bash build.sh`).

Скрипт:

1. для ПР4 запускает `tools/generate_citations.py` (генерирует списки литературы в 4 стилях и файлы для Zotero);
2. для каждой папки `lab-*` и `pw-*` вызывает Pandoc с `--citeproc`: ссылки вида `[@lewis2020]` в тексте превращаются в нумерованные ссылки IEEE `[1]`, а в конце формируется список литературы из `common/references.json`;
3. применяет шаблон `common/reference.docx` (Times New Roman 12, интервал 1,5, поля 3/1,5/2/2 см, таблицы с рамками) и добавляет оглавление.

### 3. ПР6: имя, группа и эксперимент

* Впишите имя и группу в `pw-06-research-report/student.json` и выполните `./build.sh pw-06` — получится `ИмяФамилия_Группа_PW6.docx`, имя появится во всех подписях, графиках и водяном знаке (для перерисовки графиков нужен `pip install matplotlib`).
* Повтор эксперимента: `pip install scipy scikit-learn matplotlib`, затем `bash pw-06-research-report/experiment/run_all.sh` (~3 минуты, скачивает KazQAD).

### 4. Дополнительно

```bash
# расчёт размера выборки для ПР5 (только стандартная библиотека Python)
python3 pw-05-research-methodology/tools/sample_size.py --population 5000

# пересоздать шаблон Word
python3 common/make_reference_docx.py
```

## Как редактировать

* **Текст** — правьте `.md` файлы (обычный Markdown, таблицы через `|`), затем `./build.sh`.
* **Ссылка на источник** — пишите `[@ключ]`, несколько сразу — `[@lewis2020; @karpukhin2020]`. Ключи смотрите в `common/references.json`.
* **Новый источник** — добавьте запись в `common/references.json` в формате CSL-JSON (можно экспортировать из Zotero: *File → Export Library → CSL JSON*).
* **Другой стиль цитирования** — замените `ieee.csl` в `build.sh` на `apa.csl`, `modern-language-association.csl` или `chicago-notes-bibliography.csl`.

## Об источниках

Все источники в `common/references.json` — реальные публикации. Авторы, годы, названия, издания и DOI проверены по страницам издателей, ACL Anthology, NeurIPS/OpenReview, arXiv, Google Patents и репозиториев университетов. Ссылки на онлайн-ресурсы ведут на конкретные страницы. Если преподаватель требует только рецензируемые источники, препринты arXiv помечены в списке литературы (тип `article`, издатель arXiv) и их легко заменить.
