# from A2 CPRG-100 prints inout name and calculates temperature

name = input("What is your first name? ")
tempC = float(input("What is the current temperature in Celsius?"))
tempF = (tempC*1.8)+32 # Fahrenheit conversion
print("Temperature in Fahrenheit is:", tempF, 'degrees')

if tempC > 21:
    print(name, "it is warm outside")
elif tempC == 21:
    print(name, "it is perfect outside")
elif tempC < 21:
    print(name, "it is cool outside")
