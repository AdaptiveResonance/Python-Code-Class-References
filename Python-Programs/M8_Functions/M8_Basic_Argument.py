# function example with argument

def student(firstName, lastName, idNumber):
    print("First Name: "+ str(firstName))
    print("Last Name: "+str(lastName))
    print("Id Number: "+str(idNumber))
    return(firstName+lastName+" "+idNumber)

x = input("What is your first name? ")
y = input("What is your last name? ")
z = input("What is your Id number? ")

returned=student(x,y,z)
print(returned)


