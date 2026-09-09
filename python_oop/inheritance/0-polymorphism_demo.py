#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

print(isinstance(dog, Cat))
print(isinstance(dog, Animal))
print(issubclass(Cat, Animal))