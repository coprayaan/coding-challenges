import os
import time

accounts = [];


def initBank():
    os.system('clear')
    print("Welcome to GHV Bank ")


def createNewUser():
    acc_holder_name = input("Please enter your name:")
    acc_holder_balance = int(input("Enter your initial balance "))
    new_account = [acc_holder_name, acc_holder_balance]
    accounts.append(new_account)


def credit_balance(account):
    amount_to_be_credited = int(input("Enter the amount to credit "))
    account[1] += amount_to_be_credited


def debit_balance(account):
    amount_to_be_debited = int(input("Enter the amount to withdraw "))
    account[1] = account[1] - amount_to_be_debited


def display_balance(account):
    print(f"{account[0]}'s Account total balance is {account[1]}")
    time.sleep(5)


def invalid_menu_selection():
    print("Please select a correct option")
    time.sleep(5)


def displayMenu():
    banking_option_selection = 0
    account = accounts[0]
    while banking_option_selection != 4:
        os.system('clear')
        print(f"Hello {account[0]}", end="\n")
        print("1. Credit", end="\n")
        print("2. Debit", end="\n")
        print("3. Show Balance", end="\n")
        print("4. Exit.", end="\n")
        banking_option_selection = int(input("Please select an option to continue!!"))
        if banking_option_selection == 1:
            credit_balance(account)
        elif banking_option_selection == 2:
            debit_balance(account)
        elif banking_option_selection == 3:
            display_balance(account)
        elif banking_option_selection == 4:
            exit()
        else:
            invalid_menu_selection()


def bank():
    initBank()
    createNewUser()
    displayMenu()


if __name__ == "__main__":
    bank()
