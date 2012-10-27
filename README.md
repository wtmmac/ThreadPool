Thread pool
============
This is a simple thread pool for python(using queue module).

Install:
============

        python setup.py install

Usage:
============

- Firstly, you should define a callback to deal with your task.


        def do_work(*args, **kwds):
            # do something
        
- Then, you can create a thread pool to schedule your tasks.
    
        from threadpool import ThreadPool
        # Create thread pool with nums threads
        pool = ThreadPool(nums)
        # Add a task into pool
        pool.add_task(do_work, args, kwds)
        # Join and destroy all threads
        pool.destroy()
    
