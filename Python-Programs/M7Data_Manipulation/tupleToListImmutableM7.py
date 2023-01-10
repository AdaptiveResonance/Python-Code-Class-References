# List  : Ordered, Can have duplicates, Mutable
# Tuple : Ordered, Can have duplicates, Immutable

myList = ['Esmeralda', 4, 3.14159, False]
myTuple = tuple(myList)

# Mutable vs. Immutable, (Refer to their ids)

# Mutable lists may change their elements
print(type(myList))
myList[1] = 32
print(myList)

# Immutable Tuples may NOT change their elements
print(type(myTuple))
myTuple[1] = 64 #will crash here as Tuple is immutable
print(myTuple)



