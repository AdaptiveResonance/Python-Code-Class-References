myList = [1,3,67,23,3,13,7,7,1,-53,-9,0,2345,0,1]
sorted_myList= sorted(myList)
print(sorted_myList)

'''
When you make a change to a list that has been set
to a variable, the variable will inherit the change
you made to the original list
'''
listA = ["meat", "potatoes", "vegetables"]
listB = listA
print("Old B",listB)
listA[2] = "cake"
print("New A",listA)
print("New B",listB)
#basically a pointer to listA

# But this is not true for copy
listA = ["meat", "potatoes", "vegetables"]
listB = listA.copy()
print("New B",listB)
listA[2] = "cake"
print("Final B",listB)

