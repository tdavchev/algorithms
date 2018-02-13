import numpy as np

a = np.zeros((2,2))

def possible_solutions(arr, start, end):
    if start[0] >= arr.shape[0] or start[0] < 0 or start[1] < 0 or start[1] >= arr.shape[1]:
        return 0

    if start[0] == end[0] and start[1] == end[1]:
        return 1

    count = 0

    count += possible_solutions(arr, [start[0]+1, start[1]], end)
    count += possible_solutions(arr, [start[0], start[1]+1], end)

    return count

ans = possible_solutions(a, [0,0], [1,1])
print(ans)
