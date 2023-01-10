# -*- coding: utf-8 -*-
#helpful link: https://funtech.co.uk/latest/explain-object-oriented-programming-to-kids
"""Dog class will inherit from Animal class to provide Tom the Dog actions"""
class animal:
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        print("Animal is walking")
    
    def run(self):
        print("Animal is running")
        

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name)
        self.breed = breed
    
    def bark(self):
        print("Dog is barking")
        
tom = dog("Tom","Labrador")
tom.walk()
tom.run()
tom.bark()

print(isinstance(tom, dog)) #True
print(isinstance(tom, animal)) #True
print(issubclass(dog, animal)) #True