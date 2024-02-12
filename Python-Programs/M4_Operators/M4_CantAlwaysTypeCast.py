# Can't always type cast
x = "5"
y = "g"
z = float(x)
print(z)
w = int(y)#will crash
w = float(y)#will crash

# Imagine trying to turn "g" into a number or even currency!  
# The computer says NOPE!
# However there are some alternatives mostly with other imported libraries:
'''
    String to Decimal using float()
    String to Decimal using numpy.float_()
    String to Decimal using decimal.Decimal()
'''


