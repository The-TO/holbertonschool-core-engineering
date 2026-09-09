#!/usr/bin/env python3

"""Module 2-square
Creation of Square class from the Rectangle module
"""


Rectangle = __import__('2-rectangle').Rectangle
class Square(Rectangle):
    """Initialise un Carré avec size"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        """Retourne une representation textuelle du Carré"""
        return f"[Square] {self.__size}/{self.__size}"