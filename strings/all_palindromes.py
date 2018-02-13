def isPalindrome(str, begin, end):
    if str[begin] != str[end]:
        return False

    if begin >= end:
        return True

    return isPalindrome(str, begin+1, end-1)

def all_substrings(string):
    word = ""
    answer = []
    for i in range(len(string)):
        word += string[i]
        for j in range(i+1, len(string)):
            word += string[j]
            palindrome = isPalindrome(word, 0, len(word)-1)
            if palindrome:
                answer.append(word)

        word = ""

    return answer

ans = all_substrings("aabbbaa")
print(ans)
