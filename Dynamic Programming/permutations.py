def permut(n, start, ans, count):
    if count == n:
        print(ans)

    possib = [1,2,4]
    for i in range(len(possib)):
        temp_count = count + possib[i]
        if temp_count <= n:
            ans.append(possib[i])
            permut(n, i, ans, temp_count)
            ans.pop(len(ans)-1)
            i -= 1
        else:
            return

permut(5, 0, [], 0)

def dynamic_permut(n, result):
    if n < 0:
        return 0

    if result[n] > 0:
        return result[n]

    result[n] = dynamic_permut(n-1, result) + \
         dynamic_permut(n-2, result) + \
         dynamic_permut(n-4, result)

    return result[n]

def score(n):
    if n <= 0:
        return 0

    result = [0]*(n+1)
    result[0] = 1

    result[n] = dynamic_permut(n, result)

    return result[n]

ans = score(5)
print("#####")
print(ans)

