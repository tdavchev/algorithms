def recursive_call(start, count, target, output, arr):
    if target == count:
        print(output)

    for i in range(start, len(arr)):
        # print(start, len(arr))
        # print(arr[i])
        temp_count = count + arr[i]
        # print("temp count", temp_count)
        if count >= target:
            return
        else:
            start = i
            if arr[i] <= 9:
                output.append(arr[i])
                # print("output",output)
                recursive_call(start, temp_count, target, output, arr[:i]+arr[(i+1):])
                # print("-----------")
                output.pop(len(output)-1)
                # print(output)
                # print("########")

arr = [3, 34, 4, 12, 5, 2]
recursive_call(0, 0, 9, [], arr)


