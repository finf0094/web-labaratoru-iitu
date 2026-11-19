"""Task 10. ATM Simulator: a menu loop with if / elif / else inside."""
from input_utils import read_float

INITIAL_BALANCE = 100_000


def deposit(balance, amount):
    """Return (new_balance, message). Zero or negative amounts are rejected."""
    if amount <= 0:
        return balance, "Error: the amount must be greater than zero."
    balance += amount
    return balance, f"Deposited {amount:,.2f} KZT. New balance: {balance:,.2f} KZT"


def withdraw(balance, amount):
    """Return (new_balance, message). Withdraws only if the funds are sufficient."""
    if amount <= 0:
        return balance, "Error: the amount must be greater than zero."
    if amount > balance:
        return balance, "Error: insufficient funds."
    balance -= amount
    return balance, f"Withdrew {amount:,.2f} KZT. New balance: {balance:,.2f} KZT"


def main():
    balance = INITIAL_BALANCE
    while True:
        print()
        print("1. Check balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            print(f"Balance: {balance:,.2f} KZT")
        elif choice == "2":
            balance, message = deposit(balance, read_float("Deposit amount (KZT): "))
            print(message)
        elif choice == "3":
            balance, message = withdraw(balance, read_float("Withdrawal amount (KZT): "))
            print(message)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: invalid menu choice. Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
