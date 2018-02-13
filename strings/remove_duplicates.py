def remove_duplicates(string):
    dictionary = {}
    for c in string:
        if c not in dictionary:
            dictionary[c] = True

    return dictionary.keys()

a = remove_duplicates("abracadabra")
# print(a)


def faster(string):

    i = 1
    while True:
        if i >= len(string):
            break

        if string[i] == string[i-1]:
            string = string[:i] + string[i+1:]
            i -= 1

        i += 1

    return string

def quicksort(string):
    if len(string) < 2:
        return string

    pivot = string[0]
    less = [i for i in string[1:] if i < pivot]
    greater = [i for i in string[1:] if i >= pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)

string = "aaabracadabraab"
string = quicksort(string)
a = faster(string)
print(a)


def no_sort(str):
    write_index = 0

    for i in range(len(str)):
        found = False

        for j in xrange(0, write_index):
            if str[i] == str[j]:
                found = True
                break

        if found == False:
            str[write_index] = str[i]
            write_index += 1

    str[write_index] = '\0'