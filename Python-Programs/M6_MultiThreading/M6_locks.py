# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:10:21 2021

"""

import threading

x = 0

def update_num(lock):
    global x
    lock.acquire(True)
    for _ in range(1000000):
        x = 2 * int(threading.current_thread().getName()) - 1 
    lock.release()

lock = threading.Lock()    
thread1 = threading.Thread(target = update_num, name = "1", args=(lock,))
thread2 = threading.Thread(target = update_num, name = "2", args=(lock,))
thread3 = threading.Thread(target = update_num, name = "3", args=(lock,))
thread4 = threading.Thread(target = update_num, name = "4", args=(lock,))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
   
print("x =",x)
