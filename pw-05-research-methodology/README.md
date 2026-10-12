# Practical Work 5 — Research Plan and Methodology

| Путь | Содержание |
|---|---|
| [`report/01-methodology.md`](report/01-methodology.md) | Основной текст: пункты 1–8 задания |
| [`report/02-…05-*.md`](report/) | Приложения A–D: гайд интервью, анкета (SUS + TAM + trust), спецификация датасетов, форма информированного согласия |
| [`tools/sample_size.py`](tools/sample_size.py) | Расчёт объёма выборки (Cochran, power analysis, точность доли) |
| `pw-05-research-methodology.docx` | Готовый отчёт в Word |

## Соответствие пунктам задания

| Пункт | Раздел |
|---|---|
| 1) Research questions / hypotheses | 1 (таблица RQ1–RQ5, H1–H5, метрики) |
| 2) Research design (qualitative / quantitative / mixed + обоснование) | 2 (Design Science + sequential mixed methods; тип исследования по лекции) |
| 3) Target population and sample | 3 (стратегии отбора, объём выборки, ограничения) |
| 4) Data collection methods | 4 |
| 5) Data collection instruments + pilot testing | 5, приложения A–D |
| 6) Data collection process + ethics | 6 |
| 7) Data analysis methods | 7 |
| 8) Summary of methodology | 8 (включая критерии хорошего исследования) |

## Запуск расчёта выборки

```bash
python3 pw-05-research-methodology/tools/sample_size.py                 # N = 5000 по умолчанию
python3 pw-05-research-methodology/tools/sample_size.py --population 8000
```

Нужен только Python ≥ 3.8, сторонние библиотеки не требуются.

Сборка отчёта: `./build.sh pw-05`.
