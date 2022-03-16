#coding: utf-8

import _thread
import time
import queue
import heapq
import threading
import sys
import random
import gc

PriorityFlag = False
HeapqFlag = False
TheadsPriorityFlag = True

if PriorityFlag :
    q = queue.PriorityQueue()

    q.put((2, 'code'))
    q.put((1, 'eat'))
    q.put((3, 'sleep'))

    while not q.empty():
        next_item = q.get()
        print(next_item)


if HeapqFlag:
    q = []

    heapq.heappush(q, (2, 'code'))
    heapq.heappush(q, (1, 'eat'))
    heapq.heappush(q, (3, 'sleep'))

    while q:
        next_item = heapq.heappop(q)
        print(next_item)

if TheadsPriorityFlag:
    priority_queue = queue.PriorityQueue()

    def pop_nitems(n):
        for i in range(n):
            time.sleep(0.0000001)
            item = priority_queue.get()
            print("Thread : {0}. Retrieved & Proccessed Item : {1}".format(threading.current_thread().name, item))
            #print("Thread {}. Processed Item : {}".format(threading.current_thread().name, item))
            priority_queue.task_done()


    if __name__ == "__main__":

        for i in range(1, 13):
            priority_queue.put((random.randint(1, 51), "Task-{0}".format(i)))

        thread1 = threading.Thread(target=pop_nitems, args=(3, ), name="L3")
        thread2 = threading.Thread(target=pop_nitems, args=(4, ), name="L4")
        thread3 = threading.Thread(target=pop_nitems, args=(5, ), name="L5")

        thread1.start()
        thread2.start()
        thread3.start()

        priority_queue.join()

        print("\nAll items in queue completed. Exited from Main Thread\n")

gc.collect()