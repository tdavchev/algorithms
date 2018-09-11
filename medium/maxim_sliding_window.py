from collections import deque

class Solution(object):
    def find_max_sliding_window(self, arr, window_size):
        if len(arr) == 0:
            return []

        if window_size > len(arr):
            window_size = len(arr)

        window = deque()
        solution = []

        for i in range(window_size):
            while window and arr[i] >= arr[window[-1]]:
                window.pop()

            window.append(i)

        solution.append(arr[window[0]])
        for i in range(window_size, len(arr)):
            while window and arr[i] >= arr[window[-1]]:
                window.pop()

            if window and (window[0] <= i - window_size):
                window.popleft()

            window.append(i)
            solution.append(arr[window[0]])

        return solution

    def max_sliding_window(self, arr, w):
        running_max = -999
        running_idx = -1
        solution = []
        start = 0

        if len(arr) == 0:
            return []

        if w > len(arr):
            w = len(arr)

        while w <= len(arr):
            if running_idx < start:
                running_max = arr[start]
                running_idx = start

            for idx in range(start+1, w):
                if arr[idx] > running_max:
                    running_max = arr[idx]
                    running_idx = start + idx

            w += 1
            start += 1
            solution.append(running_max)

        return solution

solution = Solution()
f = solution.max_sliding_window

assert f([-4, 2, -5, 3, 6], 3) == [2, 3, 6]
assert f([2, -4, -5, 1, 6], 3) == [2, 1, 6]
assert f([2, 2, 2, 2, 2], 3) == [2, 2, 2]
assert f([-4, 2, -5, 1, -1, 6], 3) == [2, 2, 1, 6]
assert f([2, 2], 3) == [2]
assert f([2, -4, -5, 1, 6], 10) == [6]
assert f([], 10) == []
assert f([1], 1) == [1]

f = solution.find_max_sliding_window

assert f([-4, 2, -5, 3, 6], 3) == [2, 3, 6]
assert f([2, -4, -5, 1, 6], 3) == [2, 1, 6]
assert f([2, 2, 2, 2, 2], 3) == [2, 2, 2]
assert f([-4, 2, -5, 1, -1, 6], 3) == [2, 2, 1, 6]
assert f([2, 2], 3) == [2]
assert f([2, -4, -5, 1, 6], 10) == [6]
assert f([], 10) == []
assert f([1], 1) == [1]