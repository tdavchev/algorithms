class Solution(object):
    def smallest_common(self, arr1, arr2, arr3):
        idx1, idx2, idx3 = 0, 0, 0
        while idx1 < len(arr1) and idx2 < len(arr2) and idx3 < len(arr3):
            if arr1[idx1] == arr2[idx2] and arr2[idx2] == arr3[idx3]:
                return arr1[idx1]

            if arr1[idx1] >= arr2[idx2] and arr1[idx1] >= arr3[idx3]:
                curr = arr1[idx1]
                if arr1[idx1] > arr2[idx2]:
                    idx2 += 1
                if arr1[idx1] > arr3[idx3]:
                    idx3 += 1
            elif arr2[idx2] >= arr1[idx1] and arr2[idx2] >= arr3[idx3]:
                curr = arr2[idx2]
                if arr2[idx2] > arr1[idx1]:
                    idx1 += 1
                if arr2[idx2] > arr3[idx3]:
                    idx3 += 1
            elif arr3[idx3] >= arr1[idx1] and arr3[idx3] >= arr2[idx2]:
                curr = arr3[idx3]
                if arr3[idx3] > arr1[idx1]:
                    idx1 += 1
                if arr3[idx3] > arr2[idx2]:
                    idx2 += 1

        return None


solution = Solution()
f = solution.smallest_common

assert f([1,2,3], [3, 4, 5, 6], [2, 3, 4]) == 3
assert f([], [1], [1]) == None
assert f([1], [1], [2]) == None
assert f([6, 7, 10, 25, 30, 63, 64], [-1, 4, 5, 6, 7 , 8, 50], [1, 6, 10, 14]) == 6