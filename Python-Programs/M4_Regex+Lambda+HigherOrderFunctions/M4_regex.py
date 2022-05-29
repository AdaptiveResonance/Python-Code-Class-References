# -*- coding: utf-8 -*-
import re

# Find first occurance of ab in the string abcdefabef
matc_search = re.search("ab", "abcdefabef")
print(matc_search.span())
print(matc_search.group())

# Find all occurance of ab in the string abcdefabef
matc_findall = re.findall("ab", "abcdefabef")
print(matc_findall)

# replace all occurance of ab in the string abcdefabef with AB
print(re.sub("ab","AB","abcdefabef"))

# split the string with ab
print(re.split("ab", "cabcdefabef"))

