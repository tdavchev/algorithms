def move_zeros_left(arr):
    final = []
    tmp= []
    for i in range(len(arr)):
        if arr[i] == 0:
            final.append(arr[i])
        else:
            tmp.append(arr[i])

    return final + tmp

def less_storage(arr):
    reader = len(arr) - 1
    writer = len(arr) - 1
    while writer >= 0:
        if reader < 0:
            arr[writer] = 0
            writer -= 1
        elif arr[reader] != 0:
            arr[writer] = arr[reader]
            writer -= 1
            reader -= 1
        else:
            reader -= 1
    return arr

a = [1, 10, 20, 0, 59, 63, 0, 88, 0]

ans = less_storage(a)
print(ans)