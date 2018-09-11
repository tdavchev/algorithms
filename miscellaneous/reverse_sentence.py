# Given a sentence, reverse the order of words.
def reverse(word):
    ans = []
    for i in range(len(word), 0, -1):
        ans.append(word[i-1])

    return ans

def reverse_et(sentence):
    ans = reverse(sentence)

    start = 0
    end = 0
    reverted = []
    for i in range(len(ans)):
        if ans[i] == ' ':
            end = i
            reverted = reverted + reverse(ans[start:i])
            reverted = reverted + [' ']
            start = i + 1

    reverted = reverted + reverse(ans[start:])

    print(reverted)

reverse_et("todor is cool")