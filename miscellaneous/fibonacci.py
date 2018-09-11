# Write a piece of code to create a Fibonacci
# sequence using recursion.
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

# Write a piece of code to create a Fibonacci
# sequence using iteration.
def fibonacci_iter(n):
    if n == 0 or n == 1:
        return n

    n_1 = 1
    n_2 = 0
    result = 0
    i = 1

    while i < n:
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
        i += 1

    return result

ans = fibonacci(6)
print(ans)

ans = fibonacci_iter(5)
print(ans)