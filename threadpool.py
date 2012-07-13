import unittest
import threading, Queue, time, sys


class Worker(threading.Thread):
    def __init__(self, inQueue, outQueue, errQueue):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.errQueue = errQueue
        self.start() 
    
    def run(self):
        while True:
            command, callable, args, kwds = self.inQueue.get()
            if command == 'stop':
                break
            try:
                if command != 'process':
                    raise ValueError, 'Unknown command %r' % command
            except:
                self.reportError() 
            else:
                self.outQueue.put(callable(*args, **kwds))
                
    def dismiss(self):
        print "dismiss"
        command = 'stop'
        self.inQueue.put((command, None, None, None))
        
    def reportErr(self):
        ''' we "report" errors by adding error information to errQueue '''
        self.errQueue.put(sys.exc_info()[:2])

maxThreads = 32 

class ThreadPool():
    def __init__(self, numThreads, poolSize=0):
        if numThreads > maxThreads:
            numThreads = maxThreads
        self.inQueue  = Queue.Queue(poolSize)
        self.outQueue = Queue.Queue(poolSize)
        self.errQueue = Queue.Queue(poolSize)
        self.pool = {}
        for i in range(numThreads):
            newThread = Worker(self.inQueue, self.outQueue, self.errQueue)
            self.pool[i] = newThread
            
    def addTask(self, callable, *args, **kwds):
        command = 'process' 
        self.inQueue.put((command, callable, args, kwds))

    def _getAllResults(self, queue):
        ''' generator to yield one after the others all items currently
            in the queue, without any waiting
        '''
        try:
            while True:
                yield queue.get_nowait()
        except Queue.Empty:
            print "empty"
            raise StopIteration
    
    def getTask(self):
        return self.outQueue.get()    

    def showAllResults(self):
        for result in self._getAllResults(self.outQueue):
            print 'Result:', result
        
    def showAllErrors(self):
        for etyp, err in self._getAllResults(self.errQueue):
            print 'Error:', etyp, err

    def dismissWorkers(self):
        # order is important: first, request all threads to stop...:
        for i in self.pool:
            self.pool[i].dismiss()
        # ...then, wait for each of them to terminate:
        for i in self.pool:
            self.pool[i].join()
        # clean up the pool from now-unused thread objects
        print self.pool
        del self.pool



def doWork(*args, **kwds):
    return kwds 

if __name__ == "__main__":
    pool = ThreadPool(5)
    for i in range(10):
        pool.addTask(doWork, a=i, b=i*2)
    # wait untill all tasks have been processed
    time.sleep(1)
    pool.showAllResults()
    pool.dismissWorkers()
    print "done"


