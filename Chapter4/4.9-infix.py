# 4.9 infix / prefix / postfix

# infix expressions
# operators are placed between operands such as A + B

# characteristics
# require parenthesis to dictate order of operations
# precedence & associativity rules apply

a = 3
b = 4
result = a + b * 2  # 11

# prefix expressions
# operators precede their operands
# A + B would be +AB

# characteristics
# no need for parenthesis
# evaluated right to left


def evaluate_prefix(expression):
    stack = []
    operators = set(["+", "-", "*", "/"])

    # Reverse the expression for evaluation
    for token in reversed(expression.split()):
        if token not in operators:
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)

    return stack[0]


# Example usage
prefix_expr = "+ 3 * 4 2"
# print(prefix_expr.split())
result = evaluate_prefix(prefix_expr)
print(result)  # Output: 11

# postfix

def evaluate_postfix(expression):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    
    return stack[0]

# Example usage
postfix_expr = "3 4 2 * +"
result = evaluate_postfix(postfix_expr)
print(result)  # Output: 11

