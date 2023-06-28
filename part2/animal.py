class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Животное говорит")

    def eat(self):
        print("животное ест")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("МЯУ!")

    def catch_mice(self):
        print("кошка ловит мышку")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("ГАВ!")

    def fetch_ball(self):
        print("собака ловит мяч")


animal = Animal("Generic animal")
animal.speak()  # Вывод: Animal speaks
animal.eat()  # Вывод: Animal eats

cat = Cat("Barsik")
cat.speak()  # Вывод: Meow!
cat.eat()  # Вывод: Animal eats
cat.catch_mice()  # Вывод: Cat catches mice

dog = Dog("Sharik")
dog.speak()  # Вывод: Woof!
dog.eat()  # Вывод: Animal eats
dog.fetch_ball()  # Вывод: Dog fetches ball
