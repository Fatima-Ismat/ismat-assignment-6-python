from abc import ABC, abstractmethod
class Shape(ABC):
     @abstractmethod
     def area(self):
          pass
class Rectangle(Shape):
     def __init__(self,  length, width):
          self.length = length
          self.width = width

     def area(self):
          return self.length * self.width
     
rect = Rectangle(5, 8)
print("Area of rectangle:", rect.area())


