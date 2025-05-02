# Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

# ABC = Abstract Base Class
class Shape(ABC): 
    @abstractmethod
    def area(self): # This is an abstract method
        pass

# child class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 
          


rect_area = Rectangle(6, 15)
print("Area of Rectangle:", rect_area.area())

# Output: 
# Area of Rectangle: 90




