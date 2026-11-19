"""Task 6. Numbers from 1 to N with a for loop."""
from input_utils import read_int


def numbers_up_to(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(str(i))
    return ", ".join(numbers)


def main():
    n = read_int("Enter a positive integer N: ", minimum=1)
    print(numbers_up_to(n))


if __name__ == "__main__":
    main()
