# -*- coding: utf-8 -*-
#Method Resolution Order
class A:
    def do_something(self):
        print("Executing in A")

    def SomethingElse(self):#without self it will execute but invisbly without a local references
        print("Lower Precedence Found at A!")

class B:
    def do_something(self):
        print("Executing in B")
    #def SomethingElse(self):
        #print("Lower Precedence Found at B!")

class C(B,A):
    pass

c = C()
c.do_something()
for i in C.__mro__: #Method Resolution Order
    print("location: ",i)
c.SomethingElse
