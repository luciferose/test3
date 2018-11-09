import _thread as thread
stdoutmutex=thread.allocate_lock()
exitmutexes=[False]*10

def counter(myid,count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myid,i))
        stdoutmutex.release()
    exitmutexes[myid]=True

for i in range(10):
    thread.start_new_thread(counter,(i,100))
while False in exitmutexes:
    pass
print('main thread exiting.')