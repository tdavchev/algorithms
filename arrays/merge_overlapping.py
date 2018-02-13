def merge_overlapping_intervals(arr):
    ans = []
    start = arr[0][0]
    end = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i-1][1] >= arr[i][0]:
            end = arr[i][1]
        else:
            ans.append((start,end))
            start = arr[i][0]
            end = arr[i][1]

    ans.append((start, end))
    return ans

a = [(1,5), (3, 7), (4, 6), (6, 8), (10, 12), (11, 15)]
ans = merge_overlapping_intervals(a)
print(ans)
            