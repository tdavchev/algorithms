def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


def kth(arr, k, result):

    if len(arr) == 0:
        return

    n = len(arr)
    count = factorial(n-1)
    selected = (k-1)/count

    result += str(arr[selected])
    arr.pop(selected)
    k = k - (count * selected)
    kth(arr, k, result)