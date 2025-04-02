# 3.2 what is algorithm analysis?

# class: blueprint for creating objects in programming
# algorithm: step-by-step procedure for solving a problem, how to achieve a specific result, regardless of programming language used

# both functions below are doing the same thing just written differently

# easy to read

def sumOfN(n):
  theSum = 0
  for i in range(1, n + 1):
    theSum += i
    print(i)
  return theSum

# print(sumOfN(8))

# difficult to read
  
def foo(tom):
    fred = 0  # Start with zero treats
    for bill in range(1, tom + 1):  # For each dog from 1 to tom
        barney = bill  # This step is unnecessary
        fred = fred + barney  # Add the treat count
    return fred  # Return the total count

# print(foo(9))

# measuring resources

# memory - how much memory algorithm uses lots of dogs = remebering amount of treats each one got = space taken in memory
# time - how long it takes to run algorithm = how long it takes to give all of the dogs their treats
# benchmarking - measuring how long it takes a function to run
# steps
'''
1. start timer
2. count treats
3. stop timer
4. calculate difference
'''

import time  # Import the time module

def sumOfNu(n):
    start = time.time()  # Start the timer
    theSum = 0  # Start with zero treats
    for i in range(1, n + 1):  # For each dog from 1 to n
        theSum = theSum + i  # Add the treat count
    end = time.time()  # Stop the timer
    return theSum, end - start  # Return the total count and the time taken

print(f'Sum of Nu: {sumOfNu(8)}')

# run and compare times you will notice numOfN3 is quicker.... why?

def sumOfN3(n):
    return (n * (n + 1)) / 2  # Uses a formula to calculate the sum

for n in [8, 100, 1000]:
    start = time.time()
    result = sumOfN3(n)
    end = time.time()
    print(f"Sum is {result} required {end - start} seconds")

# final thoughts
'''
I believe there is a balance of what is readable and most efficient sometimes the most efficient
way to write something may not be the easiest to read.... just a theory
'''