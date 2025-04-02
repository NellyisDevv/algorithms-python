import timeit

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a = 48
b = 18

execution_time = timeit.timeit('gcd(a, b)', globals=globals(), number=10000)

print(f"Execution time: {execution_time} seconds")


