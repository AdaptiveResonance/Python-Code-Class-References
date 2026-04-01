# -*- coding: utf-8 -*-
class animal:
    def __init__(self, name):
        self.__name = name
    
    def walk(self):
        print("Animal is walking")
    
    def run(self):
        print("Animal is running")

    def Retrieve_name(self):
        return self.__name 
    #proper way to get parent attribute is to return it to child class

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name)
        self.breed = breed #local Attribute
    
    def bark(self):
        print("Dog is barking")
        
    def getName(self):
        #print(self.name) Will not work since it is not local
        #print(self.__name) Cannot access directly since it is private attribute in parent class

        print(f"Hidden name: {self._animal__name}") 
        #roundabout method negates point of private attribute in Parent Class

    def WhatBreed(self):
        print(self.breed)   
    
    
tom = dog("Tom","Labrador")
tom.getName()
tom.WhatBreed()
print(tom.Retrieve_name())

