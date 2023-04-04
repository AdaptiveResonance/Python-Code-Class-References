# Function return values

def average(*args):
    total = 0
    count = 0
    for num in args:
        total = total + num
        count = count + 1
    return total/int(count)

print("Class Average: ")
print(average(54,67,89,45,90,75,65,65,73,72,95,56))
value=average(54,67,89,45,90,75,65,65,73,72,95,56)
