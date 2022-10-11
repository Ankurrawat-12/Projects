# Abstract Base Class & @abstractmethod

# from abc import ABCMeta, abstractmethod  # for below Python 3.4
from abc import ABC, abstractmethod


class Shape(ABC):  # <- for python 3.4 and above / class Shape(metaclass=ABCMeta): -> for python 3.4 and lower
    @abstractmethod
    def print_area(self):
        return 0
#     you can't make objects of abstract base class


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def print_area(self):
        return self.length * self.breadth


rect1 = Rectangle(10, 5)
print(rect1.print_area())
