# 4.18 Palindrome-Checker

def palchecker(aString):
    # Create an empty list to act as a deque
    chardeque = []

    # Add each character of the string to the list
    for ch in aString:
        chardeque.append(ch)  # Add to the end of the list
        # print(ch)

    stillEqual = True  # Assume the string is a palindrome initially

    # Check characters from both ends of the list
    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop(0)  # Remove and get the first character
        last = chardeque.pop()     # Remove and get the last character
        if first != last:          # Compare the two characters
            stillEqual = False      # If they are not equal, it's not a palindrome

    return stillEqual  # Return whether the string is a palindrome

# Example usage
print(palchecker("lsdkjfskf"))  # Output: False
print(palchecker("radar"))       # Output: True
