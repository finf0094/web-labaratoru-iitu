"""Practical Work 9. Processing HTML forms with GET and POST (Flask).

Run:  python3 app.py   and open http://127.0.0.1:5000
"""
from flask import Flask, render_template, request

app = Flask(__name__)

OPERATIONS = {"+": "addition", "-": "subtraction", "*": "multiplication", "/": "division"}


def request_info():
    """Where the form values travelled: shown on every result page."""
    return {
        "method": request.method,
        "url": request.full_path.rstrip("?"),
        "location": "URL query string" if request.method == "GET" else "request body (form data)",
    }


@app.get("/")
def index():
    return render_template("index.html")


# Task 1. Student Search - GET
@app.get("/student-search")
def student_search_form():
    return render_template("search.html")


@app.get("/search")
def search():
    student = request.args.get("student", "").strip()
    if not student:
        return render_template("search.html", error="Please enter a student name."), 400
    return render_template("search.html", student=student, info=request_info())


# Task 2. Student Registration - POST
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    fields = {name: request.form.get(name, "").strip() for name in ("first_name", "last_name", "email")}
    missing = [name.replace("_", " ").capitalize() for name, value in fields.items() if not value]
    if missing:
        return render_template("register.html", errors=[f"{m} is required." for m in missing],
                               form=fields), 400
    return render_template("register.html", done=fields, info=request_info())


# Task 3. Simple Calculator - GET
def calculate(a, b, operation):
    """Return (result, error). The calculation happens on the server."""
    if operation not in OPERATIONS:
        return None, "Unknown operation. Choose +, -, * or /."
    if operation == "/" and b == 0:
        return None, "Error: division by zero is not allowed."
    if operation == "+":
        return a + b, None
    if operation == "-":
        return a - b, None
    if operation == "*":
        return a * b, None
    return a / b, None


def format_number(value):
    """15.0 -> '15', 2.5 -> '2.5'."""
    return str(int(value)) if float(value).is_integer() else f"{value:.10g}"


@app.get("/calculator")
def calculator_form():
    return render_template("calculator.html", operations=OPERATIONS)


@app.get("/calculate")
def calculate_view():
    raw_a, raw_b = request.args.get("a", "").strip(), request.args.get("b", "").strip()
    operation = request.args.get("operation", "")
    form = {"a": raw_a, "b": raw_b, "operation": operation}
    try:
        a, b = float(raw_a), float(raw_b)
    except ValueError:
        return render_template("calculator.html", operations=OPERATIONS, form=form,
                               error="Please enter two valid numbers.", info=request_info()), 400
    result, error = calculate(a, b, operation)
    if error:
        return render_template("calculator.html", operations=OPERATIONS, form=form,
                               error=error, info=request_info()), 400
    return render_template("calculator.html", operations=OPERATIONS, form=form,
                           result=format_number(result), info=request_info())


# Task 4. Contact Teacher - POST
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    name = request.form.get("name", "").strip()
    message = request.form.get("message", "").strip()
    errors = []
    if not name:
        errors.append("Your name must not be empty.")
    if not message:
        errors.append("Your message must not be empty.")
    if errors:
        return render_template("contact.html", errors=errors, form={"name": name, "message": message}), 400
    return render_template("contact.html", received={"name": name, "message": message}, info=request_info())


# Task 5. GET and POST on one page
@app.get("/demo")
def demo():
    return render_template("demo.html")


@app.get("/demo/get")
def demo_get():
    course = request.args.get("course", "").strip()
    return render_template("demo.html", get_result=course or "(empty)", info=request_info())


@app.post("/demo/post")
def demo_post():
    login = request.form.get("login", "").strip()
    password = request.form.get("password", "")
    return render_template("demo.html", post_result=login or "(empty)",
                           password_length=len(password), info=request_info())


if __name__ == "__main__":
    app.run(debug=True)
