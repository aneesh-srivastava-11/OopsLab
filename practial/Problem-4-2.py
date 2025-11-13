class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bow Bow")

class Snake(Animal):
    def sound(self):
        print("Hiss Hiss")

def polymorphism_prac():
    animals = [Animal(), Dog(), Snake()]
    for animal in animals:
        animal.sound()

polymorphism_prac()