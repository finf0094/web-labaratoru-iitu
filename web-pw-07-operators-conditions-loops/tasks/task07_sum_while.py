"""Task 7. Sum of Numbers from 1 to N with a while loop."""
from input_utils import read_int


def sum_up_to(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def main():
    n = read_int("Enter a positive integer N: ", minimum=1)
    print(f"Sum of numbers from 1 to {n} = {sum_up_to(n)}")


if __name__ == "__main__":
    main()
