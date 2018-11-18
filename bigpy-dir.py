import os,glob,sys
dirname= '/Users/lucifer/test3' if len(sys.argv)==1 else sys.argv[1]

allsize=[]
allpy=glob.glob(dirname+os.sep+'*.py')
for filename in allpy:
    filesize=os.path.getsize(filename)
    allsize.append((filesize,filename))

allsize.sort()
print(allsize[:2])
print(allsize[-2:])