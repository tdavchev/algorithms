# Given a large array of integers and a window of size 'w',
# find the current maximum in the window as the window slides through the entire array.
def find_sliding(arr, window_size):
    if window_size > len(arr):
        return

    window = []
    for i in range(window_size):
        while window and arr[i] > arr[window[-1]]:
            window.pop()

        window.append(i)

    # current max:
    print(arr[window[0]])
    for i in range(window_size, len(arr)):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()

        if window and (window[0] <= i - window_size):
            window.pop(0)

        window.append(i)
        print(arr[window[0]])


find_sliding([-4, 2, -5, 1, -1, 6], 3)