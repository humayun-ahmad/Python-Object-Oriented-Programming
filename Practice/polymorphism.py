# Polymorphism = Greek word that means to "have many forms or faces"
# Poly = Many
# Morphe Form
# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck typing" = Object must have necessary attributes/methods

# ----------------------------------------------------------------

# How to add superscripts ²
# Windows: Alt + 0178
# Mac: Control + windows + space


from abc import ABC, abstractmethod


class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# circle = Circle()
# square = Square()

shapes = [Circle(4), Square(5), Triangle(6, 7)]

for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area()} cm²")
