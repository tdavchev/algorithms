# Given an integer array, move all elements containing '0' to the left
# while maintaining the order of other elements in the array.
def move_zeros_to_left(arr):
    if type(arr) != list:
        return

    if arr == None or len(arr) == 0:
        return

    reader = len(arr) - 1
    writer = len(arr) - 1
    while reader >= 0:
        if arr[reader] != 0:
            arr[writer] = arr[reader]
            reader -= 1
            writer -= 1
        else:
            reader -= 1

    while writer >= 0:
        arr[writer] = 0
        writer -= 1

    print(arr)
    return arr

move_zeros_to_left([1,0,3,4])
move_zeros_to_left([1, 10, 20, 0, 59, 63, 0, 88, 0])