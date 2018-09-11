def move_zeros_left(arr):
    reader = len(arr) - 1
    writer = len(arr) - 1

    while reader > 0:
        if arr[reader] == 0:
            reader -= 1
        else:
            reader -= 1
            writer -= 1

        arr[writer] = arr[reader]

    print(writer)
    for i in range(writer):
        arr[i] = 0

    return arr

print(move_zeros_left([1, 10, 20, 0, 59, 63, 0, 88, 0]))