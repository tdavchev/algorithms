class Solution(object):
    def monotonic(self, arr):
        if len(arr) == 0:
            return False

        if len(arr) == 1:
            return True

        _idx1 = 0
        _idx2 = 1
        starting_idx = 0
        while arr[starting_idx+_idx1] == arr[starting_idx+_idx2]:
            starting_idx += 1
            if len(arr) <= starting_idx+1:
                return True

        if arr[starting_idx+_idx1] > arr[starting_idx+_idx2]:
            _idx1 = 1
            _idx2 = 0

        for idx in range(starting_idx+1, len(arr)-1):
            if arr[idx+_idx1] > arr[idx+_idx2]:
                return False

        return True

solution = Solution()
f = solution.monotonic

assert f([1,2,3,4]) == True
assert f([4,3,2,1]) == True
assert f([1,1,2,3]) == True
assert f([-2,0,2]) == True
assert f([1,1,0]) == True
assert f([1,1,2,2]) == True
assert f([1,1,1,1]) == True
assert f([1,3,2,2]) == False
assert f([2,2,2,1,4,5]) == False
assert f([]) == False
assert f([1]) == True
assert f([1,2,3,1]) == False