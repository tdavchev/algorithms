def permute(arr, curr_string, output):
    if len(curr_string) == 3:
        print(curr_string)

    for i, s in enumerate(arr):
        curr_string.append(s)
        permute(arr[:i] + arr[(i+1):], curr_string, output)
        curr_string.pop(len(curr_string) - 1)


permute(["b", "a", "d"], [], [])

# print(blah)