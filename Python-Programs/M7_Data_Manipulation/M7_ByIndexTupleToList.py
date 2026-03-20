# You may grab list elements by index

myList = ['Esmeralda', 4, 3.14159, False]

print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[-1])

myTuple = ("Golden ratio", 1.61803)
print(type(myTuple))# immutable
myNewList = list(myTuple)# now mutable
print(type(myNewList))
myNewList[0]='New Ratio'
print(myNewList[0])



