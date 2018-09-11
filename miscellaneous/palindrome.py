# Write a piece of code to determine
# whether a number is a palindrome.
def isPalindrome(sentence):
    if len(sentence) <= 1:
        return True

    if sentence[0] != sentence[-1]:
        return False

    return isPalindrome(sentence[1:-1])

print(isPalindrome("aabbaa"))
print(isPalindrome("todor"))
print(isPalindrome("nursesrun"))