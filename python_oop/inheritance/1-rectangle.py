#!/usr/bin/env python3
""" Module BaseGeometry"""


BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Initialise un Rectangle avec width et height, privés et validés."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__height * self.__width