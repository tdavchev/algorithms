# Given a string find all substrings that are palindromes.
def is_palindrome(string):
    if len(string) < 2:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

def find_all_palindromes(string):
    if not isinstance(string, str):
        return string

    if len(string) < 2:
        return string

    ans = []
    for i in range(len(string)-1):
        for y in range(i+1, len(string)):
            if is_palindrome(string[i:y+1]):
                ans.append(string[i:y+1])

    return ans

def find_all_plaindromes_faster(string, j, k):
    while j >= 0 and k < len(string):
        if string[j] != string[k]:
            break

        print(string[j:k+1])
        j -= 1
        k += 1

def find_all_plaindromes_fast(string):
     for i in range(len(string)):
         # account for odd and evens
         find_all_plaindromes_faster(string, i-1, i+1)
         find_all_plaindromes_faster(string, i, i+1)