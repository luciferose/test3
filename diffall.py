import os,dirdiff
blocksize=1024*1024

def intersect(seq1,seq2):
    return [item for item in seq1 if item in seq2]

def comparetrees(dir1,dir2,diffs,verbose=False):
    print('-'*100)
    names1=os.listdir(dir1)
    names2=os.listdir(dir2)
    if not dirdiff.comparedirs(dir1,dir2,names1,names2):
        diffs.append('unique files at %s - %s' % (dir1,dir2))
    print('comparing contents')
    common=intersect(names1,names2)
    missed=common[:]
    for name in common:
        path1=os.path.join(dir1,name)
        path2=os.path.join(dir2,name)
        if os.path.isfile(path1) and os.path.isfile(path2):
            missed.remove(name)
            file1=open(path1,'rb')
            file2=open(path2,'rb')
            while True:
                bytes1=file1.read(blocksize)
                bytes2=file2.read(blocksize)
                if (not bytes1) and (not bytes2):
                    if verbose:print(name,'matches')
                    break
                if bytes1 != bytes2:
                    diffs.append('files differ at %s - %s' % (path1,path2))
                    print(name,'differs')
                    break
    for name in common:
        path1=os.path.join(dir1,name)
        path2=os.path.join(dir2,name)
        if os.path.isdir(path1) and os.path.isdir(path2):
            missed.remove(name)
            comparetrees(path1,path2,diffs,verbose)
            for name in missed:
                diffs.append('files missed at %s - %s: %s' % (dir1,dir2,name))
                print(name,'differs')

if __name__=='__main__':
    dir1,dir2=dirdiff.getargs()
    diffs=[]
    comparetrees(dir1,dir2,diffs,True)
    print('='*100)
    if not diffs:
        print('no diffs found.')
    else:
        print('diffs found:',len(diffs))
        for diff in diffs:
            print('-',diff)