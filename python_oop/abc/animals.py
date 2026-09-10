#!/usr/bin/env python3
"""Moduel definissant les classes abstraites Animal"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """Classe abstraite qui defini un animal"""
    @abstractmethod
    def sound(self):
        """Defini le son de l'animal"""
        pass
    def __str__(self):
        """retourne la reppresentation textuelle du son de l'animal"""
        return "[Animal] Le {} dit {}".format(type(self).__name__, self.sound())

class Dog(Animal):
    """Le chien"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Le Chat"""
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog)
print(cat)