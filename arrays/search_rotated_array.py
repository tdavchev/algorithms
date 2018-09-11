def binary_search(arr, st, end, key):

  # assuming all the keys are unique.
  
  if st > end:
    return -1

  mid = st + (end-st)/2

  if arr[mid] == key:
    return mid

  if (arr[st] < arr[mid] and
        key < arr[mid] and
        key >= arr[st]):
    return binary_search(arr, st, mid-1, key)
  elif (arr[mid] < arr[end] and 
           key > arr[mid] and
           key <= arr[end]):
    return binary_search(arr, mid+1, end, key)
  elif arr[st] > arr[mid]:
    return binary_search(arr, st, mid-1, key)
  elif arr[end] < arr[mid]:
    return binary_search(arr, mid+1, end, key)

  return -1

def binary_search_rotated2(arr, key):
  return binary_search(arr, 0, len(arr)-1, key)

arr = [6,7,8,1,2,3,4,5]

ans = binary_search_rotated(arr, 6)

print(ans)