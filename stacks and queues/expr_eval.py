def is_operator(ch):
    return ch in ['+', '-', '*', '/']

def is_priority(ch):
    return ch in ['*', '/']

def to_float(ch):
    return float(ch)

def string_to_float(n, string):
    i = 0
    while i < n:
        i += 1

    ans = ""
    if i+1 < len(string) and string[i+1] =='.':
        while i < len(string) and not is_operator(string[i]):
            ans += string[i]
            i += 1
    elif i < len(string):
        ans = string[i]

    return i, to_float(ans)

def evaluate_expression(expr):
    operators = []
    operands = []
    ans = 0
    i = 0
    while i < len(expr):
        if is_operator(expr[i]):
            operators.append(expr[i])
            i += 1
        else:
            i, d = string_to_float(i,expr)
            i += 1
            if len(operators) > 0 and is_priority(operators[-1]):
                try:
                    op = operators.pop()
                    ans = operands.pop() * d if op == '*' else operands.pop() / d
                    operands.append(ans)
                except Exception as e:
                    print("Cannot evaluate priority expression ", e)
            else:
                operands.append(d)

    while len(operands) > 1:
        a = operands.pop()
        b = operands.pop()
        if operators.pop() == '+':
            ans = a + b
            operands.append(ans)
        else:
            ans = b - a
            operands.append(ans)

    return operands

ans = evaluate_expression("3+6*5-1/2.5")
print(ans)


