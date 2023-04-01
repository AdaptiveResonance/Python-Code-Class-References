myList = [1,3,67,23,3,13,7,7,1,-53,-9,0,2345,0,1]
sort_myList= sorted(myList)
print(sort_myList)

'''
When you make a change to a list that has been set
to a variable, the variable will inherit the change
you made to the origional list
'''
listA = ["meat", "potatoes", "vegetables"]
listB = listA
print(listB)
listA[2] = "cake"
print(listB)

# But this is not true for copy
listA = ["meat", "potatoes", "vegetables"]
listB = listA.copy()
print(listB)
listA[2] = "cake"
print(listB)

