import  os
from multiprocessing import Process,Pipe

def sender(pipe):
    pipe.send(['spam']+[42,'egges'])
    pipe.close()

def talker(pipe):
    pipe.send(dict(name='bob',spam=42))
    replay=pipe.recv()
    print('talk got:',replay)

if __name__=='__main__':
    (parentend,childend)=Pipe()
    Process(target=sender,args=(childend,)).start()
    print('parent got:',parentend.recv())
    parentend.close()

    (parentend, childend) = Pipe()
    child=Process(target=talker,args=(childend,))
    child.start()
    print('parent got:',parentend.recv())
    parentend.send({x*2 for x in 'spam'})
    child.join()
    print('parent exit.')