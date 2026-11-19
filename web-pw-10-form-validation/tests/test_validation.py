"""Tests: every row of the assignment tables and the testing checklist.

Run from the folder of this practical work:  python3 -m unittest discover tests
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app import app  # noqa: E402
from validators import validate_age, validate_email, validate_name  # noqa: E402


class ValidatorTests(unittest.TestCase):
    def test_task1_table(self):
        self.assertEqual(validate_name("")[1], "Name is required!")
        self.assertEqual(validate_name("   ")[1], "Name is required!")
        self.assertEqual(validate_name("  Ali "), ("Ali", None))
        self.assertEqual(validate_name("Aigerim"), ("Aigerim", None))

    def test_task2_table(self):
        self.assertIsNone(validate_email("student@gmail.com")[1])
        for bad in ("studentgmail.com", "student@", "", "   ", "student@gmail", "a b@gmail.com", "@gmail.com"):
            self.assertEqual(validate_email(bad)[1], "Invalid email!", bad)

    def test_task3_table(self):
        self.assertEqual(validate_age("20"), (20, None))
        self.assertEqual(validate_age("15")[1], "Age must be between 18 and 100!")
        self.assertEqual(validate_age("150")[1], "Age must be between 18 and 100!")
        self.assertEqual(validate_age("abc")[1], "Age must be a number!")
        self.assertEqual(validate_age("")[1], "Age is required!")
        self.assertEqual(validate_age("20.5")[1], "Age must be a whole number!")
        self.assertIsNone(validate_age("18")[1])   # boundaries are inclusive
        self.assertIsNone(validate_age("100")[1])
        self.assertIsNotNone(validate_age("17")[1])
        self.assertIsNotNone(validate_age("101")[1])


class AppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def post(self, url, **data):
        r = self.client.post(url, data=data)
        return r.status_code, r.get_data(as_text=True)

    def test_pages_open(self):
        for url in ("/", "/task1", "/task2", "/task3", "/task4", "/task5", "/task5/without-html-validation"):
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_single_field_tasks(self):
        self.assertIn("Welcome, Ali!", self.post("/task1", student="Ali")[1])
        status, body = self.post("/task1", student="   ")
        self.assertEqual(status, 400)
        self.assertIn("Name is required!", body)
        self.assertIn("Valid email!", self.post("/task2", email="student@gmail.com")[1])
        self.assertIn("Invalid email!", self.post("/task2", email="student@")[1])
        self.assertIn("Valid age!", self.post("/task3", age="20")[1])
        self.assertIn("Age must be a number!", self.post("/task3", age="abc")[1])

    def test_task4_example_a(self):
        status, body = self.post("/task4", student="Ali", email="ali@gmail.com", age="20")
        self.assertEqual(status, 200)
        self.assertIn("Registration data is valid!", body)

    def test_task4_example_b_shows_all_errors(self):
        status, body = self.post("/task4", student="", email="invalid-email", age="15")
        self.assertEqual(status, 400)
        for message in ("Name is required!", "Invalid email!", "Age must be between 18 and 100!"):
            self.assertIn(message, body)
        self.assertNotIn("Registration data is valid!", body)

    def test_task5_html_attributes_present_and_absent(self):
        with_attrs = self.client.get("/task5").get_data(as_text=True)
        self.assertIn('type="email" required', with_attrs)
        self.assertIn('min="18" max="100" required', with_attrs)
        without = self.client.get("/task5/without-html-validation").get_data(as_text=True)
        self.assertNotIn("required", without.split("<form")[1].split("</form>")[0])

    def test_task5_server_rejects_bypassed_browser_validation(self):
        # A request sent directly (like curl) skips the browser checks entirely.
        status, body = self.post("/task5", student=" ", email="x", age="abc")
        self.assertEqual(status, 400)
        for message in ("Name is required!", "Invalid email!", "Age must be a number!"):
            self.assertIn(message, body)

    def test_output_is_escaped(self):
        body = self.post("/task1", student="<b>Ali</b>")[1]
        self.assertIn("Welcome, &lt;b&gt;Ali&lt;/b&gt;!", body)


if __name__ == "__main__":
    unittest.main()
