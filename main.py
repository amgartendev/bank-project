from typing import List
from time import sleep
from models.client import Client
from models.account import Account


accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print("====================================")
    print("==============   ATM  ==============")
    print("====================================")

    print('Select an option: ')
    print('1 - Create Account')
    print('2 - Withdrawal')
    print('3 - Deposit')
    print('4 - Transfer')
    print('5 - List Accounts')
    print('6 - Exit')

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        withdrawal()
    elif option == 3:
        deposit()
    elif option == 4:
        transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('See you!')
        sleep(2)
        exit(0)
    else:
        print('Error: Select a valid option!')
        sleep(2)
        menu()


def create_account() -> None:
    print("Insert the client's informations: ")

    name: str = input('Name: ')
    email: str = input('Email: ')
    id_card: str = input('ID Card: ')
    birth_date: str = input('Birth Date: ')

    client: Client = Client(name, email, id_card, birth_date)
    account: Account = Account(client)
    accounts.append(account)

    print('Account created successfully!')
    print('Account informations: ')
    print('------------------------')
    print(account)
    sleep(2)
    menu()


def withdrawal() -> None:
    pass


def deposit() -> None:
    pass


def transfer() -> None:
    pass


def list_accounts() -> None:
    pass


def search_account_by_number(number: int) -> Account:
    pass


if __name__ == '__main__':
    main()
