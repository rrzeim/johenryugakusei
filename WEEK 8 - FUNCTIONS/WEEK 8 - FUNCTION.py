def get_the_sum(input1, input2):
    result = input1 + input2
    print(result)
    return result

a = 30
b = 40
c = 40
d = 20

print(get_the_sum(a, b) + get_the_sum(c, d))

def get_the_sum(input1, input2):
    result = input1 + input2
    print(result)
    return result

a = 30
b = 40
c = 40
d = 20

print(get_the_sum(a, b) + get_the_sum(c, d))


import time
import sys

def start_countdown():
    print("Review session will start in...")

    for i in range(20, 0, -1):
        sys.stdout.write(f"\r{i} seconds remaining...")
        sys.stdout.flush()
        time.sleep(1)

    print("The review session is starting. Let's begin.")


start_countdown()


welcome_messages():
card_reader(isCardInserted):
input_and_validate_pin_number(pinNumber): return isValid
transaction_selection(transaction):
amount_and_account_selection(amount):
transaction_validation(amount, balance) return isValid
card_ejection():
cash_dispensing():
print_receipt(balance, amount):

amount = 0
balance = 9999999

welcome_message():


import time
import os


# Function to clear console (Windows only)
def clear_console():
    os.system('cls')


# Welcome message function
def welcome_message():
    print("Welcome to ECE 1-4 Bank of the Philippines")
    time.sleep(1)
    print("-------------")
    time.sleep(1)
    print("Kindly insert your card\n")


# Card reader function
def card_reader():
    user_input = input("Is the card inserted? (yes/no): ").lower()
    if user_input == "yes":
        print("\nCard is inserted\n")
        return True
    else:
        print("\nNo card detected. Please insert your card.\n")
        return False


# PIN input and validation
def input_and_validate_pin_number():
    correct_pin = "12345"
    attempts = 3

    for i in range(attempts):
        pin = input("Enter your PIN: ")  # User types PIN here
        if pin == correct_pin:
            print("\nPIN correct!\n")
            return True
        else:
            print("Incorrect PIN. Try again.\n")
    print("Too many incorrect attempts. Transaction cancelled.\n")
    return False


# Initial balance and amount
amount = 0
balance = 99999999999


clear_console()
welcome_message()

if card_reader():
    if input_and_validate_pin_number():
        print("Next step: Select your transaction.\n")
    else:
        print("Please contact your bank for assistance.\n")
else:
    print("Transaction cannot proceed without a card.\n")

def transaction_selection():
    print("\nTransaction types:")
    print("1. Withdrawal")
    print("2. Balance Inquiry")
    print("3. Deposit")

    choice = input("Select a transaction (type 1, 2, or 3): ")
    return choice

transaction = transaction_selection()

if transaction == "1":
    print("You chose Withdrawal")
elif transaction == "2":
    print("You chose Balance Inquiry")
elif transaction == "3":
    print("You chose Deposit")
else:
    print("Invalid selection")
# 1. Define the function first
def transaction_selection():
    print("\nTransaction types:")
    print("1. Withdrawal")
    print("2. Balance Inquiry")
    print("3. Deposit")

    choice = input("Select a transaction (type 1, 2, or 3): ")
    return choice


# ----------------- ATM Withdrawal Only -----------------
# ----------------- ATM Withdrawal with Receipt and Card Ejection -----------------
balance = 1000  # Example starting balance

print(f"Your current balance is: ${balance}\n")

while True:
    try:
        withdraw_amount = float(input("Enter the amount to withdraw: "))

        if withdraw_amount <= 0:
            print("Amount must be greater than 0.\n")
            continue

        if withdraw_amount > balance:
            print("Insufficient balance! Try a smaller amount.\n")
            continue

        # Successful withdrawal
        balance -= withdraw_amount
        print(f"\n${withdraw_amount} withdrawn successfully.")
        print(f"Remaining balance: ${balance}\n")

        # Print receipt
        print("----- RECEIPT -----")
        print(f"Withdrawn amount: ${withdraw_amount}")
        print(f"Remaining balance: ${balance}")
        print("-------------------\n")

        # Card ejection
        print("Card is ejected. Please take your card.\n")
        print("Thank you for using the ATM!")
        break

    except ValueError:
        print("Invalid input. Please enter a numeric value.\n")
