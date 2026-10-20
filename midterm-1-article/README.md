# Midterm 1 — научная статья (IMRAD)

**Тема статьи:** *How chunk size and overlap affect retrieval quality in retrieval-augmented generation: an experiment on SQuAD*
(Как размер фрагмента и перекрытие влияют на качество поиска в RAG: эксперимент на SQuAD).

**Автор:** Kulush Askhat, группа IT1CCO-2402IS, IITU, Алматы.

Готовая статья: [`KulushAskhat_IT1CCO-2402IS_MT1.docx`](KulushAskhat_IT1CCO-2402IS_MT1.docx) — 12 страниц A4.

Материалы к защите:

* [`explanation.md`](explanation.md) — простое объяснение: о чём статья, все термины, цифры, ответы на контрольные вопросы MT1;
* [`speech.md`](speech.md) — текст выступления (~7 минут), по страницам статьи.

## Что было сделано

1. Взят открытый английский датасет **SQuAD v1.1** (Стэнфорд): 490 статей Википедии, 2,46 млн слов, 10 570 вопросов с точно размеченными ответами.
2. Статьи нарезаны на фрагменты (chunks) **9 способами**: окна по 50/100/200/400 слов без перекрытия и с перекрытием 25%, плюс деление по абзацам.
3. Для каждого способа построен поисковый индекс **BM25** и для каждого вопроса найдено 40 лучших фрагментов.
4. Посчитаны Hit@k, MRR@10, доля «разрезанных» ответов и качество при фиксированном бюджете контекста; различия проверены критерием Макнемара с поправкой Холма, доверительные интервалы — бутстрэпом.

Это новая работа: другой датасет (английский SQuAD, а не казахский KazQAD из ПР6), другой вопрос (разбиение текста, а не выбор метода поиска) и свой код.

## Журнал и оформление

Журнал выбран из списка ККСОН (направление «Автоматизация, информатика, ИКТ»): **Вестник Университета Шакарима. Серия «Технические науки»** (Bulletin of Shakarim University. Technical Sciences), ISSN 2788-7995, сайт <https://tech.vestnik.shakarim.kz/jour>. В файле `KOKSON_journals_1.xlsx` он стоит в «Списке 2» под № 110; направление «Автоматизация және ақпараттық технологиялар» (автоматизация и информационные технологии) включено с января 2025 года (приказ от 28.02.2025 № 293).

По требованиям журнала в статье есть: код МРНТИ (IRSTI), название, автор, организация, город и страна, e-mail, аннотации и ключевые слова на трёх языках (английский, русский, казахский), разделы IMRAD, блок «About the author», список литературы по ГОСТ (стиль `common/csl/gost-r-7-0-5-2008-numeric.csl`, нумерация в порядке цитирования [1], [2] …).

Оформление: A4, поля 2 см, Times New Roman 12 пт, одинарный интервал, подписи «Figure N – Название» по центру под рисунком, «Table N – Название» над таблицей.

> ⚠️ Сайт журнала из нашей среды был недоступен, поэтому точные параметры шрифта и полей сверены не полностью. Перед подачей откройте раздел *Author Guidelines* на сайте журнала и, если там другие параметры, поменяйте профиль `article` в `common/make_reference_docx.py`. Код МРНТИ (20.19 — информационный поиск; 28.23 — искусственный интеллект) проверьте на <https://grnti.ru>. Впишите свой e-mail в строку `e-mail: ____` в `article/article.md`.

## Структура папки

| Путь | Что это |
|---|---|
| `article/article.md` | Исходник статьи (Markdown + ссылки `[@ключ]`) |
| `KulushAskhat_IT1CCO-2402IS_MT1.docx` | Готовая статья в Word |
| `build_article.sh` | Сборка: графики → диаграммы → скриншоты → DOCX |
| `experiment/chunking.py` | Загрузка SQuAD и 9 стратегий разбиения |
| `experiment/retrieval.py` | Поиск BM25 (k1 = 0,9, b = 0,4) на разреженных матрицах |
| `experiment/run_experiment.py` | Эксперимент: метрики, бутстрэп, McNemar + Holm |
| `experiment/make_figures.py` | Рисует графики из `results/summary.json` |
| `experiment/results/` | `summary.json` (все метрики), `per_question.csv` (ранг для каждого вопроса), `run_log.txt` (лог запуска) |
| `diagrams/*.puml` | Исходники UML-диаграмм и блок-схемы (PlantUML) |
| `mockup/rag_assistant_mockup.html` | Макет интерфейса (HTML), `screenshot.py` делает PNG |
| `code-screenshots/render_code.py` | Делает скриншоты кода (Pygments, светлая тема) |

## Источники каждого рисунка и таблицы

Все визуальные элементы созданы автором; у каждого есть исходный файл.

| Элемент в статье | Что показывает | Исходник | Картинка |
|---|---|---|---|
| Table 1 | Обзор литературы | `article/article.md` | — |
| Figure 1 | Блок-схема алгоритма оценки | `diagrams/evaluation_flowchart.puml` | `diagrams/evaluation_flowchart.png` |
| Figure 2 | UML-диаграмма классов | `diagrams/class_diagram.puml` | `diagrams/class_diagram.png` |
| Figure 3 | Код разбиения на фрагменты | `experiment/chunking.py` → `code-screenshots/render_code.py` | `code-screenshots/code_chunking.png` |
| Figure 4 | Код BM25 | `experiment/retrieval.py` → `render_code.py` | `code-screenshots/code_bm25.png` |
| Figure 5 | Код проверки релевантности и метрик | `experiment/run_experiment.py` → `render_code.py` | `code-screenshots/code_relevance.png` |
| Figure 6 | UML-диаграмма компонентов | `diagrams/experiment_components.puml` | `diagrams/experiment_components.png` |
| Table 2, Table 3, Table 4 | Размер индексов, качество, тесты | `experiment/results/summary.json`, `run_log.txt` | — |
| Figure 7 | Hit@5 от размера фрагмента | `experiment/make_figures.py` | `experiment/figures/hit5_vs_size.png` |
| Figure 8 | Разрезанные ответы и выигрыш от перекрытия | `experiment/make_figures.py` | `experiment/figures/split_and_gain.png` |
| Figure 9 | Кривые Hit@k | `experiment/make_figures.py` | `experiment/figures/hit_at_k.png` |
| Figure 10 | Качество при бюджете контекста | `experiment/make_figures.py` | `experiment/figures/context_budget.png` |
| Figure 11 | UML-диаграмма последовательности RAG | `diagrams/rag_sequence.puml` | `diagrams/rag_sequence.png` |
| Figure 12 | Макет интерфейса RAG-ассистента | `mockup/rag_assistant_mockup.html` | `mockup/rag_assistant_mockup.png` |

## Как повторить

```bash
pip install numpy scipy scikit-learn matplotlib pygments playwright python-docx
cd midterm-1-article/experiment
python3 run_experiment.py        # сам скачает SQuAD через git clone в data/, несколько минут
cd ..
PLANTUML_JAR=/путь/к/plantuml.jar ./build_article.sh   # графики, диаграммы, скриншоты и DOCX
./build_article.sh --docx-only                         # только пересобрать DOCX
```

Нужны Pandoc ≥ 3.1 и Java (для PlantUML, <https://plantuml.com/download>). Для скриншота макета нужен Chromium для Playwright (`python3 -m playwright install chromium`). Без PlantUML и Playwright скрипт оставит уже готовые PNG.
