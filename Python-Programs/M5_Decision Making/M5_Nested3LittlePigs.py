# Let me in elif I will blow your house down!
# Interactive 3 little pigs

print("Build your house out of: ")
print(" 1 straw")
print(" 2 sticks")
print(" 3 bricks")
houseType = input("> ")
if (houseType == '1'):
    print("Wolf blows your house down with ease!")
elif (houseType == '2'):
    print("Wolf blows your house down with difficulty.")
elif (houseType == '3'):
    print("Wolf can't blow down your house.  Well done!")
    print("")
    print("Let the wolf in your house? (y/n)")
    naivety = input("> ")
    if (naivety == 'y'):
        print("The wolf enters your house! For tea.")
    elif (naivety == 'n'):
        print("The wolf remains outside.")
    else:
        print("The Wolf continues to wait.")
else:
    print("Invalid input.")


    


