def prefix_calculator(expression):
    stack = []
    operators = ['+', '-', '*', '/']

    for token in reversed(expression.split()):
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            operand1 = stack.pop()
            operand2 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2

            stack.append(result)
        else:
            raise ValueError("Invalid token")

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack[0]

expression = input("Enter a prefix expression: ")
result = prefix_calculator(expression)
print("Result:", result)