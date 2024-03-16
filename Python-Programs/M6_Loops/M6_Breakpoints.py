vowel = ("a", "e", "i", "o", "u")

iteration = 1

test_word = "holiday"

pause = input("This a breakpoint, enter to continue: ")
for letter in test_word:

    print(" We are processing " + letter + " now.")
    print(" We are in iteration number " + str(iteration) + ".")
    iteration = iteration + 1

    pause = input("This a breakpoint, enter to continue: ")
    
    if letter in vowel:
        print(letter, " is a vowel")
    else:
        print(letter, " is not a vowel")


