def parenthesis(count):
    if count > 0:
        print("(", end='')
        parenthesis(count-1)
        print(")", end='')


parenthesis(3)
print("")