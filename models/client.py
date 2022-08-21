from datetime import date
from utils.helper import date_to_str, str_to_date


class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, id_card: str, birth_date: str) -> None:
        self.__id: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__id_card: str = id_card
        self.__birth_date: date = str_to_date(birth_date)
        self.__register_date: date = date.today()
        Client.counter += 1

    @property
    def id(self: object) -> int:
        return self.__id

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def id_card(self: object) -> str:
        return self.__id_card

    @property
    def birth_date(self: object) -> str:
        return date_to_str(self.__birth_date)

    @property
    def register_date(self: object) -> str:
        return date_to_str(self.__register_date)

    def __str__(self: object) -> str:
        return f'ID: {self.id}\nName: {self.name}\nBirth Date: {self.birth_date}\n' \
               f'Register Date: {self.register_date}'
