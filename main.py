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
    if len(accounts) > 0:
        account_number: int = int(input('Insert your account number: '))

        account: Account = search_account_by_number(account_number)

        if account:
            amount: float = float(input('Insert the amount you want to withdraw: '))
            account.withdraw(amount)
        else:
            print(f"We couldn't find any account with {account_number}")
    else:
        print('No accounts registered!')
    sleep(2)
    menu()


def deposit() -> None:
    if len(accounts) > 0:
        account_number: int = int(input('Insert your account number: '))

        account: Account = search_account_by_number(account_number)

        if account:
            amount: float = float(input('Insert the amount you want to deposit: '))
            account.deposit(amount)
        else:
            print(f"We couldn't find any account with {account_number}")
    else:
        print('No accounts registered!')
    sleep(2)
    menu()


def transfer() -> None:
    if len(accounts) > 0:
        sender_account_number: int = int(input('Insert your account number: '))

        sender_account: Account = search_account_by_number(sender_account_number)

        if sender_account:
            recipient_account_number: int = int(input("Insert the recipient account's number: "))

            recipient_account: Account = search_account_by_number(recipient_account_number)

            if recipient_account:
                amount: float = float(input('Insert the amount you want to transfer: '))
                sender_account.transfer(recipient_account, amount)
            else:
                print(f"We couldn't find any account with {recipient_account_number}")
        else:
            print(f"We couldn't find any account with {sender_account_number}")
    else:
        print('No accounts registered!')
    sleep(2)
    menu()


def list_accounts() -> None:
    pass


def search_account_by_number(number: int) -> Account:
    pass


if __name__ == '__main__':
    main()
