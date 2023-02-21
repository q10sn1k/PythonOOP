'''
class Person:

    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")


Fedor = Person('Fedor')
Fedor.age = 25
Fedor.display_info()
'''


# Инкапсуляция предотвращает прямой доступ к атрибутам объекта реализованного класса
# Инкапсуляция — ограничение доступа к составляющим объект компонентам (методам и переменным)
# для того, чтобы сделать атрибут приватным  в начале него ставится двойное нижнее подчеркивание __
class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1  # устанавливаем возраст


    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")


    def get_age(self):
        return self.__age


    def get_name(self):
        return self.__name


    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


Fedor = Person('Fedor')
Fedor.display_info()
# Fedor.age = 25 # значение атрибута не изменится
# Fedor.display_info()

Fedor.set_age(-25) # Недопустимый возраст (не пройдена валидация)

Fedor.set_age(25)
Fedor.display_info()

# print(Fedor.age) # приведет к ошибке поскольку атрибут age приватный
Fedor.display_info()

print(Fedor.get_age())
print(Fedor.get_name())

