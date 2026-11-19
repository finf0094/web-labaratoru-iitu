# Web Programming — Practical Work 9. Processing HTML Forms with GET and POST

**Язык:** Python 3.10+ и Flask (задание разрешает Java, Python или PHP).
Все формы обрабатываются **на сервере**: значения читаются в `app.py`, сервер формирует ответную страницу. Калькулятор тоже считает на сервере, без JavaScript.

## Как запустить

```bash
cd web-pw-09-get-post-forms
pip install -r requirements.txt     # Flask
python3 app.py                      # открыть http://127.0.0.1:5000
python3 -m unittest discover tests  # 8 автотестов
```

Скриншоты пересоздаются командой `pip install playwright pillow && python3 make_screenshots.py`. Скрипт сам запускает сервер, заполняет формы в Chromium и рисует над каждой страницей адресную строку с настоящим URL.

## Задания и где они в коде

| № | Страница | Метод | Обработчик в `app.py` | Что проверено |
|---|---|---|---|---|
| 1 | `/student-search` → `/search?student=Ali` | GET | `search()` читает `request.args["student"]` | «You searched for: Ali», имя видно в URL |
| 2 | `/register` | POST | `register()` читает `request.form` | «Registration Successful!», имя и email; в URL значений нет; пустое поле — ошибка |
| 3 | `/calculator` → `/calculate?a=10&b=5&operation=%2B` | GET | `calculate_view()` и `calculate()` | +, −, ×, ÷; деление на ноль и не-числа — сообщение об ошибке |
| 4 | `/contact` | POST | `contact()` | «Message received!»; пустые имя или сообщение отклоняются |
| 5 | `/demo` | GET + POST | `demo_get()`, `demo_post()` | Две независимые формы, таблица отличий GET и POST |

Внизу каждой страницы с результатом показано: метод запроса, URL и где были значения — в строке запроса или в теле запроса. Это удобно показывать на защите.

## Что сдавать

* **Исходный код:** `app.py`, `templates/*.html`, `static/style.css`.
* **Скриншоты всех пяти заданий** — в [`screenshots/`](screenshots/):

  | Задание | Файлы |
  |---|---|
  | 1 | `task1_1_search_form.png`, `task1_2_search_result_url.png` — URL после GET-формы |
  | 2 | `task2_1_registration_form.png`, `task2_2_registration_result.png` |
  | 3 | `task3_1_calculator_form.png`, `task3_2_calculator_result_url.png`, `task3_3_division_by_zero.png` |
  | 4 | `task4_1_contact_form.png`, `task4_2_contact_result.png`, `task4_3_contact_empty_fields.png` |
  | 5 | `task5_1_demo_page.png`, `task5_2_demo_after_get.png`, `task5_3_demo_after_post.png` |

* **Письменные ответы** (на английском, как в задании) — в [`ANSWERS.md`](ANSWERS.md).

## Как защищать (коротко)

* **GET** кладёт значения в URL после `?`: `/search?student=Ali`. Такую ссылку можно сохранить и переслать. Сервер читает их из `request.args`. Подходит для поиска и получения данных.
* **POST** кладёт значения в **тело запроса**, поэтому URL остаётся `/register`. Сервер читает их из `request.form`. Подходит для отправки данных: регистрация, сообщения, вход.
* Имя параметра берётся из атрибута `name` у `<input>`.
* **POST не значит «секретно».** Данные не шифруются: их видно в DevTools (вкладка Network) и в сети при HTTP. Защищает только **HTTPS**.
* Сообщение «Registration Successful!» не значит, что данные сохранены. Базы данных здесь нет, сервер только принимает значения и показывает их.
* Вывод экранируется шаблонизатором Jinja. Если ввести `<script>`, он покажется как текст и не выполнится (это проверяет тест `test_output_is_escaped`).
