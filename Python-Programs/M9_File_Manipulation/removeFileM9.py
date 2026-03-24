# Remove a file

import os
script_dir = os.path.dirname(os.path.abspath(__file__))  #Current Script Directory
file_path = os.path.join(script_dir, "Eggs.txt")


file=open(file_path, mode = 'r')
content = file.read()
print("fileContents: ", content)
file.close()

os.remove(file_path)
print("Eggs.txt was deleted!")

newLines2Append = ['eggs\n', 'bacon\n','eggs\n', 'bacon\n', 'bacon\n', 'bacon\n', 'bacon\n','eggs\n','eggs\n']


with open(file_path, mode = 'w') as newFile:
    for newLine in newLines2Append:

        newFile.write(newLine)
newFile.close()