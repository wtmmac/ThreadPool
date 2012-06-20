import threading, Queue, time, sys



class ThreadPool(Threading.Thread):
    def __init__(self, numThreads=MAXTHREADS):
        self.inQueue  = Queue.Queue()
        self.outQueue = Queue.Queue()
        self.errQueue = Queue.Queue()
        self.pool = []
        for 
        

def report_error():
    ''' we "report" errors by adding error information to errQueue '''
    errQueue.put(sys.exc_info()[:2])

def get_all_from_queue(Q):
    ''' generator to yield one after the others all items currently
        in the Queue Q, without any waiting
    '''
    try:
        while True:
            yield Q.get_nowait()
    except Queue.Empty:
        raise StopIteration
    
def do_work_from_queue():
    ''' the get-some-work, do-some-work main loop of worker threads '''
    while True:
        command, item = inQueue.get()       # implicitly stops and waits
        if command == 'stop':
            break
        try:
            # simulated work functionality of a worker thread
            if command == 'process':
                result = 'new' + item
            else:
                raise ValueError, 'Unknown command %r' % command
        except:
            # unconditional except is right, since we report _all_ errors
            report_error()
        else:
            outQueue.put(result)
            
def make_and_start_thread_pool(number_of_threads_in_pool=5, daemons=True):
    ''' make a pool of N worker threads, daemonize, and start all of them '''
    for i in range(number_of_threads_in_pool):
         new_thread = threading.Thread(target=do_work_from_queue)
         new_thread.setDaemon(daemons)
         Pool.append(new_thread)
         new_thread.start()
         
def request_work(data, command='process'):
    ''' work requests are posted as (command, data) pairs to inQueue '''
    inQueue.put((command, data))
    
def get_result():
    return outQueue.get()     # implicitly stops and waits

def show_all_results():
    for result in get_all_from_queue(outQueue):
        print 'Result:', result
        
def show_all_errors():
    for etyp, err in get_all_from_queue(errQueue):
        print 'Error:', etyp, err

def stop_and_free_thread_pool():
    # order is important: first, request all threads to stop...:
    for i in range(len(Pool)):
        request_work(None, 'stop')
    # ...then, wait for each of them to terminate:
    for existing_thread in Pool:
        existing_thread.join()
    # clean up the pool from now-unused thread objects
    del Pool[:]
