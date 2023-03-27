"""
Необходимо разработать программу, которая будет реализовывать классы Rectangle и Square,
описывающие прямоугольник (Rectangle) и квадрат (Square), а также демонстрировать наследование классов
и переопределение методов.
Класс Square должен быть унаследован от класса Rectangle,
а также переопределять методы area и perimeter для корректной работы с квадратами.
После необходимо создать объекты Rectangle и Square, вызвать их методы area и perimeter и вывести результат на экран.
"""


# Определяем класс Rectangle
class Rectangle:
    # Определяем метод __init__ (конструктор), который будет вызван при создании нового объекта
    def __init__(self, length, width):
        # Задаем атрибуты объекта: длину и ширину прямоугольника
        self.length = length
        self.width = width

    # Определяем метод area, который будет возвращать площадь прямоугольника
    def area(self):
        return self.length * self.width

    # Определяем метод perimeter, который будет возвращать периметр прямоугольника
    def perimeter(self):
        return 2 * (self.length + self.width)


# Определяем класс Square, который будет наследоваться от класса Rectangle
class Square(Rectangle):
    # Определяем метод __init__, который будет вызываться при создании нового объекта
    # Классу Square передается только один параметр, так как все стороны квадрата равны
    def __init__(self, side):
        # Вызываем конструктор родительского класса и передаем ему значение стороны квадрата для обоих атрибутов
        super().__init__(side, side)

    # Переопределяем метод area для класса Square, чтобы он возвращал площадь квадрата
    def area(self):
        return self.length ** 2

    # Переопределяем метод perimeter для класса Square, чтобы он возвращал периметр квадрата
    def perimeter(self):
        return 4 * self.length


# Создаем объекты классов Rectangle и Square
rectangle1 = Rectangle(10, 20)
rectangle2 = Square(10)

# Выводим на экран площадь и периметр каждого прямоугольника
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle2.area())
print(rectangle2.perimeter())
