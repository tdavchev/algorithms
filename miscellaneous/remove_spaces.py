# Given a null terminated string, remove any
# white spaces (tabs or spaces).

def remove_spaces(sentence):
    if len(sentence) < 1:
        return

    read = 0
    write = 0
    ans = ''
    while read < len(sentence):
        if sentence[read] == ' ':
            read += 1
        else:
            ans += sentence[read]
            read += 1 

    print(ans)

remove_spaces("todor davchev")
