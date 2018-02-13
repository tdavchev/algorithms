def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    if nums[n] != -1:
        return nums[n]
    else:
        nums[n] = fib(n-1) + f(n-2)

    return nums[n]

def fib_iter(n):
    if n == 0 or n == 1:
        return n

    first = 1
    second = 0
    res = 0

    i = 2
    while i <= n:
        res = first + second
        first = second
        second = res

        i += 1

    return res