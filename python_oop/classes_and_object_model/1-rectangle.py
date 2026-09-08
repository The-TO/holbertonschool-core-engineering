#!/usr/bin/env python3
"""Module 5-Square size verif."""


class Rectangle:
    """Representation d'un Rectangle simple."""

    def __init__(self, width=0, height=0):
        """Initialise la taille du Carre."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter retourne la taille."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value


    @property
    def height(self):
        """Getter retourne la height"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            raise TypeError ("height must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__width = value

    def area(self):
            """Defini l'aire du Rectangle."""
            return self.__width * self.__height

    def my_print(self):
        print(self)

    def __str__(self):
        """Retourne la representation textuelle du Rectangle."""
        if self.width == 0:
            return ""
        else:
            lines =[]
            for i in range(self.height):
                lines.append("")
            for i in range(self.width):
                lines.append("#" * self.height + "#" * self.width)
            return "\n".join(lines)
