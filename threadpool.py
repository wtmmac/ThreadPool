import threading, Queue, time, sys


class Worker(Threading.Thread):
    def __init__(self, inQueue, outQueue, errQueue):
        Threading.Thread._ _init_ _(self, **kwds)
        self.setDaemon(True)
        self.inQueue = inQueue
        self.outQueue = outQueue
        self.errQueue = errQueue
        self.active = True
        self.start() 
    
    def run(self):
        while True:
            if !self.active:
                break
            try:
                callable, args, kwds = self.inQueue.get()
            except:
                self.reportError() 
            else:
                self.outQueue.put(callable(*args, **kwds))
                
    def dismiss(self):
        self.active = False
        
    def reportErr(self):
        ''' we "report" errors by adding error information to errQueue '''
        self.errQueue.put(sys.exc_info()[:2])

        
class ThreadPool():
    def __init__(self, numThreads, poolSize=0):
        self.inQueue  = Queue.Queue(poolSize)
        self.outQueue = Queue.Queue(poolSize)
        self.errQueue = Queue.Queue(poolSize)
        self.pool = {}
        for i in range(numThreads):
            newThread = Worder(self.inQueue, self.outQueue, self.errQueue)
            self.pool[i] = newThread
            
    def addTask(self, callable, *args, **kwds):
        self.inQueue.put((callable, args, kwds))

    def getAllResults(self, queue):
        ''' generator to yield one after the others all items currently
            in the queue, without any waiting
        '''
        try:
            while True:
                yield queue.get_nowait()
        except Queue.Empty:
            raise StopIteration
    
    def getTask(self):
        return self.outQueue.get()     # implicitly stops and waits

    def showAllResults(self):
        for result in getAllResults(self.outQueue):
            print 'Result:', result
        
    def showAllErrors(self):
        for etyp, err in get_all_from_queue(self.errQueue):
            print 'Error:', etyp, err

    def dismissWorkers(self):
        # order is important: first, request all threads to stop...:
        for i in pool:
            self.pool[i].dismiss
        # ...then, wait for each of them to terminate:
        for i in Pool:
            self.pool[i].join()
        # clean up the pool from now-unused thread objects
        del Pool
