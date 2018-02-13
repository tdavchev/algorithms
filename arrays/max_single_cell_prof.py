def find_max_sell_profit(arr):
    buy = 0
    sell = len(arr) - 1
    curr_best = [arr[buy], arr[sell]]

    while buy+1 < sell:
        move_sell = arr[sell - 1] - arr[buy]
        move_buy = arr[sell] - arr[buy + 1]
        if move_sell > move_buy:
            sell -= 1
        else:
            buy += 1

        if curr_best[1] - curr_best[0] < arr[sell] - arr[buy]:
            curr_best = [arr[buy], arr[sell]]

    return curr_best

a = [8, 5, 12, 9, 19, 1]
b = [21, 12, 11, 9, 6, 3]
ans = find_max_sell_profit(b)
print(ans)
