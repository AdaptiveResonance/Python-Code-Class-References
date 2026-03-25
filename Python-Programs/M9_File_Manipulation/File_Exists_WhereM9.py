import os


print(os.getcwd())  #current working directory of terminal.
print(os.path.dirname(os.path.abspath(__file__)))  #Current Script Directory

Terminal_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))  #Current Script Directory
file_path = os.path.join(script_dir, "Eggs.txt")


if os.path.exists("Eggs.txt"):      #check the current terminal working directory for the text file
    print("Egg text exists locally to terminal!")
elif os.path.exists(file_path):     #check the Current Script file Directory for the text file
    print("Egg text exists locally to file!")
else:
    print("Egg text has not been created yet!")
    print(os.getcwd())  #current working directory of terminal.


