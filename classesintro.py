class MyClass:
    pass

species = "Canis familiaris"

class Dog:
    species = "Canis familiaris"

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} barks!"

dog1 = Dog("Buddy", 5)
print(dog1.bark())

dog2 = Dog("Max", 2)
print(dog2.bark())

dog3 = Dog("Moo", 10)
print(dog3.bark())

class GermanShepherd(Dog):
    def guard(self):
        return f"{self.name} is guarding!"
    
gs_dog = GermanShepherd("Rex", 3)
print(gs_dog.guard())

print(species)