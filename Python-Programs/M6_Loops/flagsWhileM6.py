'''
Say you want your program to return "BIG NUMBER"
if the user plugs in a number greater than 2000
over the 5 iterations that they are asked.  You
can use "Flags" with a while loop.
'''

big_number_flag = False

for i in range(5):
    n = int(input("Enter a number: "))
    if (n > 2000):
        big_number_flag = True

if (big_number_flag):
    print("BIG NUMBER")


