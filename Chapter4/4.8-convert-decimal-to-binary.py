# 4.8 converting decimal numbers to binary numbers

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_digits = []
    
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2  # Use floor division to get the quotient
    
    binary_digits.reverse()  # Reverse the list to get the correct order
    return ''.join(binary_digits)

# Example usage
print(decimal_to_binary(13))  # Output: 1101

# step one
print(13 % 2)
'''
13 / 2 = 6.5
6 x 2 = 12
13 - 12 = 1
'''

# step two
# append digit 1 into binary_digits list as a string

# step three
'''
value of n keeps getting updated until its 0 fulfilling n > 0 then run loop
'''
print(13 // 2)
print(6 // 2)
print(3 // 2)
print(1 // 2)
'''
13 // 2 = 6
6 // 2 = 3
etc
'''