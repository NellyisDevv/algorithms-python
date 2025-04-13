# 4.16 deque 

"""
A deque (pronounced "deck") is a data structure that stands for double-ended queue. It allows you to add and remove elements from both ends (the front and the back) efficiently. This makes deques more flexible than regular queues or stacks, which only allow operations at one end.
"""

class Deque:
  def __init__(self):
    self.items = [] # Initialize an empty list to hold the deque items
    
  def is_empty(self):
    return len(self.items) == 0 # check if deque is empty
  
  def add_rear(self, item):
    self.items.append(item) # add an item to back of deque
    
  def remove_front(self):
    if not self.is_empty:
      return self.items.pop(0) # return and remove front item
    else:
      return None # return None if the deque is empty
  
  def remove_rear(self):
    if not self.is_empty():
      return self.items[0] # Return the front item without removing it
    else:
      return None
  
  def peek_rear(self):
    if not self.is_empty():
      return self.items[-1] # return the back item without removing it
    else:
      return None
  
  def size(self):
    return len(self.items) # return the number of items in the deque

# Example usage
deque = Deque()
deque.add_rear(1)
deque.add_rear(2)
deque.add_front(0)
print("Front item:", deque.peek_front())  # Output: 0
print("Back item:", deque.peek_rear())    # Output: 2
print("Size of deque:", deque.size())      # Output: 3

removed_item = deque.remove_front()
print("Removed from front:", removed_item)  # Output: 0
print("Size of deque after removal:", deque.size())  # Output: 2