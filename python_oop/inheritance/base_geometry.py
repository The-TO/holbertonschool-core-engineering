#!/usr/bin/env python3
""" Module BaseGeometry"""

class BaseGeometry:
    """Representation d'un base Geometrie"""
    def area(self):
        """Definition de l'aire de la forme"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
            """Validation des parametres"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")
