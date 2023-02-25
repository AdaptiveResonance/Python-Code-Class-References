vowel = ("a", "e", "i", "o", "u")

test_word = "holiday"

for letter in test_word:
    if letter in vowel:
        print(letter, " is a vowel")
    else:
        print(letter, " is not a vowel")
