def largest_sum_subarray(arr):
    if len(arr) < 1:
        return 0

    curr_max = arr[0]
    global_max = arr[0]
    lengthArr = len(arr)

    for i in range(1, lengthArr):
        if curr_max < 0:
            curr_max = A[i]
        else:
            curr_max += A[i]

        if global_max < curr_max:
            global_max = curr_max

    return global_max