# Create a new file called "Eggs.txt"

import os

script_dir = os.path.dirname(os.path.abspath(__file__))  #Current Script Directory
file_path = os.path.join(script_dir, "Eggs.txt")
file = open(file_path, mode = 'r')


content = file.read()
print("fileContents: ", content)
file.seek(0) # reset cursor to 0 or file start

newLines2Append = []
for line in file:
    if "bacon" in line:
        newLine = line.replace("bacon", "eggs")
        newLines2Append.append(newLine)
        print("Lines 2 append: ", newLines2Append)
    else:
        newLines2Append.append(line)
file.close()


with open(file_path, mode = 'w') as newFile:
    for newLine in newLines2Append:

        newFile.write(newLine)
newFile.close()

