#Based upon A4 CPRG-100
#Basic pizza toppings and bill calculator
#Hey computer make me a pizza
print("Welcome to Python Pizza!!")
name = input("What is your last name for the order? ")
toppings=("Cheese", "Pineapple", "Pepperoni", "Ham", "Everything", "Done")
count = choice = 0 #assigning mutable objects such like list/dict instead of immutable objects; int, float, or str, will assign same object to all variables!!
urpizza=[]#plain pizza to build on
while choice !=6:
    print("Pick the number associated with your desired topping, then press done")
    print(f"1. Cheese \n2. Pineapple, \n3. Pepperoni, \n4. Ham, \n5. Everything, \n6. Done")
    choice = input("")
    if int(choice) > 6 or int(choice) <1:
        print("Invalid selection")
    elif choice == '6' :#select done to exit
        if count==0:#go back if no toppings selected and notify user
            print("No toppings selected, please select at least 1 topping.")
        else:#Leave topping selector
            break
    elif choice == '5':#select everything to override toppings with ALL toppings
        count=4
        print(toppings[int(choice)-1], "added")
        urpizza=[]#clear out prior topping duplicates
        urpizza.append(toppings[0])
        urpizza.append(toppings[1])
        urpizza.append(toppings[2])
        urpizza.append(toppings[3])
        break
    else:# Normal case for adding topping
        count=count+1
        urpizza.append(toppings[int(choice)-1])
        print(toppings[int(choice)-1], "added")
if count==1:
    cost=8
elif count==2:
    cost=10
elif count==3:
    cost=12
else:#includes 4+ or everything toppings
    cost=14
print("Pizza with {}".format((str(urpizza))[1:-1]), "at {}{:.2f}".format('$', float(cost)), "for", name)
#[1:-1] helps to omit the first char '[ and ]' from the list when printing whole list, for a clean output
#check https://blog.finxter.com/how-to-print-a-list-without-brackets-in-python/