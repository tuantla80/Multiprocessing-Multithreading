### 1. [Multiprocessing](https://github.com/tuantla80/Multiprocessing-Multithreading/blob/master/Multiprocessing.ipynb)  
> 1. What is a multiprocessing?  
> &rarr; It is to run a program in multiple CPU (core).
  
> 2. When it is good for?   
> &rarr; It is good for multi CPU bound problem. (Such as a problem which is tightly bound 'for' loop)  
  
> 3. Multiprocessing properties:  
    Seperate memory   
    
> 4. **For multiprocessing, it is suggested to run in Python instead of Jupyter Notebook**  
### 2. [Multithreading](https://github.com/tuantla80/Multiprocessing-Multithreading/blob/master/Multithreading.ipynb)  
> 1. What is a thread?  
> &rarr; Thread is the smallest unit (taks or program) that is scheduled to be done by an Operating System.
  
> 2. When it is good for?   
> &rarr; It is good for Network and I/O bound problem such as download images from a website.  
> &rarr; Especially good to use on tasks that run pretty much independent of each other.
  
> 3. Thread properties:  
    One or multi threads can run parallel on a process (CPU).  
    Threads in same process (CPU) share the state and space (memory).  
    All threads should communicate back to the main thread.  
### 3. [concurrent.futures module](https://github.com/tuantla80/Multiprocessing-Multithreading/blob/master/concurrent.futures.ipynb)  
> A high-level interface for asynchronously executing callables.  
> Both thread (ThreadPoolExecutor) and process (ProcessPoolExecutor) implement in the same interface.  
### 4. [Mix multiprocessing and multithreading](https://github.com/tuantla80/Multiprocessing-Multithreading/blob/master/multiprocessing_multithreading.py)  
> **In general, it is not recommended to mix multiprocessing and multithreading together in the same program**. In some special cases, however, we many combine them. This code will show how to do it.   
### 5. Terminate all the processes if one process has met the certain condition   
> In some case, we may not need to wait for all processes to finish. But instead if one process has met the certain condition, we can stop all the processes.  
#### 5.1. [Using terminate method]()   
> Please take care when using terminate method by reading Python multiprocessing document.  
#### 5.2 [Using multiprocessing Event]()  
> In fact, it is a clone of threading event.
