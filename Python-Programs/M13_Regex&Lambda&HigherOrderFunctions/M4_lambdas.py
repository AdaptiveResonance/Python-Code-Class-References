# -*- coding: utf-8 -*-
# Example of a lambda that adds 5 to the input
x = lambda a: a+5
print(x(5))	#prints 10

# Implementation of above lambda as a function
def add5(a):
	a = a + 5
	return a
print(add5(5))	#prints 10

# Nesting two lambdas
x = lambda n: lambda a: a*n
print(x(2)(10)) # prints 20 here n = 2 and a = 10

# Nesting lambda in a function
def myfunc(n):
	return lambda a : a * n

doubler = myfunc(2) # n = 2
print(doubler(11)) # prints 22 as a = 11

tripler = myfunc(3) # n = 3
print(tripler(11)) # prints 33 here a = 11

print(myfunc(2)(10)) # prints 20 here n = 2 and a = 10

# Function Object
opr = lambda a, x : x(a)
print(opr(6,lambda a: a**2 ))
print(opr(6, lambda a: a+2))