def find_smallest_common_number(arr1, arr2, arr3):
    i,j,k = 0, 0, 0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            return arr1[i]

        if arr3[k] <= arr1[i] and arr3[k] <= arr2[j]:
            k += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            i += 1
        
    return -1


a = [6,
7,
10,
25,
30,
63,
64]

b = [-1,
4,
5,
7,
8,
9,
50]

c = [1, 6, 7, 10, 14]

ans = find_smallest_common_number(a, b, c)
print(ans)