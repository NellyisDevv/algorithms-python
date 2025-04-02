import math
import timeit

def greatestcomdom(a, b):
  return f'Greatest Common Denominator: {math.gcd(a, b)}'

# print(greatestcomdom(2, 3))

a = 48
b = 18

execution_time = timeit.timeit('greatestcomdom(a, b)', globals=globals(), number=1000)
print(f'Execution time: {execution_time} seconds')




