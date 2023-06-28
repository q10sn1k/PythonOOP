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
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
        
    def say_hello(self):
        print("Hello")


person = Person("Timofey", 20)
person.say_hello()
print(person.get_name()) 
print(person.get_age())

