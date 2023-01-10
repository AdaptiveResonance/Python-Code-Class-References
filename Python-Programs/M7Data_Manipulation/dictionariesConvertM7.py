# Dictionaries

myString = "Oct-pumpkin, Nov-snow, Dec-santa"
print("myString: " + myString)

myListOfStrings = myString.split(", ")
print("myListOfStrings: " + str(myListOfStrings))

myList = []
for i in range(0, len(myListOfStrings)):
    myList.append(myListOfStrings[i].split("-"))
print("myList: " + str(myList))

myDictionary = dict(myList)
print("myDictionary: " + str(myDictionary))

