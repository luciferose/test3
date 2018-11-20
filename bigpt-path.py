import sys,os,pprint
trace=0
visited={}
allsizes=[]
for srcdir in sys.path:
    for (thisdir,subshere,fileshere) in os.walk(srcdir):
        if trace>0:
            print(thisdir)
        thisdir=os.path.normpath(thisdir)
        fixcase=os.path.normcase(thisdir)
        if fixcase in visited:
            continue
        else:
            visited[fixcase]=True
        for filename in fileshere:
            if filename[-3:]=='.py':
                if trace > 1:
                    print('...',filename)
                pypath=os.path.join(thisdir,filename)
                try:
                    pysize=os.path.getsize(pypath)
                except os.error:
                    print('skipping',pypath,sys.exc_info()[0])
                else:
                    pylines = len(open(pypath, 'rb').readlines())
                    allsizes.append((pysize,pylines,pypath))

print('by size...')
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

print('by lines...')
allsizes.sort(key=lambda x:x[1])
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])