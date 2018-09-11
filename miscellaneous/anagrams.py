# Write a piece of code to determine
# whether two words are anagrams.
def isAnagram(word1, word2):
    if word1 == None or word2 == None:
        return False

    if len(word1) != len(word2):
        return False

    CHARS = 256
    arr = [0]*CHARS
    for i in range(len(word1)):
        arr[ord(word1[i])] += 1

    for i in range(len(word2)):
        arr[ord(word2[i])] -= 1

    for i in range(len(arr)):
        if arr[i] != 0:
            return False

    return True

print(isAnagram("aabac", "cbaaa"))
print(isAnagram("todor", "rodot"))
print(isAnagram("pieeee", "pie"))
print(isAnagram(None, "pie"))