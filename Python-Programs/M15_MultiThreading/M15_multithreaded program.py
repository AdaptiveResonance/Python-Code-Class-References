# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 20:02:48 2021

"""

import threading, time

""" Define a method for running in multithreaded envrioment
This method prints the thread name and the current value of 1"""
def printing():
    for i in range(1,6):
        """Sleep for one second before printing"""
        time.sleep(1)
        print(threading.current_thread().getName(), i)

""" Create thread objects for use and assign a target method to execute"""
thread1 = threading.Thread(target = printing,name="Thread1")
thread2 = threading.Thread(target = printing, name="Thread2")

"""Accessing the main threads"""
print(threading.main_thread().getName())

"""Enumerate to access all threads"""
for threads in threading.enumerate():
    print(threads)

print()
""" Starting the threads"""
thread1.start()
thread2.start()

""" Making the main thread wait until thread1 and thread2 completes
main thread calls the join method on thread1 and thread2 and 
hence main_thread has to wait until these two threads complete"""
thread1.join()
thread2.join()