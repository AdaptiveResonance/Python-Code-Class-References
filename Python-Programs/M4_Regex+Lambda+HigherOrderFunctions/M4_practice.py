import math
from functools import reduce
import re

lst = range(1,101)

# a % 2 == 0 and a % 3 == 0 and a % 7 == 0 can be written as not (a % 2 or a % 3 or a % 7)
# using demorgan's theorem.
new_lst = list(map(lambda a: math.pow(a,3), filter(lambda a: not (a % 2 or a % 3 or a % 7), lst)))
print(new_lst)

lst_comprehension = [math.pow(i, 3) for i in lst if not (i % 2 or i % 3 or i % 7)]
print(lst_comprehension)

lst_comprehension.sort(key = lambda num : num % 10)
print(lst_comprehension)

print (reduce(lambda a, b: a * b, lst_comprehension)/reduce(lambda a, b: a + b, lst_comprehension))

txt = "A quick brown fox"
text2 = "123 dog"
print(re.search('^[a-zA-Z ]+$', txt))
print(re.search('^[a-zA-Z ]+$', text2))