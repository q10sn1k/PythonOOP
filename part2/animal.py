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
animal.speak()  
animal.eat()  

cat = Cat("Barsik")
cat.speak() 
cat.eat()  
cat.catch_mice()  

dog = Dog("Sharik")
dog.speak()  
dog.eat()  
dog.fetch_ball()  
