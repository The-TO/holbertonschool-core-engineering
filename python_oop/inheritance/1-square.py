#!/usr/bin/env python3
""" Module Square"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Initialise un Carré avec size"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
