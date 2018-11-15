import os,time
def child(pipeout):
    zzz=0
    while True:
        time.sleep(zzz)
        msg = ('spam %3d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5

def parent():
    pipein,pipeout=os.pipe()
    if os.fork()==0:
        os.close(pipein)
        child(pipeout)
    else:
        os.close(pipeout)
        pipein=os.fdopen(pipein)
        while True:
            line=pipein.readline()[:-1]
            print('parent %d got [%s] at %s' % (os.getpid(),line,time.time()))

parent()