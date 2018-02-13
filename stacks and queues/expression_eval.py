def is_div_or_mul(ch):
  return ch == '*' or ch == '/'

def is_operator(c):
  return c == '+' or c == '-' or c == '*' or c == '/'

def is_digit(ch):
  return ch >= '0' and ch <= '9'

def str_to_double(s, i):
  n = len(s)

  temp = []
  while i < n and (s[i] == ' ' or s[i] == '\t'):
    ++i

  if i >= n:
    return None

  if s[i] == '-':
    temp.append('-')
    ++i

  while i < n:
    ch = s[i]
    if ch != '.' and not is_digit(ch):
      break

    temp.append(ch)
    i += 1

  temp_str = "".join(temp)
  return float(temp_str), i

def evaluate2(expr):
  operators = []
  operands = []

  op = 0
  prev = 0

  i = 0
  n = len(expr)
  while i < n:
    ch = expr[i]
    if ch == ' ' or ch == '\t':
      i += 1
      continue

    if is_operator(ch):
      op = ch;
      operators.append(ch)
      i += 1
    else:
      d, i = str_to_double(expr, i)

      if is_div_or_mul(op):
        operators.pop()
        operands.pop()

        prev = (prev * d) if (op == '*') else (prev / d)
        operands.append(prev)
        op = 0
      else:
        operands.append(d)
        prev = d

  t = operands[0] if operands else 0

  i = 1
  for operator in operators:
    operand =  operands[i]
    t = t + operand if operator == '+' else t - operand
    i += 1

  return t

evaluate2("3+6*5−1/2.5")