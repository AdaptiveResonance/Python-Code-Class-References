# Suppose we want to do the following
'''
Remove all the cats
Then confirm that they are gone!
'''
myList = ["cat", "yarn", "dog", "cat", "bottle", "cat", "cat", "fork"]

myList.remove("cat")#removes first one
determine = "cat" in myList

if (not determine):#double negative
    print("No cats in myList")
else:#not True is false
    print("At least one cat remains in myList")

# We can also remove elements using del
# del allows us to remove an element by index

print(myList)
index = input("Index of element to be removed: ")
print("Delete: "+ str(myList[int(index)]))
del myList[int(index)]
print(myList)


