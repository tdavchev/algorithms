def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

def find_kth_permutation(v, k, result):
    if not v:
        return

    n = len(v)
    count = factorial(n-1)
    selected = (k-1) // count
    result += str(v[selected])
    v.pop(selected)
    