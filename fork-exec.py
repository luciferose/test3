import  os
parm=0
while True:
    parm+=1
    pid=os.fork()
    if pid==0:
        os.execlp('python','python3.7','child.py',str(parm))
        assert False,'error starting program'
    else:
        print('child is',pid)
        if input()=='q':
            break