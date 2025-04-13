# 4.7 balanced symbols (a general case)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

def is_balanced(symbols):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}

    for symbol in symbols:
        if symbol in opening:
            stack.push(symbol)
        elif symbol in closing:
            if stack.is_empty() or stack.pop() != matches[symbol]:
                return False

    return stack.is_empty()

# Example usage
print(is_balanced("{[()]}"))  # Output: True
print(is_balanced("{[(])}"))  # Output: False
