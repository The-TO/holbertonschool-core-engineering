#!/usr/bin/env python3
"""Module definisssanrt des mixin"""

class SwimMixin:
    """Classe afin de definir la nage a dragon"""
    def swim(self):
        print ("The creature swims!")

class FlyMixin:
    """Classe afin de definir le vol a dragon"""
    def fly(self):
        print ("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print ("The dragon roars!")


dragon = Dragon()

dragon.swim()
dragon.fly()
dragon.roar()
