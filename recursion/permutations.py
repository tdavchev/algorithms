def permutations(arr, output, n):
    if len(output) == n:
        print(output)

    if len(output) < n:
        for i in range(len(arr)):
            if arr[i] not in output:
                output.append(arr[i])
                permutations(arr[:i] + arr[i+1:], output, n)
                output.pop(len(output)-1)
    else:
        return

permutations(["a", "b", "c"], [], 3)