# Fibonacci Sequence

first = 1
second = 1
myList = [first, second]

number = input("How many Fibonacci numbers would you like to print? ")

index = 0
while (index < int(number)):
    print("F" + str(index + 1) + " = " + str(myList[index]))
    myList.append(myList[index] + myList[index + 1])
    #adding last to # together and append
    index = index + 1
