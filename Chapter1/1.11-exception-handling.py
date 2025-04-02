import math

# expection handling

anumber = -1

try:
    print(math.sqrt(anumber))
except:
    print("Bad Value for square root")
    print("Using absolute value instead")
    print(math.sqrt(abs(anumber)))

'''
if anumber < 0:
    raise RuntimeError("You can't use a negative number!")
else:
    print(math.sqrt(anumber))
'''