#coding: utf-8

import _thread
import time
import queue
import threading
import sys
import gc

#threads return value methods
thread00Flag = False
thread01Flag = False
#【★★★★★】 have good methods
thread02Flag = False
#semphore
thread03Flag = False
#lock or Rlock
thread04Flag = False
#【★★★★★】 return methods 
thread05Flag = True

# time print function
if thread00Flag :
    def foo(bar, baz):
        print ("hello {0}".format(bar))
        return "foo" + baz

    from multiprocessing.pool import ThreadPool
    pool = ThreadPool(processes=1)

    async_result = pool.apply_async(foo, ('world', 'ice')) # tuple of args for foo

    # do some other stuff in the main process

    return_val = async_result.get()  # get the return value from your function.

    print(return_val)

if thread01Flag:
    def print_time( threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print ("{0}: {1}".format( threadName, time.ctime(time.time()) ))

    # two thread
    try:
        _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
        _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
    except:
        print ("Error: can't start threads")

    #loop main source
    #while 1:
    #    pass
    while 0:
        pass

#【★★★★★】 if want to return , class def join return you methods
if thread02Flag :
    exitFlag = 0

    class myThread (threading.Thread):
        def __init__(self, threadID, name, q):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.q = q

        def run(self):
            print ("start threads ：" + self.name)
            process_data(self.name, self.q)
            print ("exit threads ：" + self.name)

        def join(self):
            return "icewindful"
            

    def process_data(threadName, q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print ("%s processing : %s" % (threadName, data))
            else:
                queueLock.release()
            time.sleep(0.00000001)

    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    nameList = ["(1) One", "(2) Two", "(3) Three", "(4) Four", "(5) Five","(6) Six","(7) Seven","(8) Eight","(9) Nine","(10) Ten"]
    queueLock = threading.Lock()
    QueueLen = len(nameList)
    print("QL = {Len}".format(Len = QueueLen))
    workQueue = queue.Queue(QueueLen)
    threads = []
    threadID = 1

    # build threads 
    for tName in threadList:
        thread = myThread(threadID, tName, workQueue)
        thread.start()
        threads.append(thread)
        threadID += 1

    for i in range(0-2):
        print(threads[i])
    # 
    #queueLock.acquire()
    queueLock.acquire(blocking=True, timeout=10)
    for word in nameList:
        workQueue.put(word)
    queueLock.release()

    # wait Queue clear
    while not workQueue.empty():
        pass

    # all Queue finish set exitFlag = 1
    exitFlag = 1

    #counts = 0
    # wait all threads finish
    for t in threads:
        #counts +=1
        #print ("counts = {counts}".format(counts = counts ))
        string = t.join()
        print(string)

        """
        t.join() split funtion like :

        threads[0].join()
        threads[1].join()
        threads[2].join()
        """

        #print(t)
    print ("Exit main process")


if thread03Flag :

    class Worker(threading.Thread):
        def __init__(self, queue, num, semaphore):
            threading.Thread.__init__(self)
            self.queue = queue
            self.num = num
            self.semaphore = semaphore
        def run(self):
            while self.queue.qsize() > 0:
                msg = self.queue.get()
                # get semaphoreflag
                semaphore.acquire()
                print("Semaphore acquired by Worker {d}".format(d = self.num))
                # allow mulite process threads
                print("Worker {d}: {s}".format(d = self.num , s = msg))
                time.sleep(1)
                # release semaphore process
                print("Semaphore released by Worker {d}".format(d = self.num))
                self.semaphore.release()
    
    my_queue = queue.Queue()
    for i in range(20):
        my_queue.put("Data {d}".format(d = i))
    # build thread semaphore 
    semaphore = threading.Semaphore(2)
    #asign threads 
    my_worker1 = Worker(my_queue, 1, semaphore)
    my_worker2 = Worker(my_queue, 2, semaphore)
    my_worker3 = Worker(my_queue, 3, semaphore)
    my_worker1.start()
    my_worker2.start()
    my_worker3.start()
    my_worker1.join()
    my_worker2.join()
    my_worker3.join()
    print("Done.")

if thread04Flag:
    class Worker(threading.Thread):
        def __init__(self, queue, num, lock):
            threading.Thread.__init__(self)
            self.queue = queue
            self.num = num
            self.lock = lock

        def run(self):
            while self.queue.qsize() > 0:
                msg = self.queue.get()

                # lock quire
                self.lock.acquire(timeout=10)
                """
                self.rlock.acquire(timeout=10) #one lock
                self.rlock.acquire(timeout=10) #two lock
                """
                print("Lock acquired by Worker {d}".format(d= self.num))

                # mutex lock
                print("Worker {d}: {s}".format(d = self.num, s = msg))
                time.sleep(0.00000001)

                # lock release
                print("Lock released by Worker {d}".format(d = self.num))
                self.lock.release()
                """
                self.rlock.release()
                self.rlock.release()
                """

    my_queue = queue.Queue()
    for i in range(10):
        my_queue.put("Data {d}".format(d = i))

    # 建立 lock
    lock = threading.Lock()

    """
    lock = threading.RLock(timeout=10)
    """

    my_worker1 = Worker(my_queue, 1, lock)
    my_worker2 = Worker(my_queue, 2, lock)

    my_worker1.start()
    my_worker2.start()

    my_worker1.join()
    my_worker2.join()

    print("Done.")

if thread05Flag:
    def foo(bar, result, index):
        print ("hello {0}{1}".format(bar,index))
        result[index] = str(index)

    from threading import Thread

    threads = [None] * 10
    results = [None] * 10

    for i in range(len(threads)):
        threads[i] = Thread(target=foo, args=('world!', results, i))
        threads[i].start()

    # do some other stuff

    for i in range(len(threads)):
        threads[i].join()

    print (" ".join(results))  # what sound does a metasyntactic locomotive make?

    import concurrent.futures

    def fooconcurrent(bar):
        print("hello {0}".format(bar))
        return "icewindful"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(fooconcurrent, 'world!')
        try:
            return_value = future.result(timeout=10)
        except :
            print("sys.exc_info()[0]: {err}".format(err = sys.exc_info()[0]))
        else :
            print(return_value)
        
gc.collect()