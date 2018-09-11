# Given a sorted array of integers, return the index of the given key.
# Return -1 if not found. Hint: I don't want to consider the med anymore..
def binary_search(arr, elem):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + ((end - start)//2)
        if arr[mid] == elem:
            return mid

        if arr[mid] < elem:
            start = mid + 1
        elif arr[mid] > elem:
            end = mid - 1

    return -1

print(binary_search([1,2,3], 2))
print(binary_search([1,2,3], 1))
print(binary_search([1,2,3], 3))
print(binary_search([1,2,3], 23))