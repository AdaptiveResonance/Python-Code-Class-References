# -*- coding: utf-8 -*-
import functools

lst_numbers = range(1, 11)
print(list(lst_numbers))

# sorted in reverse
print(sorted(lst_numbers,reverse=True))

# sorted with keys
str_lst = ['John','Kim','Daniel','Sheldon']
# lets sort the above list in order of the length of each word
#increasing
print(sorted(str_lst,key= lambda a: len(a)))

#decreasing
print("List after sorted", sorted(str_lst,
                key= lambda a: len(a), reverse = True))

# sort function
print("Original List", str_lst)
str_lst.sort(key=lambda a: len(a), reverse = True)
print("List after sort", str_lst)


# Reduce with lambda
prod = functools.reduce(lambda acc,ele: acc*ele, lst_numbers)
#print(prod)

# Reduce without lambda
def mult(acc,ele):
    return acc*ele
prod = functools.reduce(mult, lst_numbers)
#print(prod)


# filter with lambda
even_numbers = filter(lambda a: a%2 == 0, lst_numbers)
#print(list(even_numbers))

# filter with a function
def even_num(a):
    return a%2 == 0
even_ = filter(even_num, lst_numbers)
#print(list(even_))


# Map with Lambda
doubled_numbers = map(lambda a: a*2,lst_numbers)
#print(list(doubled_numbers))

# Map with a function
def double_num(a):
    return a * 2
doubled = map(double_num, lst_numbers)
#print(list(doubled))
