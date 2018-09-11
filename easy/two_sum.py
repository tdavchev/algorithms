class Solution(object):
    def binary_search(self, arr, targ):
        if len(arr) == 0:
            return - 1

        start = 0
        end = len(arr) - 1
        result = -1
        while start <= end:
            mid = start + (end - start) // 2
            if targ > arr[mid]:
                start = mid + 1
            elif targ < arr[mid]:
                end = mid - 1
            if targ == arr[mid]:
                result = mid
                break

        return result

    def task_with_sorted(self, arr, tar):
        arr.sort()
        idx_1, idx_2 = -1, -1
        for idx in range(len(arr)):
            curr = arr[idx]
            left = tar - curr
            temp = self.binary_search(arr[idx+1:], left)
            if temp != -1:
                idx_1 = idx
                idx_2 = temp+idx+1
                break

        return [idx_1, idx_2]

    def task_dict(self, arr, target):
        lookup = {}
        for i, v in enumerate(arr):
            if target - v in lookup:
                return [lookup[target-v], i]

            lookup[v] = i


solution = Solution()

f = solution.task_dict
s = solution.binary_search
assert s([], 3) == -1
assert s([1,2,3], 1) == 0
assert s([1,2,3], 2) == 1
assert s([1,2,3], 3) == 2
assert s([1,2,3], 35) == -1
assert s([0, 1,2,3, 12, 200, 5], 21) == -1
assert s([0, 1, 2, 3, 12, 200, 500], 200) == 5
assert s([0, 1, 2, 3, 12, 200, 500], 500) == 6

assert f([2, 7, 11, 15], 9) == [0, 1]
print(f([7, 2, 11, 15], 9))
assert f([2, 7, 11, 15], 9) == [0, 1]
print(f([2, 7, 11, 15], 19))
assert f([3, 3], 6) == [0, 1]
assert f([], 9) == None
assert f([2, 7, 11, 15], 19) == None
assert f([2, 7, 11, 15], 22) == [1, 3]
print("pass")