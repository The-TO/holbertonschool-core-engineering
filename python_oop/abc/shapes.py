#!/usr/bin/env python3
"""MOdule definisssanrt des figures"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Classe abstraite permettant de definir les formes"""
    @abstractmethod
    def area(self):
        """Defini l'aire"""
        pass
    @abstractmethod
    def perimeter(self):
        """Defini le perimetre"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return self.radius * 2 * math.pi

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

def shape_info(shape):
    print ("Area: {}".format(shape.area()))
    print ("Perimeter: {}".format(shape.perimeter()))

circle = Circle(5)
rectangle = Rectangle(4, 7)

shape_info(circle)
shape_info(rectangle)