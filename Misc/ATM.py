import os
import time


def bank():
    print("Hello ")
    acc_holder_name = input("Please enter your name:")
    acc_holder_balance = int(input("Enter your initial balance "))
    banking_option_selection = 0
    while banking_option_selection != 4:
        os.system('clear')
        print(f"Hello {acc_holder_name}", end="\n")
        print("1. Credit", end="\n")
        print("2. Debit", end="\n")
        print("3. Show Balance", end="\n")
        print("4. Exit.", end="\n")
        banking_option_selection = int(input("Please select an option to continue!!"))
        if banking_option_selection == 1:
            amount_to_be_credited = int(input("Enter your initial balance "))
            acc_holder_balance += amount_to_be_credited
        elif banking_option_selection == 2:
            amount_to_be_debited = int(input("Enter your initial balance "))
            acc_holder_balance -= amount_to_be_debited
        elif banking_option_selection == 3:
            print(f"Total balance in your account is {acc_holder_balance}")
            time.sleep(5)
        elif banking_option_selection == 4:
            exit()
        else:
            print("Please select a correct option")
            time.sleep(5)


if __name__ == "__main__":
    bank()
