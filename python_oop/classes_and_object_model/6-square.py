#!/usr/bin/env python3
"""Module 5-Square size verif."""


class Square:
    """Representation d'un Carre simple."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise la taille du Carre."""
        self.size = size
        self.position = position

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

    def my_print(self):
        print(self)

    def __str__(self):
        """Retourne la representation textuelle du carré."""
        if self.size == 0:
            return ""
        else:
            lines = []
            for i in range(self.position[1]):
                lines.append("")
            for i in range(self.size):
                lines.append(" " * self.position[0] + "#" * self.size)
            return "\n".join(lines)

    @property
    def position(self):
        """getter retourne la position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
