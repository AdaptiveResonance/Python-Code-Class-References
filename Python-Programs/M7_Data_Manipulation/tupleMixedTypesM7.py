myTuple = ('Huckleberry', 3, 2.71828, True)
print(myTuple)

index = 0
while (index < len(myTuple)):
    print(type(myTuple[index]))
    index = index + 1

# You can assign names to tuples variables
name, age, whiskerLength, furry = myTuple
print(name, age, whiskerLength, furry)

# And you don't always have to assign them all
naturalLogBase, DoILoveMath = myTuple[2], myTuple[3]
print(naturalLogBase, DoILoveMath)




