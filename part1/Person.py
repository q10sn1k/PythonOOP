# методы классов
'''
class Person:
    def say_hello(self):
        print('Hello')
'''


'''
class Person:
    def say(self, message):
        print(message)
        
        
Fedor = Person()
Fedor.say("hello I`m Fedor")
'''


'''
class Person:
    # конструктор
    def __init__(self):
        print("Создание объекта Person")

    def say_hello(self):
        print("Hello")


Fedor = Person()  # Создание объекта Person
Fedor.say_hello()  # Hello
'''


# атрибуты объекта
class Person:
    # конструктор
    def __init__(self, name):
        self.name = name  # имя человека
        self.age = 20  # возраст человека

    def say_hello(self):
        print("Hello")


Fedor = Person('Fedor')  # Создание объекта Person и передача атрибута name со значением Fedor
print(Fedor.name)
print(Fedor.age)

Fedor.age = 25
print(Fedor.age)


