import sys,os,pprint
trace=False
dirname=input('path:')
allsizes=[]
for (thisdir,subshere,fileshere) in os.walk(dirname):
    if trace:
        print(thisdir)
    for filename in fileshere:
        if filename[-3:]=='.py':
            if trace:
                print('...',filename)
            fullname=os.path.join(thisdir,filename)
            fullsize=os.path.getsize(fullname)
            allsizes.append((fullsize,fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint('-'*100)
pprint.pprint(allsizes[-2:])
pprint.pprint('-'*100)
pprint.pprint(allsizes)
