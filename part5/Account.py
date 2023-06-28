class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

class CreditCard(Account):
    def charge_interest(self, interest_rate):
        interest = self.balance * interest_rate
        self.balance += interest

class SavingsAccount(Account):
    def add_interest(self, interest_rate):
        interest = self.balance * interest_rate
        self.balance += interest


account = Account(1000)
account.deposit(500)
account.withdraw(200)
print(account.balance)  

credit_card = CreditCard(1000)
credit_card.deposit(500)
credit_card.withdraw(200)
credit_card.charge_interest(0.1)
print(credit_card.balance)

savings_account = SavingsAccount(1000)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.add_interest(0.05)
print(savings_account.balance)
