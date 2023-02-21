# Аннотации свойств
class Person:
    def __init__(self, name):
        self.__name = name  # устанавливаем имя
        self.__age = 1  # устанавливаем возраст

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")


    @property
    def name(self):
        return self.__name


    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


Fedor = Person('Fedor')
Fedor.display_info()
Fedor.age = -25
print(Fedor.age) # 1
Fedor.age = 25
Fedor.display_info()