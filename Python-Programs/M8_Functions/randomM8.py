# random

import random

x = random.random()
y = random.randint(1,100)
z = random.randrange(1,100,2)
u = random.choice([10,12,15,18])

vList = ["cat","dog","lion","wolf"]
v = random.shuffle(vList)

# sample gives you multiple random samples
w = random.sample(vList,2)

print(x)
print(y)
print(z)
print(u)
print(vList)
print(w)


