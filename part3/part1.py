# рассмотрим класс Person, который представляет человека и имеет свойства name и age.
# Свойство name должно быть доступно для чтения и записи, а свойство age только для чтения.

class Person:
    # self ссылается на текущий объект и используется для доступа к его атрибутам и методам.
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

#  В этом классе мы использовали два подчеркивания перед именами свойств (__name и __age).
#  Это делает эти свойства приватными, то есть они не могут быть доступны напрямую извне класса.
#  Вместо этого мы определили методы get_name, set_name и get_age, которые позволяют получать
#  и устанавливать значения этих свойств.


person = Person('Ivan', 30)
print(person.get_name())  # выводит 'Ivan'
person.set_name('Sergey')
print(person.get_name())  # выводит 'Sergey'
print(person.get_age())   # выводит 30


