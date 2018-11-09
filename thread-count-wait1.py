import _thread as thread
stdoutmutex=thread.allocate_lock()
exitmutexes=[thread.allocate_lock() for i in range(10)]

def counter(myid,count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myid,i))
        stdoutmutex.release()
    exitmutexes[myid].acquire()

for i in range(10):
    thread.start_new_thread(counter,(i,100))
for mutex in exitmutexes:
    while not mutex.locked():
        pass
print('main thread exiting.')