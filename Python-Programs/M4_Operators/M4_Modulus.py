# Modular arithmetic
# Say you want to separate hours from minutes
timeMinutes = 476
oneHour = 60
minutes = timeMinutes % oneHour #this is the modulus % which only provides remainder
hours = timeMinutes // oneHour #floor division here rounds down
print(str(timeMinutes) + " min is " + str(hours) + " hours & " + str(minutes) + " min")

