myTuple = (1, 2, 3)
print(myTuple)
print(myTuple[0])
print(type(myTuple))
myTuple[1] = 5 #tuples are immutable so will crash here

# (1, 2, 3)
# 1
# <class 'tuple'>
#   myTuple[1] = 5
# TypeError: 'tuple' object does not support item assignment

