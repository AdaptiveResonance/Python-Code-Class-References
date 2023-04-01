string_a = "   Oh, wow!  Starts and ends with 3 spaces!   "
string_b = (string_a.strip())

print(string_a)
print(string_b)

print(len(string_a))
print(len(string_b))

print(string_a.find("Oh"))
print(string_b.find("Oh"))

print(string_a.endswith("spaces!"))
print(string_b.endswith("spaces!"))


