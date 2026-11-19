"""Tests for all 10 tasks: logic functions and full runs with simulated keyboard input.

Run from the folder of this practical work:  python3 -m unittest discover tests
"""
import subprocess
import sys
import unittest
from pathlib import Path

TASKS = Path(__file__).resolve().parent.parent / "tasks"
sys.path.insert(0, str(TASKS))

from task01_even_odd import even_or_odd  # noqa: E402
from task02_exam_admission import is_admitted  # noqa: E402
from task03_grade_calculator import grade  # noqa: E402
from task04_discount import discount_percent, final_price  # noqa: E402
from task05_day_of_week import day_name  # noqa: E402
from task06_numbers_1_to_n import numbers_up_to  # noqa: E402
from task07_sum_while import sum_up_to  # noqa: E402
from task08_multiplication_table import multiplication_table  # noqa: E402
from task10_atm import deposit, withdraw  # noqa: E402


def run(script, keyboard):
    """Run a task script, type `keyboard` into it and return everything it printed."""
    result = subprocess.run([sys.executable, str(TASKS / script)], input=keyboard,
                            capture_output=True, text=True, timeout=10)
    return result.stdout


class LogicTests(unittest.TestCase):
    def test_even_odd(self):
        self.assertEqual(even_or_odd(4), "even")
        self.assertEqual(even_or_odd(7), "odd")
        self.assertEqual(even_or_odd(0), "even")
        self.assertEqual(even_or_odd(-3), "odd")

    def test_exam_admission(self):
        self.assertTrue(is_admitted(70, True))
        self.assertTrue(is_admitted(95, True))
        self.assertFalse(is_admitted(69.9, True))
        self.assertFalse(is_admitted(90, False))

    def test_grades_on_boundaries(self):
        cases = {100: "A", 90: "A", 89: "B", 75: "B", 74: "C", 50: "C", 49: "F", 0: "F"}
        for score, letter in cases.items():
            self.assertEqual(grade(score), letter, score)
        self.assertIsNone(grade(-1))
        self.assertIsNone(grade(101))

    def test_discount_rules(self):
        cases = {9_999: 0, 10_000: 5, 49_999: 5, 50_000: 10, 99_999: 10, 100_000: 15, 250_000: 15}
        for amount, percent in cases.items():
            self.assertEqual(discount_percent(amount), percent, amount)
        self.assertEqual(final_price(60_000), 54_000)

    def test_day_names(self):
        self.assertEqual(day_name(1), "Monday")
        self.assertEqual(day_name(7), "Sunday")
        self.assertEqual(day_name(0), "Invalid day number")
        self.assertEqual(day_name(8), "Invalid day number")

    def test_loops(self):
        self.assertEqual(numbers_up_to(5), "1, 2, 3, 4, 5")
        self.assertEqual(sum_up_to(10), 55)
        self.assertEqual(sum_up_to(1), 1)
        table = multiplication_table(5)
        self.assertEqual(len(table), 10)
        self.assertEqual(table[0], "5 × 1 = 5")
        self.assertEqual(table[-1], "5 × 10 = 50")

    def test_atm_operations(self):
        self.assertEqual(deposit(100_000, 5_000)[0], 105_000)
        self.assertEqual(deposit(100_000, 0)[0], 100_000)
        self.assertEqual(deposit(100_000, -10)[0], 100_000)
        self.assertEqual(withdraw(100_000, 30_000)[0], 70_000)
        self.assertEqual(withdraw(100_000, 200_000), (100_000, "Error: insufficient funds."))
        self.assertEqual(withdraw(100_000, -5)[0], 100_000)


class ProgramRunTests(unittest.TestCase):
    def test_task01_asks_again_on_text(self):
        out = run("task01_even_odd.py", "abc\n7\n")
        self.assertIn("Please enter a whole number.", out)
        self.assertIn("7 is odd.", out)

    def test_task02(self):
        self.assertIn("Allowed to exam", run("task02_exam_admission.py", "85\nyes\n"))
        self.assertIn("Not allowed", run("task02_exam_admission.py", "60\nyes\n"))

    def test_task03_error(self):
        self.assertIn("Error: the score must be between 0 and 100.", run("task03_grade_calculator.py", "120\n"))
        self.assertIn("Grade: B", run("task03_grade_calculator.py", "80\n"))

    def test_task04(self):
        out = run("task04_discount.py", "60000\n")
        self.assertIn("Discount: 10%", out)
        self.assertIn("Final amount: 54,000.00 KZT", out)

    def test_task05(self):
        self.assertIn("Wednesday", run("task05_day_of_week.py", "3\n"))
        self.assertIn("Invalid day number", run("task05_day_of_week.py", "9\n"))

    def test_task06_to_08(self):
        self.assertIn("1, 2, 3, 4, 5", run("task06_numbers_1_to_n.py", "0\n5\n"))
        self.assertIn("= 5050", run("task07_sum_while.py", "100\n"))
        self.assertIn("5 × 10 = 50", run("task08_multiplication_table.py", "5\n"))

    def test_task09_repeats_until_correct(self):
        out = run("task09_password.py", "1234\npython\njava123\n")
        self.assertEqual(out.count("Wrong password, try again."), 2)
        self.assertIn("Access granted", out)

    def test_task10_full_session(self):
        out = run("task10_atm.py", "1\n2\n-50\n2\n20000\n3\n500000\n3\n70000\n9\n1\n4\n")
        self.assertIn("Balance: 100,000.00 KZT", out)
        self.assertIn("Error: the amount must be greater than zero.", out)
        self.assertIn("New balance: 120,000.00 KZT", out)
        self.assertIn("Error: insufficient funds.", out)
        self.assertIn("New balance: 50,000.00 KZT", out)
        self.assertIn("Error: invalid menu choice.", out)
        self.assertIn("Goodbye!", out)


if __name__ == "__main__":
    unittest.main()
