#A5 from CPRG-100
#Summer 2022
#takes textfile henryTheSquareEaredCat.txt and 
#creates henryThePentagonEaredCat.txt with appropriate text replaced
file = open("henryTheSquareEaredCat.txt", "r")
"""
this is quick and dirty alternative method, however
it can result in a large buffer with large input files
data=file.read()
data = data.replace("Square", "Pentagon")
data = data.replace("square", "pentagon")
file.close()
file2 = open("henryThePentagonEaredCat.txt", 'w')
#file2.write(data) # quick and dirty write
"""
data=[]#check slide 6 M9
for line in file:
    if "Square" in line or "square" in line:#check and replace square with pentagon
        newline = line.replace("Square", "Pentagon")
        newline = newline.replace("square", "pentagon")
        data.append(newline)
    else:
        data.append(line)
file.close()

file2 = open("henryThePentagonEaredCat.txt", 'w')#create/write new file
for newline in data:
    file2.write(newline)
file2.close()
print("file saved")

#confirmation to keep new file
ans=input("Would you like to keep new file henryThePentagonEaredCat.txt Y or N?")
if ans=='N' or ans=='NO' or ans=='0':
    import os
    if os.path.exists("henryThePentagonEaredCat.txt"):
        os.remove("henryThePentagonEaredCat.txt")

