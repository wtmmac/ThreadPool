import time
import threadpool

def doWork(*args, **kwds):
    return kwds 

if __name__ == "__main__":
    pool = threadpool.ThreadPool(5)
    for i in range(10):
        pool.addTask(doWork, a=i, b=i*2)
    # wait for a while untill all tasks have been processed
    time.sleep(1)
    pool.showAllResults()
    pool.dismissWorkers()
