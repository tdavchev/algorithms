# Given a string find all substrings that are palindromes.
def is_palindrome(input, i, j):
    while i<j:
        if input[i] != input[j]:
            return False
        i += 1
        j -= 1

    return True


def find_all_palindrome_substrings(input):
    count = 0
    for i in range(0, len(input)):
        for j in range(i + 1, len(input)):
            if is_palindrome(input, i, j):
                print(input[i:j+1])
                count += 1

    return count