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
        A.show(self)
        super().show()
        print("Show B")
    
b = B()
b.display()
b.show()
