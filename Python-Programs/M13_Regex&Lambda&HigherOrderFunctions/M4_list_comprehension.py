# -*- coding: utf-8 -*-
import numpy as np

lst = list(range(1,11))

""" Get a new list with only odd numbers and 
each of them multiplied by 5"""

new_lst = [i * 5 for i in lst if i % 2 != 0]
#print(new_lst)

""" For loop implementation"""
new_lst = []
for i in lst:
    if i % 2 != 0:
        new_lst.append(i*5)
#print(new_lst)

"""Using lambda as part of expression"""
x = lambda a : a * 5
new_lst = [x(i) for i in lst if i % 2 != 0]
#print(new_lst)


""" Using map and filter"""
new_lst = list(map(lambda a : a * 5, 
                    filter(lambda b: b%2 != 0, lst)))
#print(new_lst)



# multiplication table using for loop
table = []
for i in range(1,6):
    lst = []
    for j in range(1,6):
        lst.append(i*j)
    table.append(lst)
print(np.matrix(table))

print()

table = [[i*j for j in range(1,6) ] for i in 
         range(1,6)]
print(np.matrix(table))
