# Given a positive integer, print all
# possible sum combinations using positive integers.

def all_sum_comb(n, current_sum, start, output):
    if current_sum == target:
        print(output)

    for i in range(start, target):
        temp_sum = current_sum + i
        if temp_sum <= target:
            output.append(i)
            all_sum_comb(target, temp_sum, i, output)
            output.pop()
        else:
            return
