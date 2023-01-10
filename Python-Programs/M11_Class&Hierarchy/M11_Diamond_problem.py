# -*- coding: utf-8 -*-
class A:
    def do_something(self):
        print("Executing in A")

class B():
    def do_something(self):
        print("Executing in B")

class C(A,B):
    pass

c = C()
c.do_something()
for i in C.__mro__:
    print(i)
