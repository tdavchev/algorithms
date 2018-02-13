def reverse_array(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

def rotate_array(arr, n):
    length_arr = len(arr)
    # normalising rotations if
    # n > arr size or n is negative
    n = n % length_arr

    if n < 0:
        n = n + length_arr

    reverse_array(arr, 0, length_arr - 1)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, n, length_arr)