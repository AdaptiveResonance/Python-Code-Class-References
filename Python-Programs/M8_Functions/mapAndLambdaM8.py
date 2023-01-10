# lambda function example

cube = lambda x : x **3
print("2^3 = " + str(cube(2)))

# map function example

def toUpper(s):
    return s.upper()

p = ["bc","ab","sk","mb","on","qc","nf","pei","nb","ns","nw","yk"]
P = map(toUpper, p)

print(list(P))


