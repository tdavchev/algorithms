def magic_index(arr, i, output):
    if i >= len(arr) or i < 0:
        return output

    if arr[i] == i:
        output.append(i)

    output = magic_index(arr, i + 1, output)
    return output


ans = magic_index([0, 1, 2, 4], 0, [])
print(ans)
