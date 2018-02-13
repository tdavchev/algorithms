def find_low(arr, key):
    start = 0
    end = len(arr) - 1
    low = -1
    while start <= end:
        mid = start + (end - start)//2
        if mid - 1 < 0:
            return mid

        if arr[mid] == key and arr[mid - 1] < key:
            return mid
        if arr[mid] < key:
            start = mid
        else:
            end = mid

    return low

def find_high(arr, key):
    start = 0
    end = len(arr) - 1
    high = -1
    while start <= end:
        mid = start + (end - start)//2

        if mid + 1 > end:
            return mid

        if arr[mid] == key and arr[mid + 1] > key:
            return mid
        elif arr[mid] > key:
            end = mid
        else:
            start = mid

    return high

a = [1,2,5,5,5,5,5,5,5,5,20]
lo = find_low(a, 5)
hi = find_high(a, 5)

print(lo, hi)