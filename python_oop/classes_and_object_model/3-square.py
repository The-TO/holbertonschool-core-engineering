#!/usr/bin/env python3
"""Module 3-Square size verif."""


class Square:
    """Representation d'un Carre simple."""

    def __init__(self, size=0):
        """Initialise la taille du Carre."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Defini l'aire du Carre."""
        return self.__size * self.__size
