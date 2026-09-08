#!/usr/bin/env python3
"""Module 2-Square size verif."""


class Square:
    """Representation d'un Carre simple."""

    def __init__(self, size=0):
        """Initialise la taille du Carre."""
        self.size = size

    @property
    def size(self):
        """Getter retourne la taille"""
        return self.__size

    def area(self):
        """Defini l'aire du Carre."""
        return self.__size * self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
