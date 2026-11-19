"""Tests for all five tasks (Flask test client).

Run from the folder of this practical work:  python3 -m unittest discover tests
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app import app  # noqa: E402


class FormsTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def text(self, response):
        return response.get_data(as_text=True)

    def test_pages_open(self):
        for url in ("/", "/student-search", "/register", "/calculator", "/contact", "/demo"):
            self.assertEqual(self.client.get(url).status_code, 200, url)

    def test_task1_search_uses_query_string(self):
        r = self.client.get("/search?student=Ali")
        self.assertEqual(r.status_code, 200)
        self.assertIn("You searched for: Ali", self.text(r))
        self.assertIn("/search?student=Ali", self.text(r))
        self.assertIn('method="GET"', self.text(self.client.get("/student-search")))
        self.assertEqual(self.client.get("/search?student=").status_code, 400)

    def test_task2_registration_post(self):
        r = self.client.post("/register", data={"first_name": "Ali", "last_name": "Akhmetov",
                                                "email": "ali@example.com"})
        body = self.text(r)
        self.assertIn("Registration Successful!", body)
        self.assertIn("Name: Ali Akhmetov", body)
        self.assertIn("Email: ali@example.com", body)
        self.assertIn("URL: <code>/register</code>", body)  # no form values in the URL
        self.assertIn('method="POST"', self.text(self.client.get("/register")))

    def test_task2_missing_field(self):
        r = self.client.post("/register", data={"first_name": "Ali", "last_name": "", "email": "a@b.kz"})
        self.assertEqual(r.status_code, 400)
        self.assertIn("Last name is required.", self.text(r))

    def test_task3_calculator(self):
        self.assertIn("Result: 15", self.text(self.client.get("/calculate?a=10&b=5&operation=%2B")))
        self.assertIn("Result: 5", self.text(self.client.get("/calculate?a=10&b=5&operation=-")))
        self.assertIn("Result: 50", self.text(self.client.get("/calculate?a=10&b=5&operation=*")))
        self.assertIn("Result: 2.5", self.text(self.client.get("/calculate?a=5&b=2&operation=/")))
        r = self.client.get("/calculate?a=10&b=0&operation=/")
        self.assertEqual(r.status_code, 400)
        self.assertIn("division by zero", self.text(r))
        self.assertIn("two valid numbers", self.text(self.client.get("/calculate?a=x&b=5&operation=%2B")))

    def test_task4_contact(self):
        r = self.client.post("/contact", data={"name": "Dana", "message": "I have a question about GET and POST."})
        body = self.text(r)
        self.assertIn("Message received!", body)
        self.assertIn("From: Dana", body)
        r = self.client.post("/contact", data={"name": "  ", "message": ""})
        self.assertEqual(r.status_code, 400)
        self.assertIn("Your name must not be empty.", self.text(r))
        self.assertIn("Your message must not be empty.", self.text(r))

    def test_task5_two_forms(self):
        page = self.text(self.client.get("/demo"))
        self.assertIn('method="GET"', page)
        self.assertIn('method="POST"', page)
        self.assertIn("Course: Web", self.text(self.client.get("/demo/get?course=Web")))
        r = self.text(self.client.post("/demo/post", data={"login": "student01", "password": "secret"}))
        self.assertIn("Login: student01", r)
        self.assertNotIn("secret", r)

    def test_output_is_escaped(self):
        r = self.text(self.client.get("/search?student=<script>alert(1)</script>"))
        self.assertNotIn("<script>alert(1)</script>", r)
        self.assertIn("&lt;script&gt;", r)


if __name__ == "__main__":
    unittest.main()
