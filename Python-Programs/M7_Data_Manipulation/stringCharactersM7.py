print("1.) Backslash n to go to next line.")
print(r'\n')

print("2.) Does string have alphabetic characters only?")
string_a = "Hello"
print(string_a.isalpha())

print("3.) This time it has a space!")
string_b = "Hello there"
print(string_b.isalpha())

print("4.) Swaps lowercase with upercase and visa versa.")
print(string_b.swapcase())

print("5.) Takes frist two charactrs 0, and 1, of a string!")
print(string_b[0:2])

print("6.) Takes 5th character, remeber we start from zero!")
print(string_a[4])

print("7.) Takes characters 0, 1, and 2.")
print(string_a[:3])
