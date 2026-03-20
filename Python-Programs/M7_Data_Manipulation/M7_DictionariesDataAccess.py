# Dictionaries

pizzaToppings = {1: "Cheese", 2: "Pepperoni", 3: "Pineapple", 4: "Ham"}

print(pizzaToppings)
print(pizzaToppings.keys)
print(pizzaToppings.keys())#Key ring
print(pizzaToppings.items())#like printing entire dictionary
print(pizzaToppings.values())# values
print(pizzaToppings[3])
print("")
print(pizzaToppings)
print("")
Topping = input("What topping would you like? ")
print("You selected: " + pizzaToppings[int(Topping)])

