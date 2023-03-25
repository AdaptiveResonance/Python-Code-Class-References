vowel = ("a", "e", "i", "o", "u")

test_word = "holiday"

for letter in test_word:
    if letter in vowel:#this is an iterator but not a loop
        print(letter, " is a vowel")
    else:
        print(letter, " is not a vowel")
