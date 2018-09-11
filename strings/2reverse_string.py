# Given a sentence, reverse the order of words
def reverse_word(word):
    if not isinstance(word, str):
        return word

    if len(word) < 1:
        return word

    ans = ''
    for i in range(len(word) -1 , -1, -1):
        ans = ans + word[i]

    return ans

def reverse_sentence(sentence):
    if not isinstance(sentence, str):
        return sentence

    if len(sentence) < 1:
        return sentence

    reverse_sentence = reverse_word(sentence)
    temp_ans = ''
    ans = ''
    for i in range(len(reverse_sentence)):
        if reverse_sentence[i] == ' ':
            ans = ans + reverse_word(temp_ans)
            ans = ans + reverse_sentence[i]
            temp_ans = ''
        else:
            temp_ans = temp_ans + reverse_sentence[i]

    ans = ans + reverse_word(temp_ans)
    return ans

