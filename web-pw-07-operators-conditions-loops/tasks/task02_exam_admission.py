"""Task 2. Exam Admission: a comparison operator combined with the logical operator and."""
from input_utils import read_float, read_yes_no

MIN_ATTENDANCE = 70


def is_admitted(attendance, project_done):
    return attendance >= MIN_ATTENDANCE and project_done


def main():
    attendance = read_float("Enter attendance in percent (0-100): ")
    while not 0 <= attendance <= 100:
        print("Attendance must be between 0 and 100.")
        attendance = read_float("Enter attendance in percent (0-100): ")
    project_done = read_yes_no("Has the student completed the project? (yes/no): ")
    if is_admitted(attendance, project_done):
        print("Allowed to exam")
    else:
        print("Not allowed")


if __name__ == "__main__":
    main()
