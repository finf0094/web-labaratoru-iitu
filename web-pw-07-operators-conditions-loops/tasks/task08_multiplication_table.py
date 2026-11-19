"""Task 8. Multiplication Table from 1 to 10 with a for loop."""
from input_utils import read_int


def multiplication_table(number):
    lines = []
    for i in range(1, 11):
        lines.append(f"{number} × {i} = {number * i}")
    return lines


def main():
    number = read_int("Enter an integer: ")
    for line in multiplication_table(number):
        print(line)


if __name__ == "__main__":
    main()
