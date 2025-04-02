def gcd(a, b):
  while(b):
    a, b = b, a % b
  return a

num1 = 7
num2 = 3
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")