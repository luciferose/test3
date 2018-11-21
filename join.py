import os,sys
redsize=1024

def join(fromdir,tofile):
    output=open(tofile,'wb')
    parts=os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath=os.path.join(fromdir,filename)
        fileobj=open(filepath,'rb')
        while True:
            filebytes=fileobj.read(redsize)
            if not filebytes:
                break
            output.write(filebytes)
        fileobj.close()
    output.close()

if __name__=='__main__':
    if len(sys.argv)==2 and sys.argv[1]=='- help':
        print('use: join [from-dir-name to-file-name]')
    else:
        if len(sys.argv) !=3:
            interactive=True
            fromdir=input('dircctory containing part files?')
            tofile=input('name of file to be recreated?')
        else:
            interactive=False
            fromdir,tofile=sys.argv[1:]
        absfrom,absto=map(os.path.abspath,[fromdir,tofile])
        print('joining',absfrom,'to make',tofile)
        try:
            join(fromdir,tofile)
        except:
            print('error joining files:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('join complete: see',absto)
        if interactive:input('press enter key')
