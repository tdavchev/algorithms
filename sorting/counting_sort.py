def radixSort(a, n, maxLen):
    for x in range(maxLen): #maxlen e kolko cifri ima 10000 ima 5
        bins [[] for i in range(n)] # n e koi base -- 10 for example
        for y in a:
            bins[(y//n**x)%n].append(y)

        a = []
        for section in bins:
            a.extend(section)

    return a
