from collections import deque

class stack_using_queue:
  def __init__(self):
    self.queue1 = deque()
    self.queue2 = deque()

  def push(self, data):
    self.queue1.append(data)

  def isEmpty(self):
    return len(self.queue1) + len(self.queue2) == 0;

  def pop(self):
    if self.isEmpty():
      raise Exception("stack is empty")

    while len(self.queue1) > 1 :
      self.queue2.append(self.queue1.popleft())

    value = self.queue1.popleft()

    self.swap_queues()

    print(value)
    return value


  def swap_queues(self): 
    self.queue3 = self.queue1
    self.queue1 = self.queue2
    self.queue2 = self.queue3

q = stack_using_queue()

q.push(3)
q.push(5)
q.push(9)
q.pop()
q.push(10)
q.push(16)
q.pop()




def is_operator(c):
      return c == '+' or c == '-' or c == '*' or c == '/'

# returns true if op1 has higher/equal precedence
# compared to op2
def preced(op1, op2):
  if op1 == '*' or op1 == '/':
    return True

  if op1 == '+' or op1 == '-':
    if op2 == '+' or op2 == '-':
      return True

  return False

def is_digit(ch):
  return ch >= '0' and ch <= '9'

def str_to_double(s, i):
  n = len(s)
  if i >= n:
    return None

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

def convert_to_postfix(expr):
  post_fix = []

  operators = []
  n = len(expr)
  i = 0
  while i < n:
    ch = expr[i]
    if ch == ' ' or ch == '\t':
      i += 1
      continue

    if is_operator(ch):
      while operators and preced(operators[-1], ch):
        post_fix.append(token(operators.pop(), True))
      operators.append(ch)
      i += 1
    else:
      d, i = str_to_double(expr, i)
      post_fix.append(token(d, False))

  while operators:
    post_fix.append(token(operators.pop(), True))

  return post_fix

def evaluate(post_fix):
  operands = []
  for x in post_fix:
    if x.is_operator:
      val2 = operands.pop()
      val1 = operands.pop()
      op = x.value

      if op == '+':
        operands.append(val1 + val2)
      elif op == '-':
        operands.append(val1 - val2)
      elif op == '*':
        operands.append(val1 * val2)
      elif op == '/':
        operands.append(val1 / val2)
    else:
      val = x.value
      operands.append(val)

  return operands.pop()

def evaluate1(expr):
  return evaluate(convert_to_postfix(expr))