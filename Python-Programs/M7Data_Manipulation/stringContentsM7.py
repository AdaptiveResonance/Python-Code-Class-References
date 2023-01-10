arduinoOutput = "1 25 20"
parsed = arduinoOutput.split()
print(parsed)
print("")
print("Arduino output: ")
if (parsed[0] == "1"):
    print("Power ON")
else:
    print("Power OFF")
print("Temperature is: "+ parsed[1] +" degrees Celsius")
print("Oxygen percentage is: "+ parsed[2] + "%")


