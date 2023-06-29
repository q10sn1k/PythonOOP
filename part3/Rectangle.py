class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width * self.width


rectangle = Rectangle(3, 4)
print(rectangle.area())  
print(rectangle.perimeter())  

square = Square(5)
print(square.area()) 
print(square.perimeter()) 
