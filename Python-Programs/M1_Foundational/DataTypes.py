#List[]: Ordered[1] and changeable
print("List:")
mylist = ["Dogs", "Cats", "Birds", 3, True]
print(mylist)
print(mylist[2])
print(len(mylist))#print # of items in list

# Set{}: unordered, unindexed, No-duplicates(will not output double), 
# unchangable but removeable/replacable
print("Set:")
myset = {"apple", False, 48, "cherry"}
print(myset)
print(len(myset))#will print 3 not 4!

# Tuple(): Ordered[2] collection,  and unchangeable!
# does not support item deletion but can delete tuple: del mytuple
print("Tuple:")
mytuple = ("Goat","Cow","Llama", True, 35)
Singletuple= ("tuple",)#',' is required for single tuple
print(mytuple)
print(mytuple[1])
print(len(mytuple))#prints #5 for tuple item count
print(mytuple.count('Cow'))  # Output: 2
print(mytuple.index('Llama'))  # Output: 2

# Dictionary{}: are unordered[3] as of Py3.7
# store changeable data values in key:value pairs
#No duplicates pairs they will overwrite existing/previous values pair!
print("Dictionary:")
thisdict = {
  "brand": "Lenovo",
  "model": "Thinkpad",
  "year": 2018
} 
print(thisdict)
print(thisdict["brand"])#prints brand
print(len(thisdict))#3 for # or value pairs