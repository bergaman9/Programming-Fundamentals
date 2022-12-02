""" A Queue of Groceries to Put Away """

# create a new queue object
import queue
q = queue.Queue()
print(q.empty())

# put bags into the queue
q.put('bag1')
print(q.empty())
q.put('bag2')
q.put('bag3')

# get bags from the queue in FIFO order
print(q.get())
print(q.get())
print(q.get())
# q.get() # causes an error

# create a new queue to hold two items
q = queue.Queue(2)
print(q.empty())

# put two bags into the two-item queue
q.put('bag1')
print(q.full())
q.put('bag2')
print(q.full())

# try to put an extra bag into the queue
q.put_nowait('bag3') # causes an error
