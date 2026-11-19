"""Task 3. Student Grade Calculator: an if / elif / else chain."""
from input_utils import read_float


def grade(score):
    """Return the letter grade, or None if the score is outside 0-100."""
    if score < 0 or score > 100:
        return None
    elif score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


def main():
    score = read_float("Enter the final score (0-100): ")
    letter = grade(score)
    if letter is None:
        print("Error: the score must be between 0 and 100.")
    else:
        print(f"Grade: {letter}")


if __name__ == "__main__":
    main()
