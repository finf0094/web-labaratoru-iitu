"""Practical Work 10. Form validation and data processing (Flask).

All validation runs on the server (validators.py); HTML attributes in Task 5 are only a convenience.
Run:  python3 app.py   and open http://127.0.0.1:5000
"""
from flask import Flask, render_template, request

from validators import validate_age, validate_email, validate_name, validate_registration

app = Flask(__name__)

SINGLE_FIELD_TASKS = {
    1: {"title": "Task 1. Student Registration (required name)", "field": "student", "label": "Student Name",
        "type": "text", "validate": validate_name, "success": "Welcome, {value}!"},
    2: {"title": "Task 2. Email Validation", "field": "email", "label": "Email",
        "type": "text", "validate": validate_email, "success": "Valid email!"},
    3: {"title": "Task 3. Age Validation (18-100)", "field": "age", "label": "Age",
        "type": "text", "validate": validate_age, "success": "Valid age!"},
}


@app.get("/")
def index():
    return render_template("index.html", tasks=SINGLE_FIELD_TASKS)


@app.route("/task<int:number>", methods=["GET", "POST"])
def single_field_task(number):
    task = SINGLE_FIELD_TASKS.get(number)
    if task is None:
        return "Not found", 404
    if request.method == "GET":
        return render_template("single.html", task=task, number=number)
    raw = request.form.get(task["field"], "")
    value, error = task["validate"](raw)
    if error:
        return render_template("single.html", task=task, number=number, error=error, raw=raw), 400
    return render_template("single.html", task=task, number=number, raw=raw,
                           success=task["success"].format(value=value))


def registration_page(endpoint, title, browser_validation):
    if request.method == "GET":
        return render_template("registration.html", endpoint=endpoint, title=title,
                               browser_validation=browser_validation, form={})
    data, errors = validate_registration(request.form)
    raw = {key: request.form.get(key, "") for key in ("student", "email", "age")}
    if errors:
        return render_template("registration.html", endpoint=endpoint, title=title,
                               browser_validation=browser_validation, form=raw, errors=errors), 400
    return render_template("registration.html", endpoint=endpoint, title=title,
                           browser_validation=browser_validation, form=raw, valid=data)


@app.route("/task4", methods=["GET", "POST"])
def task4():
    return registration_page("task4", "Task 4. Complete Student Registration Form", browser_validation=False)


@app.route("/task5", methods=["GET", "POST"])
def task5():
    """Part A: the same form with HTML validation attributes (required, type=email, min/max)."""
    return registration_page("task5", "Task 5A. With client-side (HTML) validation", browser_validation=True)


@app.route("/task5/without-html-validation", methods=["GET", "POST"])
def task5_without_html():
    """Part B: attributes removed, so invalid values reach the server, which still rejects them."""
    return registration_page("task5_without_html", "Task 5B. HTML validation removed", browser_validation=False)


if __name__ == "__main__":
    app.run(debug=True)
