"""Helpers for reading user input safely: they ask again until the value is valid."""


def read_int(prompt, minimum=None, maximum=None):
    """Read an integer; repeat the question on text or on a value outside [minimum, maximum]."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"The number must be at least {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"The number must be at most {maximum}.")
        else:
            return value


def read_float(prompt):
    """Read a number (integer or decimal); repeat the question on invalid text."""
    while True:
        text = input(prompt).strip().replace(",", ".")
        try:
            return float(text)
        except ValueError:
            print("Please enter a number.")


def read_yes_no(prompt):
    """Read yes/no (also y/n); return True for yes."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please answer yes or no.")
