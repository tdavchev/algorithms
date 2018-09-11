# implement quicksort

def quicksort(arr):
    if type(arr) != list:
        return None

    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i < pivot]
    right = [i for i in arr[1:] if i >= pivot]

    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3,4,8, 100, 1, 2, 16, 12, 0]))