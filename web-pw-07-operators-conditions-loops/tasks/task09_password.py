"""Task 9. Password Verification.

Python has no do...while, so the equivalent is `while True` with `break`:
the body always runs at least once, and the condition is checked at the end.
"""
CORRECT_PASSWORD = "java123"  # fixed by the assignment (educational example only)


def main():
    while True:
        password = input("Enter the password: ")
        if password == CORRECT_PASSWORD:
            break
        print("Wrong password, try again.")
    print("Access granted")


if __name__ == "__main__":
    main()
