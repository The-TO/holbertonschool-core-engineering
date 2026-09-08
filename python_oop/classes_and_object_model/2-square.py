#!/usr/bin/env python3
"""Module 1-Square area"""


class Square:
    """Representation d'un Carre simple."""

    def __init__(self, size):
        """initialise la taille du Carre."""
        if type(size) is not int:
            raise TypeError("la taille dois etre un entier")
        if type(size) < 0:
            raise ValueError("la taille dois etre superieur ou egal à 0") 
        self.__size = size
