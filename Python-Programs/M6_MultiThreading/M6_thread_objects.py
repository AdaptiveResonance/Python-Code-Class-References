# -*- coding: utf-8 -*-
import threading

class myThread(threading.Thread):
    
    def __init__(self, thread_name):
        threading.Thread.__init__(self,name=thread_name)
            
    """ Define a method run with the code to run in 
    multithreaded envrioment
    This method prints the thread name and the current value of 1"""
    def run(self):
        for i in range(1,6):
            print(threading.current_thread().getName(),i)

""" Create thread objects for use"""
thread1 = myThread(thread_name="Thread1")
thread2 = myThread(thread_name="Thread2")

""" Starting the threads"""
thread1.start()
thread2.start()

""" Making the main thread wait until thread1 and thread2 completes
main thread calls the join method on thread1 and thread2 and 
hence main_thread has to wait until these two threads complete"""
thread1.join()
thread2.join()
