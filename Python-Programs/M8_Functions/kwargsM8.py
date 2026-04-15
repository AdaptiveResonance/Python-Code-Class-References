# **kwargs
#Key word Arguements

def setupDict(**kwargs):
    print(kwargs)
    print(*kwargs) #Clean ouput but on keys
    #result = ""
    result = kwargs
    return result

catNames = setupDict(cat1 = "Esmeralda",
                     cat2 = "Huckleberry",
                     cat3 = "Dorian",
                     cat4 = "Winifred")
print(catNames)
