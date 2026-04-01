# -*- coding: utf-8 -*-
class animal:
    def __init__(self, name):
        self.__name = name
    
    def walk(self):
        print("Animal is walking")
    
    def run(self):
        print("Animal is running")
    

class dog(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name)
        self.breed = breed #local Attribute
    
    def bark(self):
        print("Dog is barking")
        
    def getName(self):
        print(self.name)
        print(self.__name)

    #def WhatBreed(self):
        #print(self.breed)   
    
    
tom = dog("Tom","Labrador")
tom.getName()
tom.WhatBreed()


