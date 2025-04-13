class Queue:
  def __init__(self):
    self.items = []
    
  def is_empty(self):
    return len(self.items) == 0
  
  def enqueue(self, item):
    self.items.append(item) # add item to back of queue
    
  def dequeue(self):
    if not self.is_empty():
      return self.items.pop(0) # remove item from front of queue
    else:
      return None # if queue is empty return none
  
  def peek(self):
    if not self.is_empty():
      return self.items[0] # return front item without removing it
    else:
      return None # if queue is empty return none
    
  def size(self):
    return len(self.items) # return number of items in queue

queue = Queue()
print("Is the queue empty?", queue.is_empty())  # Output: True

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Front item:", queue.peek())  # Output: 1
print("Queue size:", queue.size())  # Output: 3

print("Dequeued item:", queue.dequeue())  # Output: 1
print("Front item after dequeue:", queue.peek())  # Output: 2 # because 1 was dequeued
print("Queue size after dequeue:", queue.size())  # Output: 2 # only 2 items in queue now
