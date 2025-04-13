# 4.6 simple balanced parenthesis

def is_balanced(parentheses):
    stack = []  # Initialize an empty stack
    for char in parentheses:
        if char == '(':
            stack.append(char)  # Push opening parenthesis onto the stack
        elif char == ')':
            if not stack:
                return False  # Unmatched closing parenthesis
            stack.pop()  # Pop the matching opening parenthesis
    return len(stack) == 0  # Check if the stack is empty

# Test the function
print(is_balanced("(())"))  # Output: True
print(is_balanced("(()"))  # Output: False
print(is_balanced("())"))  # Output: False