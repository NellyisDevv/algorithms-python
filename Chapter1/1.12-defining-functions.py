import string
import random

def square(n):
  return n**2

print(square(3))

def squareroot(n):
  root = n / 2
  for k in range(20):
    root = (1/2) * (root + (n / root))
  return root

print(squareroot(100))

for i in range(3):
  print (i)
  
letters = string.ascii_letters

def randomchar():
  randomstring = []
  i = 0
  while i <= 20:
   randomstring.append(random.choice(letters))
   i += 1
  return ''.join(randomstring)
   
  
print(randomchar())