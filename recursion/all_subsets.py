def find_subsets(arr, start, output):
    if len(output) < len(arr):
        for i in range(start, len(arr)):
            output.append(arr[i])
            find_subsets(arr, start+1, output)
            start += 1
            print(output)
            output.pop(len(output)-1)

find_subsets([1,2, 3, 4], 0, [])