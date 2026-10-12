# Practical Work 4 — Citation, Zotero and Literature Review

| Путь | Содержание |
|---|---|
| [`report/`](report/) | Отчёт по частям: `01` введение (плагиат, стили), `02` задание 1 (генерируется), `03` задание 2 (Zotero), `04` задание 3 (обзор литературы), `99` список литературы |
| `pw-04-citation-and-literature-review.docx` | Готовый отчёт в Word |
| [`sources/task1-sources.json`](sources/task1-sources.json) | Какие источники цитируются в задании 1, по категориям |
| [`sources/zotero-collections.json`](sources/zotero-collections.json) | Коллекции и теги библиотеки для задания 2 |
| [`output/citations-*.md`](output/) | Списки задания 1 отдельно для каждого стиля: APA, Chicago, IEEE, MLA |
| `output/zotero-library.ris` / `.bib` / `.json` | Библиотека из 20 статей для импорта в Zotero или Mendeley |
| `output/demo-*.docx`, `output/demo-*.md` | Один и тот же текст с цитатами и списком литературы в 4 стилях |
| [`task2-zotero/demo.md`](task2-zotero/demo.md) | Исходный текст демо-документа |
| [`tools/generate_citations.py`](tools/generate_citations.py) | Генератор списков и файлов для Zotero |

## Задание 1 — цитирование в 4 стилях

10 типов источников: журнальные статьи (7), книги (6), журналы целиком (5), газетные статьи (6), диссертации (6), электронные ресурсы (6), патенты (6), а также 3 дополнительных типа: доклады конференций (6), стандарты (5), отчёты (5). Каждый тип оформлен отдельно в APA 7, Chicago 17 (notes-bibliography), IEEE и MLA 9.

## Задание 2 — Zotero (что сделать на своём компьютере)

1. Установить Zotero 7 (<https://www.zotero.org/download/>) и плагин для Word (ставится автоматически) или браузерный Zotero Connector.
2. *File → Import… → A file →* выбрать `output/zotero-library.ris` → *Place imported collections and items into new collection*.
3. Создать подколлекции `01 Foundations and surveys` … `05 Security and MCP` (*New Subcollection…*) и перетащить статьи по таблице из `report/03-task2-zotero.md`; теги импортируются автоматически, коллекция каждой статьи указана в её заметке.
4. В Word: вкладка *Zotero → Add/Edit Citation* — вставить цитаты; *Document Preferences* — переключить стиль (APA / Chicago / IEEE / MLA); *Add/Edit Bibliography* — сформировать список.
5. Сделать скриншот рабочего пространства Zotero, сохранить как `screenshots/zotero-workspace.png` и вставить в отчёт (раздел *Step 5*).

Без Zotero тот же результат воспроизводит команда `./build.sh pw-04`: файлы `output/demo-*.docx` собираются тем же процессором CSL, что использует Zotero.

## Задание 3 — обзор литературы

`report/04-task3-literature-review.md`: больше двух страниц, тематическая структура (RAG; tool use и agent loop; оценка; безопасность; казахстанский контекст), нумерованные ссылки, как в примере из задания.

Сборка: `./build.sh pw-04`.
