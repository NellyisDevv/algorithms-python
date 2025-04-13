# 4.3 what is a stack?

class Stack:
  def __init__(self):
    self.items = []
    
  def push(self, item):
    self.items.append(item)
    
  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    return None
  
  def peek(self):
    if not self.is_empty():
      return len(self.items) == 0
    
  def size(self):
    return len(self.items)

# initialize a new stack class
my_stack = Stack()

# Push items onto the stack
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

# Check the size of the stack
print("Size of stack:", my_stack.size())  # Output: Size of stack: 3

# Peek at the top item
print("Top item:", my_stack.peek())  # Output: Top item: 30

# Pop items from the stack
print("Popped item:", my_stack.pop())  # Output: Popped item: 30
print("Popped item:", my_stack.pop())  # Output: Popped item: 20

# Check if the stack is empty
print("Is stack empty?", my_stack.is_empty())  # Output: Is stack empty? False

# Pop the last item
print("Popped item:", my_stack.pop())  # Output: Popped item: 10

# Check if the stack is empty again
print("Is stack empty?", my_stack.is_empty())  # Output: Is stack empty? True