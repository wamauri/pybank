from calendar import c
from datetime import datetime, time
from typing import List
from time import sleep

from models.client import Client
from models.account import Account


accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print("+----------------------------------------+")
    print("|<<<<<<<<<<<<<<<<<< ATM >>>>>>>>>>>>>>>>>|")
    print("|<<<<<<<<<<<<<<<<< PyBank >>>>>>>>>>>>>>>|")
    print("+----------------------------------------+\n")

    print("Select an option in menu:")
    print("+-----------------------+")
    print("| 1 - Create Account    |")
    print("| 2 - Withdraw          |")
    print("| 3 - Deposit           |")
    print("| 4 - Transfer          |")
    print("| 5 - View Accounts     |")
    print("| 6 - Exit              |")
    print("+-----------------------+\n")

    option: int = int(input("Type an option: "))
    print()

    if option == 1:
        create_account()
    elif option == 2:
        make_withdraw()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        greeting()
        sleep(2)
        exit(0)
    else:
        print("Invalid Option. Try again.")
        sleep(2)
        menu()


def create_account() -> None:
    print("To create a PyBank account, type the client informations:")

    name: str = input("Client name: ")
    email: str = input("Client email: ")
    cpf: str = input("Client cpf (format -> 000.000.000-00): ")
    birth_date: str = input("Client birth date (format -> DD/MM/YYYY): ")

    client: Client = Client(
        name=name, email=email, 
        cpf=cpf, birth_date=birth_date)

    account: Account = Account(client=client)

    accounts.append(account)

    print("The account was successfully created!")
    print("Account: ")
    print("---------------------------------------------------------")
    print(account)
    sleep(2)
    menu()


def make_withdraw() -> None:
    if len(accounts) > 0:
        account_number: int = int(input("Type your account number: "))

        account: Account = get_account_by_account_number(account_number)

        if account:
            message: str = "Enter the withdrawal amount (format -> 10.00): "
            value: float = float(input(message))

            account.withdraw(value=value)
        else:
            print(f"Account with account number {account_number} not found.")
    else:
        print("No accounts have been created yet.")
    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        account_number: int = int(input("Type your account number: "))

        account: Account = get_account_by_account_number(account_number)

        if account:
            message: str = "Enter the deposit amount (format -> 10.00): "
            value: float = float(input(message))

            account.deposit(value=value)
        else:
            print(f"Account with account number {account_number} not found.")
    else:
        print("No accounts have been created yet.")
    sleep(2)
    menu()


def make_transfer() -> None:
    if len(accounts) > 0:
        origin_number: int = int(input("Type your account number: "))

        origin_account: Account = get_account_by_account_number(
            account_number=origin_number)

        if origin_account:
            message: str = "Type the destination account number: "
            destination_number: int = int(input(message))

            destination_account: Account = get_account_by_account_number(
                account_number=destination_number)

            if destination_account:
                value: float = float(input("Type the transfer amount: "))

                origin_account.transfer(
                    desti_account=destination_account, 
                    value=value)
            else:
                print(f"The destination account with number \
                    {destination_number} wasn't found.")
        else:
            print(f"Account with number {origin_number} was not found.")
    else:
        print("No accounts have been created yet.")
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print("Account Listing:\n")

        for account in accounts:
            print(account)
            print("--------------------")
            sleep(1)
    else:
        print("No accounts have been created yet.")
    sleep(2)
    menu()


def get_account_by_account_number(account_number: int) -> Account:
    acc: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.account_number == account_number:
                acc = account

    return acc


def greeting() -> None:
    now = datetime.now()
    now_time = now.time()

    if now_time <= time(00,00) or now_time >= time(18,00):
        print("Thanks for using PyBank! Have a good night.")
    else:
        print("Thanks for using PyBank! Have a good day.")


if __name__ == "__main__":
    main()

