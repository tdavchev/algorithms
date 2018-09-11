class Solution(object):
    # implement ordinary binary search first ..
    def search_rotated_array(self, arr, num):
        # f([176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162], 176)
        start = 0 
        end = len(arr) - 1

        if len(arr) == 0:
            return -1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == num:
                return mid

            if arr[mid] >= arr[start]:
                if arr[mid] < num:
                    start = mid + 1
                else:
                    if arr[start] <= num:
                        end = mid - 1
                    elif arr[start] >= num:
                        start = mid + 1
            elif arr[mid] <= arr[start]:
                if arr[mid] < num:
                    if arr[start] <= num:
                        end = mid - 1
                    elif arr[start] >= num:
                        start = mid + 1
                elif arr[mid] > num:
                    end = mid - 1

        return -1

    def binary_search_rotated(self, arr, num):
        start = 0 
        end = len(arr) - 1

        if len(arr) == 0:
            return -1

        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == num:
                return mid

            if arr[mid] >= arr[start] and arr[mid] > num and arr[start] <= num:
                end = mid - 1
            elif arr[mid] <= arr[end] and arr[mid] < num and arr[end] >= num:
                start = mid + 1
            elif arr[mid] < arr[start]:
                end = mid - 1
            elif arr[mid] > arr[end]:
                start = mid + 1
            elif arr[mid] <= arr[end] and arr[mid] < num and arr[end] < num:
                start = mid + 1
            elif arr[mid] >= arr[start] and arr[mid] > num and arr[start] > num:
                end = mid - 1

        return -1

solution = Solution()
f = solution.search_rotated_array
# f = solution.binary_search_rotated

assert f([1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162, 176, 188, 199, 200, 210, 222], 176) == 14
assert f([1, 2, 3], 2) == 1
assert f([1, 2, 3], 3) == 2
assert f([1, 2, 3], 1) == 0
assert f([], 2) == -1
assert f([3,4,1,2], 4) == 1
assert f([3,4,1,2], 3) == 0
assert f([5,6,7,8,1,2,3,4], 6) == 1
assert f([4,5,6,7,8,1,2,3], 6) == 2
assert f([176, 188, 199, 200, 210, 222, 1, 10, 20, 47, 59, 63, 75, 88, 99, 107, 120, 133, 155, 162], 176) == 0
assert f([1, 2, 3, 4], 5) == -1
assert f([], 5) == -1
assert f([1, 1, 1], 1) == 1
