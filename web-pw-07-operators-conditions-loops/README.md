# Web Programming — Practical Work 7. Operators, Conditional Statements and Loops

**Язык:** Python 3.10+ (задание разрешает Java, Python или PHP на выбор).
Нужен Python ≥ 3.10, потому что в задании 5 используется `match / case` — это аналог `switch`. Сторонние библиотеки не нужны.

## Как запустить

```bash
cd web-pw-07-operators-conditions-loops
python3 tasks/task01_even_odd.py          # любое задание: task01 … task10
python3 -m unittest discover tests        # 15 автотестов всех заданий
python3 demo.py                           # пересоздать demo_output.md (примеры запусков)
```

На Windows вместо `python3` пишите `python`.

## Задания

| № | Файл | Что делает | Что используется |
|---|---|---|---|
| 1 | [`task01_even_odd.py`](tasks/task01_even_odd.py) | Чётное или нечётное число | `%`, `==`, `if / else` |
| 2 | [`task02_exam_admission.py`](tasks/task02_exam_admission.py) | Допуск к экзамену: посещаемость ≥ 70% **и** проект сдан | `>=`, логическое `and` |
| 3 | [`task03_grade_calculator.py`](tasks/task03_grade_calculator.py) | Оценка A/B/C/F по баллу 0–100, ошибка вне диапазона | цепочка `if / elif / else`, `or` |
| 4 | [`task04_discount.py`](tasks/task04_discount.py) | Скидка 0/5/10/15% по сумме покупки, итоговая цена | `<`, `if / elif`, арифметика |
| 5 | [`task05_day_of_week.py`](tasks/task05_day_of_week.py) | День недели по номеру 1–7, иначе «Invalid day number» | `match / case` (switch) |
| 6 | [`task06_numbers_1_to_n.py`](tasks/task06_numbers_1_to_n.py) | Числа от 1 до N | цикл `for` |
| 7 | [`task07_sum_while.py`](tasks/task07_sum_while.py) | Сумма чисел от 1 до N | цикл `while` |
| 8 | [`task08_multiplication_table.py`](tasks/task08_multiplication_table.py) | Таблица умножения от 1 до 10 | цикл `for` |
| 9 | [`task09_password.py`](tasks/task09_password.py) | Запрашивает пароль, пока не введут `java123` | `while True` + `break` — аналог `do...while` |
| 10 | [`task10_atm.py`](tasks/task10_atm.py) | Банкомат: баланс, пополнение, снятие, выход; баланс 100 000 KZT | цикл меню + `if / elif / else` |

Общие функции ввода лежат в [`tasks/input_utils.py`](tasks/input_utils.py). Если ввести текст вместо числа, программа не падает, а вежливо спрашивает ещё раз.

Примеры запусков всех заданий (ввод и вывод) — в [`demo_output.md`](demo_output.md).

## Как защищать (коротко)

* **Операторы.**
  * Арифметические: `+ - * / %`. Остаток `%` проверяет чётность: `n % 2 == 0`.
  * Сравнения: `== != < > <= >=`.
  * Логические: `and`, `or`, `not`. В задании 2 нужны **оба** условия, поэтому `and`.
* **Условия.**
  * `if / elif / else` проверяет условия по порядку и выполняет первую подходящую ветку. В задании 3 поэтому достаточно `score >= 75`: случай ≥ 90 уже обработан выше.
  * `match / case` — это `switch` в Python. `case _` — ветка «по умолчанию», как `default`.
* **Циклы.**
  * `for` — когда число повторов известно заранее: `range(1, n + 1)` даёт 1…N.
  * `while` — пока условие истинно. Счётчик увеличиваем сами (`i += 1`), иначе цикл будет бесконечным.
  * `do...while` в Python нет. Аналог — `while True:` и `break` внутри: тело выполнится минимум один раз, а условие проверяется в конце (задание 9).
* **Банкомат (задание 10).**
  * Меню крутится в `while True`, выход по пункту 4 через `break`.
  * Нулевые и отрицательные суммы отклоняются (`amount <= 0`).
  * Снять больше баланса нельзя (`amount > balance`).
  * Неверный пункт меню — сообщение об ошибке.
