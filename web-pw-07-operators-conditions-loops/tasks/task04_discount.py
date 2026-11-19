"""Task 4. Discount Calculator: ranges of the purchase amount give the discount."""
from input_utils import read_float


def discount_percent(amount):
    if amount < 10_000:
        return 0
    elif amount < 50_000:
        return 5
    elif amount < 100_000:
        return 10
    else:
        return 15


def final_price(amount):
    return amount - amount * discount_percent(amount) / 100


def main():
    amount = read_float("Enter the purchase amount (KZT): ")
    while amount < 0:
        print("The amount cannot be negative.")
        amount = read_float("Enter the purchase amount (KZT): ")
    percent = discount_percent(amount)
    print(f"Original amount: {amount:,.2f} KZT")
    print(f"Discount: {percent}%")
    print(f"Final amount: {final_price(amount):,.2f} KZT")


if __name__ == "__main__":
    main()
