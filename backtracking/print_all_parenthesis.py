def print_all_parenthesses_rec(n, left, right, output):
    if left >= n and right >= n:
        print(output)

    if left < n:
        output += '{'
        print_all_parenthesses_rec(n, left+1, right, output)
        output.pop()

    if right < n:
        output += '}'
        print_all_parenthesses_rec(n, left, right+1, output)
        output.pop()

def print_all_parenthesses(n):
    output = []
    print_all_parenthesses_rec(n, 0, 0, output)
