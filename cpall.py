import os,sys
maxfileload=1000000
blksize=1024*500

def copyfile(pathfrom,pathto,maxfileload=maxfileload):
    if os.path.getsize(pathfrom)<=maxfileload:
        bytesfrom=open(pathfrom,'rb').read()
        open(pathto,'wb').write(bytesfrom)
    else:
        filefrom=open(pathfrom,'rb')
        fileto=open(pathto,'wb')
        while True:
            bytesfrom=filefrom.read(blksize)
            if not bytesfrom:break
            fileto.write(bytesfrom)

def copytree(dirfrom,dirto,verbose=0):
    fcount=dcount=0
    for filename in os.listdir(dirfrom):
        pathfrom=os.path.join(dirfrom,filename)
        pathto=os.path.join(dirto,filename)
        if not os.path.isdir(pathfrom):
            try:
                if verbose>1:print('copying',pathfrom,'to',pathto)
                copyfile(pathfrom,pathto)
                fcount+=1
            except:
                print('error copying',pathfrom,'to',pathto)
                print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            if verbose:print('copying dir',pathfrom,'to',pathto)
            try:
                os.mkdir(pathto)
                below=copytree(pathfrom,pathto)
                fcount+=below[0]
                dcount+=below[1]
                dcount+=1
            except:
                print('error creating',pathto,'---skipped')
                print(sys.exc_info()[0],sys.exc_info()[1])
    return (fcount,dcount)

def getargs():
    try:
        dirfrom,dirto=sys.argv[1:]
    except:
        print('usage error: cpall.py dirfrom dirto')
    else:
        if not os.path.isdir(dirfrom):
            print('error: dirname is not dirctory')
        elif not os.path.exists(dirto):
            os.mkdir(dirto)
            print('note: dirto was created')
            return (dirfrom,dirto)
        else:
            print('warning: dirto already exists')
            if hasattr(os.path,'samefile'):
                same=os.path.samefile(dirfrom,dirto)
            else:
                same=os.path.abspath(dirfrom)==os.path.abspath(dirto)
            if same:
                print('error: dirfrom same as dirto')
            else:
                return (dirfrom,dirto)

if __name__=='__main__':
    import time
    dirstuple=getargs()
    if dirstuple:
        print('copying...')
        start=time.process_time()
        fcount,dcount=copytree(*dirstuple)
        print('copied',fcount,'file',dcount,'directories',end='')
        print('in',time.process_time()-start,'second')
