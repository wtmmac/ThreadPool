ThreadPool
==========

A simple thread pool for python

Usage:

def doWork(*args, **kwds):
    return kwds 

pool = ThreadPool(5)
for i in range(10):
    pool.addTask(doWork, a=i, b=i*2)
# wait for a while untill all tasks have been processed
time.sleep(1)
pool.showAllResults()
pool.dismissWorkers()
