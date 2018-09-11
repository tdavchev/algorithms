def binary_search(arr, item):
    if len(arr) == 0:
        return -1

    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + ((end - start)//2)
        if arr[mid] < item:
            start = mid
        elif arr[mid] > item:
            end = mid
        else:
            return mid

    return -1

ans = binary_search([1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120], 47)
print(ans)


def binary_search_zagrqvka(arr, item):
    if len(arr) == 0:
        return -1

    start = 0
    end = len(arr)-1
    while start < end:
        mid = start + ((end - start)//2)

        if arr[mid] < item:
            start = mid
        elif arr[mid] > item:
            end = mid
        else:
            return mid

    return -1
