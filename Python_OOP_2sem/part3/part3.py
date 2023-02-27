class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance
        self.__password = '1234'

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print('Insufficient funds')  # недостаточно средств
        else:
            self._balance -= amount

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
        else:
            print('Incorrect password')

    def get_balance(self):
        print(self._balance)

    def __get_password(self):
        return self.__password

    def show_password(self):
        return self.__password


account = BankAccount('123456789', 1000)

# вызов публичного метода
account.deposit(500)

# вызов защищенного атрибута
print(account._balance)

# попытка вызова приватного метода (вызов приведет к ошибке)
# account.__get_password()

print(account.show_password())

# изменение пароля через публичный метод
account.change_password('1234', '5678')

print(account.show_password())

#
account.deposit(900)
#

account.get_balance()

account.withdraw(1400)

account.get_balance()

account.withdraw(1400)