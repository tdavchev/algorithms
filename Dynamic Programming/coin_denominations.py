def denomnom(target, start, count, output):
    if count == target:
        print(output)

    poss = [1, 2, 5]
    for i in range(start, len(poss)):
        temp_count = count + poss[i]
        if temp_count <= target:
            output.append(poss[i])
            denomnom(target, i, temp_count, output)
            output.pop(len(output) - 1)
        else:
            break

def denom_dynamic(target, result):
    # kolko 1 ima v 7 1
    # kolko 2 ima v 7 3
        # 7%2 = 1
    # kolko 5 ima v 7 1
        # 7%5 = 2 - po dva na4ina
    possib = [1, 2, 5]
    total = 0
    for i in possib:
        if i == 1:
            total += 1
        else:
            total += 7//i
            rest = 7%i
            if rest > 1:
                total += rest//2 + rest//5

    return total

denomnom(6, 0, 0, [])

n = 6
result = [0]*(n+1)
result[0] = 1
ans = denom_dynamic(2,result)
print(ans)