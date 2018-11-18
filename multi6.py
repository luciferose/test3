import os
from multiprocessing import Pool

def powers(x):
    #print(os.getpid())
    return 2**x

if __name__=='__main__':
    workers=Pool(processes=5)
    results=workers.map(powers,[2]*100)
    print(results)
    print(results[:16])
    print(results[-2:])
    print('*'*100)

    results=workers.map(powers,range(100))
    print(results)
    print(results[:16])
    print(results[-2:])wge