# Инкапсуляция с использованием декораторов
# В Python также существует возможность использовать декораторы для определения приватных свойств класса.
# Вместо двух подчеркиваний перед именем свойства мы можем использовать декоратор @property
# для определения геттера и декоратор @<имя свойства>.setter для определения сеттера


#  Есть класс Person с закрытыми атрибутами name, age и height,
#  нам нужно иметь способ установить и получить эти значения.
#  Здесь на помощь приходят методы getter и setter.
#
#  Методы getter позволяют получать значение закрытого атрибута, а методы setter позволяют устанавливать его.
#
#  Для создания метода getter в Python используется декоратор @property,
#  а для создания метода setter используется декоратор @<имя_атрибута>.setter.

class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 and age < 120:
            self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height > 0 and height < 300:
            self.__height = height

# мы создали методы getter и setter для атрибутов name, age и height.
# Обратите внимание, что методы setter для атрибутов age и height содержат
# дополнительную проверку на допустимость значений (возраст должен быть в диапазоне от 0 до 120 лет,
# а рост - от 0 до 300 сантиметров).


person = Person("Ivan", 25, 180)
print(person.name)  # выводит "Ivan"
person.name = "Sergey"
print(person.name)  # выводит "Sergey"
print(person.age)  # выводит 25
person.age = 130  # возраст не изменится
print(person.age)  # выводит 25
print(person.height)  # выводит 180
person.height = 180  # рост не изменится
print(person.height)  # выводит 180
