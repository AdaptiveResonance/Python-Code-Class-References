# -*- coding: utf-8 -*-
class A:
    def display(self):
        print("I'm in A")
    
    def show(self):
        print("Show A")
    
class B(A):
    def display(self):
        print("I'm in B")
    
    def show(self):
        A.show(self) #Name reference directly
        super().show() #Positional reference by Hierarchy
        print("Show B")
    
b = B()
b.display()
b.show()
