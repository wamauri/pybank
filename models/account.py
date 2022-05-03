from distutils.log import debug
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

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def _calculate_total_balance(self: object) -> float:
        return self.balance + self.limit

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.total_balance = self._calculate_total_balance
            print("Deposit made successfully.")
        else:
            print(f"Error. {value} needs to be greater than 0.")

    def withdraw(self: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.limit + remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance
                print("Withdrawal made successfullt.")
        else:
            print("Withdrawal not made. Try again.")

    def transfer(self: object, desti_account: object, value: float) -> None:
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calculate_total_balance

                desti_account.balance = desti_account.balance + value
                total_balance: float = desti_account._calculate_total_balance
                desti_account.total_balance = total_balance
            else:
                remaining: float = self.balance - value
                self.limit = self.limit + remaining
                self.balance = 0
                self.total_balance = self._calculate_total_balance

                desti_account.balance = desti_account.balance + value
                total_balance: float = desti_account._calculate_total_balance
                desti_account.total_balance = total_balance
            print("Transfer made successfullt.")
        else:
            print("Transfer not made. Try again.")

