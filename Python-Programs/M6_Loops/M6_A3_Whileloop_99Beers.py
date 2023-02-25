#Based upon A3 CPRG-100
#Loop printing of '99 BOTTLES OF BEER ON THE WALL'
String1="bottles of beer on the wall,"
String1A="bottle of beer on the wall,"
String2="bottles of beer!"
String2A="bottle of beer!"
String3="Take one down,"
String3A="Take it down,"
String4="Pass it around,"
String5="bottles of beer on the wall!"
String5A="bottle of beer on the wall!"
String5B="No more bottles of beer on the wall!"

i=99
while i > 0:
    if i == 1:#one bear
        print(i,String1A)
        print(i,String2A)
        print(String3A)
        print(String4)
        print(String5B)
    else:#every bear
        print(i,String1)
        print(i,String2)
        print(String3)
        print(String4)
        if i == 2:#second last bear
            print(i-1,String5A)
        else:
            print(i-1,String5)
    print("")
    i=i-1
  
