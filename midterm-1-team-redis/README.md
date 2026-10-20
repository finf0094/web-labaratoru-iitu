# Midterm 1 — командная статья: Spring Boot + Redis

**Статья:** *Performance study of a Spring Boot REST API and evaluation of Redis caching under high load*.
**Авторы:** Serik Zholdygaliev\* (автор для переписки), Ravil Yermukhan, Kulush Askhat — IITU, Алматы.
**Журнал:** International Journal of Information and Communication Technologies (IJICT, IITU), перечень ККСОН — Список 2, № 139.

| Файл | Что это |
|---|---|
| [`article/…_article.docx`](article/MT1_Zholdygaliev_Yermukhan_Askhat_Spring_Boot_Redis_article.docx) | Статья (12 страниц, IMRAD, аннотации EN/KZ/RU) |
| [`article/…_article.pdf`](article/MT1_Zholdygaliev_Yermukhan_Askhat_Spring_Boot_Redis_article.pdf) | Та же статья в PDF |
| [`article/CHANGES.txt`](article/CHANGES.txt) | Список последних правок статьи |
| [`figures/`](figures/) | Пять рисунков статьи (PNG) |
| [`explanation.md`](explanation.md) | Объяснение для защиты: термины, цифры, механизм, ответы на контрольные вопросы MT1 и на вопросы преподавателя |
| [`speech.md`](speech.md) | Текст выступления на ~7 минут, по страницам статьи |

**Главный результат:** Redis убрал 91% SQL-запросов и сократил p99 задержки на 32–61%, но средняя задержка и пропускная способность достоверно не изменились. На равномерной нагрузке пропускная способность упала на 22–34%. Причина: база занимала только 32% CPU на запрос (предел Амдала ≈ 1,47×), а путь через кэш добавил работу JVM.

> Исходники всех рисунков, код `cache-bench`, скрипты k6 и данные прогонов лежат в отдельном архиве `MT1_sources.zip` (Supplementary materials S1–S7). Его нужно прикладывать к статье при сдаче; в этой папке его нет.
