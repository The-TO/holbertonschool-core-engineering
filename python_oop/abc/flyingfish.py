#!/usr/bin/env python3
"""Module definisssanrt des heritages multiples"""

class Fish:
    """Classe definissant un poisson"""

    def swim(self):
        print ("The fish is swimming")

    def habitat(self):
        print ("The fish lives in water")

class Bird:
    """Classe definissant un oiseau"""
    def fly(self):
        print ("The bird is flying")
    def habitat(self):
            print ("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Classe du poisson volant"""
    def fly(self):
         print("The flying fish is soaring!")
    def swim(self):
         print("The flying fish is swimming!")
    def habitat(self):
         print ("The flying fish lives both in water and the sky!")

flyingfish = FlyingFish()

flyingfish.fly()
flyingfish.swim() 
flyingfish.habitat()

FlyingFish.__mro__
     