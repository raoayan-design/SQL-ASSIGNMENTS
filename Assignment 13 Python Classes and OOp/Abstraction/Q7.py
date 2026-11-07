# Q7 - Shape Calculator (Abstraction)

from abc import ABC, abstractmethod

PI = 3.14159


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if isinstance(radius, bool) or not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2

    def perimeter(self):
        return 2 * PI * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        for value in (width, height):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
                raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print(f"Circle area: {circle.area():.2f}")
    print(f"Circle perimeter: {circle.perimeter():.2f}")
    print(f"Rectangle area: {rectangle.area():.2f}")
    print(f"Rectangle perimeter: {rectangle.perimeter():.2f}")

    try:
        shape = Shape()
    except TypeError as error:
        print(f"Cannot instantiate Shape: {error}")

    # Shape is abstract, so Python prevents creating its object directly.
