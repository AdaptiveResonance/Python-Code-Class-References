myDiction = {"bacon" : 4, "lettuce": 1, "tomatoes" : 2}
print(myDiction)
# print lettuce value using key "lettuce"
print(myDiction["lettuce"])
#print(myDiction["1"]) inverse will not work
print(type(myDiction))
myDiction["sausage"] = 3
myDiction["lettuce"] = 5
myDiction['pepperoni'] = myDiction.pop('bacon')
print(myDiction)

# {'bacon': 4, 'lettuce': 1, 'tomatoes': 2}
# 1
# <class 'dict'>
# {'bacon': 4, 'lettuce': 1, 'tomatoes': 2, 'sausage': 3}

