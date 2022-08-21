from models.client import Client
from models.account import Account


joao: Client = Client('João', 'joao@gmail.com', '123456', '16/12/2003')
jennifer: Client = Client('Jennifer', 'jennifer@gmail.com', '654321', '05/08/2003')

# print(joao)
# print(jennifer)

accountA: Account = Account(joao)
accountB: Account = Account(jennifer)

print(accountA)
print(accountB)
