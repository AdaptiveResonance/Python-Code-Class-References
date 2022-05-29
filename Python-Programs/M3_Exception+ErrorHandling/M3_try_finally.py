# -*- coding: utf-8 -*-
def exception_method(a):
    result = None
    try:
        result = 10/a
    finally:
        print("Operation Completes")
    return result
        
print(exception_method(0))
print(exception_method(10))

