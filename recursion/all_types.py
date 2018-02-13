def all_the_ways(target, count, start, output, arr):
    if count == target:
        print(output)

    if count < target:
        for i in range(start, len(arr)):
                temp_count = count + arr[i]
                output.append(arr[i])
                all_the_ways(target, temp_count, start, output, arr)
                output.pop(len(output) - 1)
                start += 1
    else:
        return


all_the_ways(25, 0, 0, [], [25,10,5,1])