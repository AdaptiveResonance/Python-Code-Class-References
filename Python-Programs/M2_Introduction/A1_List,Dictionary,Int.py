# WIP clarify when dictionary ordered or not
# #Based upon CPRG-104 prints name
# Dictionary{}: are ordered as of Py3.7
name = (input("What is your first name? "))

year = [2026, 2000]#replace with current year and birth year
year[1] = int(input("What is your birth Year"))#replace first year
print("Hello {0} aged {1}, Welcome to Python Class!".format(name,str(year[0]-year[1])))
print("Both lists and dictionaries have changeable data values")
print("Dictionary values are not ordered before 3.7 but stored/indexed in Key:Value pairs")
print("while lists are ordered and indexed by their integer indice")
# Both lists and dictionaries have changeable data values
# Dictionary values are not ordered but stored/indexed in Key:Value pairs
# While lists are ordered and indexed by their integer indice

