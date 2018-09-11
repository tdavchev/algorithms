def permute_string(arr, ans):
    if len(arr) < 1:
        print(ans + arr)
        return

    for i in range(len(arr)):
        ans.append(arr[i])
        permute_string(arr[:i]+arr[i+1:], ans)
        ans.pop()

permute_string(['b', 'a', 'd'], [])