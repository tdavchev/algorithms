def sum_of_twos(sorted_arr, target):
    start = 0
    end = len(sorted_arr) - 1
    ans = []
    while start < end:
        if sorted_arr[start] + sorted_arr[end] == target:
            ans.append((sorted_arr[start], sorted_arr[end]))

        if sorted_arr[start+1] + sorted_arr[end] > target:
            end = end - 1
        else:
            start = start + 1

    return ans

def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

a = [5, 7, 1, 2, 8, 4, 3]
a = quicksort(a)
ans = sum_of_twos(a, 10)
print(ans)


