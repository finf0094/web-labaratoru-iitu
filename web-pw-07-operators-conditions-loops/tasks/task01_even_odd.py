"""Task 1. Even or Odd Number: the remainder operator % decides."""
from input_utils import read_int


def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


def main():
    number = read_int("Enter an integer: ")
    print(f"{number} is {even_or_odd(number)}.")


if __name__ == "__main__":
    main()
