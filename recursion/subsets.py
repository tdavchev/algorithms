def all_subsets(arr, output, start):
    if len(arr) == 0 or len(arr) == 1:
        print(output)

    if len(output) == 0:
        print(output)

    for i in range(len(arr)):
        output.append(arr[i])
        all_subsets(arr[i+1:], output, start+1)
        start += 1
        output.pop(len(output) - 1)


all_subsets([1,2, 3], [], 0)
