class Person:

    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")




Fedor = Person('Fedor')
Fedor.age = 25
Fedor.display_info()

Ivan = Person('Ivan')
Ivan.age = 30
Ivan.display_info()