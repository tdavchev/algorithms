
# -4 , 2, -5, 3, 6
def maximum_sliding_window(array, w):
    start = 0
    hip = []
    while start+w <= len(array):
        curr_big = -99999
        for i in range(start, start + w):
            if curr_big < array[i]:
                curr_big = array[i]

        hip.append(curr_big)
        start += 1

    return hip

def fast_maximum_sliding_window(arr, window_size):
    if window_size > len(arr):
        return

    window = deque()

    for i in xrange(0, window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)
    
    print arr[window[0]]
    for i in xrange(window_size, len(arr)):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        if window and (window[0] <= i - window_size):
            window.popleft()

        window.append(i)
        print(arr[window[0]])


arr = [-4 , 2, -5, 3, 6]
result = maximum_sliding_window(arr, 3)
print(result)

