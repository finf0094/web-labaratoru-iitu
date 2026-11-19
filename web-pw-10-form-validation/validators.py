"""Server-side validation rules. Each function returns (clean_value, error_message or None)."""
import re

# local part @ domain . top-level domain (at least two letters); no spaces
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$")
INTEGER_PATTERN = re.compile(r"^[+-]?\d+$")
DECIMAL_PATTERN = re.compile(r"^[+-]?\d+[.,]\d+$")
MIN_AGE, MAX_AGE = 18, 100


def validate_name(raw):
    name = (raw or "").strip()  # "   " becomes "" and is rejected like an empty field
    if not name:
        return name, "Name is required!"
    return name, None


def validate_email(raw):
    email = (raw or "").strip()
    if not email or not EMAIL_PATTERN.match(email):
        return email, "Invalid email!"
    return email, None


def validate_age(raw):
    text = (raw or "").strip()
    if not text:
        return None, "Age is required!"           # 1. presence
    if DECIMAL_PATTERN.match(text):
        return None, "Age must be a whole number!"
    if not INTEGER_PATTERN.match(text):
        return None, "Age must be a number!"      # 2. type
    age = int(text)
    if not MIN_AGE <= age <= MAX_AGE:
        return age, f"Age must be between {MIN_AGE} and {MAX_AGE}!"  # 3. range
    return age, None


def validate_registration(form):
    """Validate every field independently and collect ALL errors (Task 4)."""
    name, name_error = validate_name(form.get("student"))
    email, email_error = validate_email(form.get("email"))
    age, age_error = validate_age(form.get("age"))
    errors = [e for e in (name_error, email_error, age_error) if e]
    return {"student": name, "email": email, "age": age}, errors
