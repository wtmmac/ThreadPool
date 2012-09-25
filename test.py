import threadpool
import logging
import time

logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
        )

def doWork(*args, **kwds):
    logging.debug('starting')
    logging.debug('args is ' + str(args) + ' kwds is ' + str(kwds))
    logging.debug('exiting')

if __name__ == "__main__":
    logging.debug('Initialize thread pool and spawn 3 threads.')
    pool = threadpool.ThreadPool(3)
    logging.debug('Add 10 tasks to thread pool.')
    for i in range(20):
        pool.add_task(doWork, i, a=i)
    logging.debug('Wait for a while untill all tasks have been processed')
    time.sleep(1)
    logging.debug('Destroy thread pool and join threads')
    pool.destroy()