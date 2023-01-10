# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:10:21 2021

"""

import threading

x = 0

def update_num():
    global x
    for _ in range(1000000):
        x = 2 * int(threading.current_thread().getName()) - 1 
    
thread1 = threading.Thread(target = update_num, name = "1")
thread2 = threading.Thread(target = update_num, name = "2")
thread3 = threading.Thread(target = update_num, name = "3")
thread4 = threading.Thread(target = update_num, name = "4")

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
   
print("x =",x)
