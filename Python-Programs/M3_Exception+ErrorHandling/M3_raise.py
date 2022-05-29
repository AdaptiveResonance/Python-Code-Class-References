# -*- coding: utf-8 -*-
import numbers

def exception_method(a):
    result = None
    if not isinstance(a, numbers.Number):
        raise TypeError("the argument has to be a number")
    try:
        result = 10/a
    except ZeroDivisionError:
        print("cannot divide by 0")
        result = 0
    except:
        print("Some other error occured")
    finally:
        print("Operation Completes")
    return result
        
print(exception_method(10))
print(exception_method(""))
