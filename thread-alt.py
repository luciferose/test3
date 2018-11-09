import _thread as thread
import time

def action(i):
    print('1:',i**32,end='\n')

class Power:
    def __init__(self,i):
        self.i=i
    def action(self):
        print('2:',self.i**32,end='\n')

thread.start_new_thread(action,(2,))
time.sleep(1)
thread.start_new_thread((lambda: action(2)),())
time.sleep(1)
obj=Power(2)
thread.start_new_thread(obj.action,())

time.sleep(1)
print('main thread exiting.')