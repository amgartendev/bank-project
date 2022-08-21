from models.client import Client
from utils.helper import format_float_str


class Account:
    counter: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__id: int = Account.counter
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.0
        self.__total: float = self.calculate_total_balance
        Account.counter += 1

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total(self: object) -> float:
        return self.__total

    @total.setter
    def total(self: object, amount: float) -> None:
        self.__total = amount

    @property
    def calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def __str__(self: object) -> str:
        return f'ID: {self.id}\nClient: {self.client.name}\nTotal Balance: {format_float_str(self.total)}'

    def deposit(self: object, amount: float) -> None:
        if amount > 0:
            self.balance = self.balance + amount
            self.total = self.calculate_total_balance
            print(f'You deposited £ {amount:.2f} to your account!')
        else:
            print('Error: Insert a valid amount to deposit!')

    def withdraw(self: object, amount: float) -> None:
        if self.total >= amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.total = self.calculate_total_balance
            else:
                remaining: float = self.balance - amount
                self.limit = self.limit + remaining
                self.balance = 0
                self.total = self.calculate_total_balance
                print(f'You with withdrew £ {amount}')
        else:
            print(f"You can't withdraw {amount}!")

    def transfer(self: object, recipient: object, amount: float) -> None:
        pass
