# Dictionaries

pizzaToppings = {1: "Cheese", 2: "Pepperoni", 3: "Pinapple", 4: "Ham"}

print(pizzaToppings)
print(pizzaToppings.keys)
print(pizzaToppings.keys())
print(pizzaToppings.items())
print(pizzaToppings.values())
print(pizzaToppings[3])
print("")
print(pizzaToppings)
print("")
topping = input("What topping would you like? ")
print("You selected: " + pizzaToppings[int(topping)])

