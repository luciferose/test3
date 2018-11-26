import os,sys
findonly=False
rootdir=os.getcwd() if len(sys.argv)==1 else sys.argv[1]

found=removed=0
for (thisdirlevel,subshere,fileshere) in os.walk(rootdir):
    for filename in fileshere:
        if os.path.splitext(filename)[1]=='.pyc':
            fullname = os.path.join(thisdirlevel,filename)
            print('=>',fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed+=1
                except:
                    type,inst=sys.exc_info()[:2]
                    print('*'*4,'failed:',filename,type,inst)
        found+=1

print('found',found,'files,removed',removed)