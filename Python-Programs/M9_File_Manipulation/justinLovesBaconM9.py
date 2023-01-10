# Create a new file called "justinLovesEggs.txt"

file = open("JustinLovesBacon.txt", mode = 'r')

newLines = []
for line in file:
    if "bacon" in line:
        newLine = line.replace("bacon", "eggs")
        newLines.append(newLine)
    else:
        newLines.append(line)
file.close()

print(newLines)

with open("justinLovesEggs.txt", mode = 'w') as newFile:
    for newLine in newLines:
        newFile.write(newLine)

newFile.close()






