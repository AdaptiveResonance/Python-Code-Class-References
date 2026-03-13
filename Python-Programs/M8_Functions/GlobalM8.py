# global
#to do cleanup terms
globalVar = 1   #implicit global value

def myFunction():
    print("(inside function) globalVar = ", globalVar)
    global innerVar #explicit global value
    innerVar = 3
    print("(inside function) innerVar = ", innerVar)
    localVar = 2
    ReVar = 4
    print("(inside function) localVar = ", localVar)
    
    return (ReVar)
    
globalVar = 2
backVar=myFunction()

print("")
print("(outside function) globalVar = ", globalVar)
print("(outside function) localVar = ", backVar) # was returned
print("(outside function) innerVar = ", innerVar) #innerVar was made global
print("(outside function) localVar = ", localVar) #cannot access! As it is local to function
