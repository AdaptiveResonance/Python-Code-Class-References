# lambda function example

cubed = lambda x : x **3 #power of 3 to cube
print("2^3 = " + str(cubed(2)))

# map function example

def toUpper(s):
    return s.upper()

p = ["bc","ab","sk","mb","on","qc","nf","pei","nb","ns","nw","yk"]
P = map(toUpper, p)

print(list(P))


