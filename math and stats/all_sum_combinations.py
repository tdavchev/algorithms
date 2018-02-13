def print_all_sum_rec(target, current_sum, start, output):
    if current_sum == target:
        print_list(output)

    for i in xrange(start, target):
        temp_sum = current_sum + i
        if temp_sum <= target:
            output.append(i)
            # print("output ", output)
            print_all_sum_rec(target, temp_sum, i, output)
            output.pop(len(output)-1)
            print(output)
        else:
            return

def print_all_sum(target):
    output = []
    print_all_sum_rec(target, 0, 1, output)

def print_list(output):
    print(output)


print_all_sum(5)