Thread pool
============
This is a simple thread pool for python(using queue module).

Usage:
============
It's so easy to use^_^

- Firstly, you should define a callback to deal with your task.


        def do_work(*args, **kwds):
            # do something
        
- Then, you can create a thread pool to schedule your tasks.
    
        # Create thread pool with nums threads
        pool = threadpool.ThreadPool(nums)
        # Add a task into pool
        pool.add_task(do_work, args, kwds)
        # Join and destroy all threads
        pool.destroy()
    
