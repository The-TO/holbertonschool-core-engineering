#!/usr/bin/env python3
""" Module BaseGeometry"""

BaseGeometry = __import__('1-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """Initialise un Rectangle avec width et height, privés et validés."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        """Retourne une representation textuelle du Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
