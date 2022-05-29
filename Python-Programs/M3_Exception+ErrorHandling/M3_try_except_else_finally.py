# -*- coding: utf-8 -*-
def exception_method(a):
    result = None
    try:
        result = 10/a
    except ZeroDivisionError:
        print("cannot divide by 0")
        result = 0
    except:
        print("Some other error occured")
    else:
        print("Division successful")
    finally:
        print("Operation Completes")
    return result
        
print(exception_method(10))
print(exception_method(0))
