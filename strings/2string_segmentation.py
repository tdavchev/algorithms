# Given a dictionary of words and an input string tell whether
# the input string can be completely segmented into dictionary words.

def segment_string(string, dictionary):
    segment = False
    start = 0
    for end in range(1,len(string)+1):
        if string[start:end] in dictionary.keys():
            segment = True
            start = end
            if start < len(string):
                segment = False

    return segment