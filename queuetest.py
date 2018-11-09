numconsumers=2
numproducers=4
nummessages=4

import _thread as thread,queue,timg
safeprint=thread.allocate_lock()
dataqueue=queue.Queue()

git push -u origin master