import threading

x = 0

def incr():
    global x
    x += 1

def update(lock):
    for _ in range(1000000):
        lock.acquire()
        incr()
        lock.release()

lock = threading.Lock()
thread1 = threading.Thread(target=update, args=[lock])
thread2 = threading.Thread(target=update, args=[lock])
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(x)
