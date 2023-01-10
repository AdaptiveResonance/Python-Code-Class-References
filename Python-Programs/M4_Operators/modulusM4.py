# Modular arithmetic
# Say you want to separate hours from minutes
timeMinutes = 456
oneHour = 60
minutes = timeMinutes % oneHour
hours = timeMinutes // oneHour
print(str(timeMinutes) + " min is " + str(hours) + " hrs & " + str(minutes) + " min")

