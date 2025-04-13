# 4.14 printer simulation

from collections import deque
import time

class PrintJob:
  def __init__(self, name, pages):
    self.name = name
    self.pages = pages
  
  def __str__(self):
    return f"{self.name} ({self.pages} pages)"
  
def print_tasks(jobs):
  queue = deque(jobs)
  
  while queue: # Create a queue from the list of print jobs
    current_job = queue.popleft() # Get the job at the front of the queue
    print(f"Printing {current_job}")
    time.sleep(current_job.pages)  # Simulate the time taken to print
    print(f"Finished printing {current_job}.")
    
# Example usage
jobs = [
    PrintJob("Document1", 3),
    PrintJob("Document2", 5),
    PrintJob("Document3", 2)
]

print_tasks(jobs)

