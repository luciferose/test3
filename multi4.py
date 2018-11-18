import os,time,queue
from multiprocessing import Process,Queue,Lock

class counter(Process):
    label=' @'
    def __init__(self,start,queue,lock):
        self.state=start
        self.post=queue
        self.lock=lock
        Process.__init__(self)

    def run(self):
        for i in range(3):
            time.sleep(1)
            self.state+=1
            with lock:
                print(self.label,self.pid,self.state)
                self.post.put([self.pid,self.state])
        print(self.label,self.pid,'-')

if __name__=='__main__':
    print('start',os.getpid())\
    expected=9

    post=Queue()
    lock=Lock()
    p=counter(0,post,lock)
    q=counter(100,post,lock)
    r=counter(1000,post,lock)
    p.start()
    q.start()
    r.start()

    while expected:
        time.sleep(0.5)
        try:
            data=post.get(block=False)
        except queue.Empty:
            print('no data ...')
        else:
            print('posted',data)
            expected-=1

    p.join()
    q.join()
    r.join()
    print('finish',os.getpid(),r.exitcode)