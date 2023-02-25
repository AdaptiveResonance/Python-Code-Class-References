# Let me in elif I will blow your house down!
# Interactive 3 little pigs

print("Build your house out of: ")
print(" 1 straw")
print(" 2 sticks")
print(" 3 bricks")
print(" 4 Flowers")
houseType = input("> ")
if (houseType == '1'):
    print("Wolf blows your house down with ease!")
elif (houseType == '2'):
    print("Wolf blows your house down with difficulty.")
elif (houseType == '3'):
    print("Wolf can't blow down your house. Good Decision!")
elif (houseType == '4'):
    print("Wolf sneezed and can't blow down your house. Clever Decision!")
else:
    print("Invalid input.")

