def binary_search(array, elem):
    start = 0
    end = len(array)
    while start <= end:
        pt = int((end - start)/2)
        if array[start+pt] == elem:
            print(start+pt)
            return pt
        elif array[start+pt] < elem:
            start = start+pt
        else:
            end = pt
    print("-1")
    return -1

arr = [1,
10,
20,
47,
59,
63,
75,
88,
99,
107,
120,
133,
155,
162,
176,
188,
199,
200,
210,
222]

# binary_search(arr, 222)


def binary_search_atmpt2(array, elem):
    start = 0
    end = len(array)

    while start < (end-1):
        mid = start + int((end-start)/2)
        if array[mid] == elem:
            return mid
        elif array[mid] < elem:
            start = mid
        else:
            end = mid

    return -1

ans = binary_search_atmpt2(arr, 223)
print(ans)