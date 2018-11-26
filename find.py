import fnmatch,os

def find(pattern,startdir=os.curdir):
    for (thisdir,subhere,fileshere) in os.walk(startdir):
        for name in subhere+fileshere:
            if fnmatch.fnmatch(name,pattern):
                fullpath=os.path.join(thisdir,name)
                yield fullpath

def findlist(pattern,startdir=os.curdir,dosort=False):
    matches=list(find(pattern,startdir))
    if dosort:matches.sort()

if __name__=='__main__':
    import sys
    namepattern,startdir=sys.argv[1],sys.argv[2]
    for name in find(namepattern,startdir):print(name)