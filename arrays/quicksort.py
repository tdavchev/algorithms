def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

a = [55, 23, 26, 2, 18, 78, 23, 8, 2, 3]
ans = quick_sort(a)
print(ans)