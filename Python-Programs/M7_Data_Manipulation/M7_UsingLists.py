# Suppose we want to do the following
'''
For every dog in the list add 2 more cats
Give us the total number of cats at the end
'''
myList = ["cat", "yarn", "dog", "cat", "bottle", "cat", "cat", "fork"]

for i in range(0, len(myList) + 1):
    if (myList[i] == "dog"):
        myList.extend(["cat", "cat"])

myBinaryList = []
j = 0
while (j < len(myList)):
    if (myList[j] == "cat"):
        myBinaryList.append(1)
    else:
        myBinaryList.append(0)
    j = j + 1

print("myList = "+ str(myList))
print("myBinaryList = "+ str(myBinaryList))
print("Adding 2 cats for every dog, yields "+ str(sum(myBinaryList)) +" cats!")
