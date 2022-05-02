from models.client import Client
from utils.helper import format_float_to_str_currency


class Account:

    account_code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__account_number: int = Account.account_code
        self.__client: Client = client
        self.__balance: float = 0.0
        self.__limit: float = 100.00
        self.__total_balance: float = self._calculate_total_balance
        Account.account_code += 1

    def __str__(self: object) -> str:
        return (
            f"Account Number: {self.account_number}\n"
            f"Client Name: {self.client.name}\n"
            f"Total Balance: {format_float_to_str_currency(self.total_balance)}")

    @property
    def account_number(self: object) -> int:
        return self.__account_number

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
    def total_balance(self: object) -> float:
        return self.__total_balance

    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        pass

    def withdraw(self: object, value: float) -> None:
        pass

    def transfer(self: object, desti_account: object, value: float) -> None:
        pass
