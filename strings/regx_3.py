def regx(pattern, text, i, j):
    if len(pattern) == i and len(text) == j:
        return True

    if i < len(pattern) - 1 and pattern[i+1] == "*":
        for k in range(i, len(text) + 1):
            if regx(pattern, text, i+2, k):
                return True

            if k >= len(text):
                return False

    if i < len(pattern) and j < len(text) and (
        pattern[i] == "." or pattern[i] == text[j]):
            return regx(pattern, text, i+1, j+1)

    return False

ans = regx(".a*a", "baac", 0, 0)
print(ans)