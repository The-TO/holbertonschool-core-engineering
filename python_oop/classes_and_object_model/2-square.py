#!/usr/bin/env python3
"""Module 1-Square area"""


class Square:
    """Representation d'un Carre simple."""

    def __init__(self, size):
        """initialise la taille du Carre."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type(size) < 0:
            raise ValueError("size must be >= 0") 
        self.__size = size
