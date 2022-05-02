from datetime import date

from utils.helper import date_to_str, str_to_date


class Client:
    counter: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, birth_date: str) -> None:
        self.__client_code: int = Client.counter
        self.__name: str = name
        self.__email: str = email
        self.__cpf: str = cpf
        self.__birth_date: date = str_to_date(birth_date)
        self.__created: date = date.today()
        Client.counter += 1

    def __str__(self: object) -> str:
        return (
            f"Client Code: {self.client_code}\n" 
            f"Client Name: {self.name}\n" 
            f"Client Birth Date: {self.birth_date}\n"
            f"Account Created: {self.created}")

    @property
    def client_code(self: object) -> int:
        return self.__client_code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def birth_date(self: object) -> str:
        return date_to_str(self.__birth_date)

    @property
    def created(self: object) -> str:
        return date_to_str(self.__created)
