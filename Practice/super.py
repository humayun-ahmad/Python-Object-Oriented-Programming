
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not filled'}")
    

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # Corrected call to superclass
        self.radius = radius
    
    def describe(self):
        print(f"Area of the circle is {3.1416 * self.radius * self.radius}")
        super().describe()

# class eclepse(Circle):
#     def __init__(self, color, is_filled, major_axis, minor_axis):
#         super().__init__(color, is_filled, radius)
#         self.major_axis = major_axis
#         self.minor_axis = minor_axis


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

# class Square(Shape):
#     def __init__(self, color, is_filled, width):
#         super().__init__(color, is_filled)
#         self.width = width

# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="green", is_filled=False, width=10)
triangle = Triangle(color="blue", is_filled=True, width = 10, height=10)

# print(f"square color is {square.color} and width is {square.width}")
# print(f"Triangle color is {triangle.color} and width is {triangle.width}")

circle.describe()

square.describe()


