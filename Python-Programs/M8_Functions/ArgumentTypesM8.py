# function example with argument

def student(firstName,lastName,idNumber):
    return idNumber + " - " + firstName + " " + lastName


def classroom(classId,computers = True,classSize = 5):
    if (classSize < 5):
        return "Cannot justify offering this course."
    else:
        if (computers):
            return "Course will be offered with computers!"
        else:
            return "Course will be offered."

print(student("Justin", "Pilon", "000554433"))
print(classroom(123456789, classSize = 25))
print(classroom(123456789, classSize = 1))
print(classroom(123456789))
print(classroom(123456789, computers = False, classSize = 6))
