"""Task 5. Day of the Week: match / case is Python's switch statement (Python 3.10+)."""
from input_utils import read_int


def day_name(number):
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number"


def main():
    number = read_int("Enter a number from 1 to 7: ")
    print(day_name(number))


if __name__ == "__main__":
    main()
