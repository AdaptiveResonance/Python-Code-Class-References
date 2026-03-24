# Read
import os
script_dir = os.path.dirname(os.path.abspath(__file__))  #Current Script Directory
file_path = os.path.join(script_dir, "Eggs.txt")


file = open(file_path, mode = 'r')

for line in file:
    print(line, end="")


file.seek(0) # reset cursor to 0 or file start
content = file.read()
print("fileContents: ", content)