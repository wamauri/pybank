from models.client import Client
from models.account import Account


amauri: Client = Client("Amauri Clementino", "amauri@pybank.com", "111.111.111-11", "02/05/2022")
polly: Client = Client("Polly Cat", "polly@pybank.com", "222.222.222-22", "03/05/2022")

# print(amauri)
# print(polly)

account_amauri: Account = Account(amauri)
print(account_amauri)
print()
account_polly: Account = Account(polly)
print(account_polly)
