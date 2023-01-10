# global
globalVar = 1

def myFunction():
    print("(inside function) globalVar = ", globalVar)
    global innerVar
    innerVar = 3
    print("(inside function) innerVar = ", innerVar)
    localVar = 2
    ReVar = 4
    print("(inside function) localVar = ", localVar)
    
    return (ReVar)
    

backVar=myFunction()

print("")
print("(outside function) globalVar = ", globalVar)
print("(outside function) localVar = ", backVar)
print("(outside function) innerVar = ", innerVar) #innerVar was made global
print("(outside function) localVar = ", localVar) #cannot access! As it is local to function
