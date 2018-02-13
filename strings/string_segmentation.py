def segment(string, dictionary):
    count = 0
    word = ""
    while count < len(string):
        word += string[count]
        if word in dictionary.keys():
            print(word)
            word = ""
        
        count += 1

def segment_recursive(string, dictionary, word, output):
    if word in dictionary.keys():
        output.append(word)
        word = ""

    if len(string) > 0:
        word += string[0]
        output = segment_recursive(string[1:], dictionary, word, output)

    return output
    

dicto = {}
dicto["hello"] = 1
dicto["hell"] = 1
dicto["on"] = 1
dicto["now"] = 1
ans = segment_recursive("hellonow", dicto, "", [])
print(ans)