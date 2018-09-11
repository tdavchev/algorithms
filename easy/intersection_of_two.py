import time

class Solution(object):

    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        return list(nums1.intersection(nums2))

    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))

    def intersection_proper(self, nums1, nums2):
        lookup = {}
        solution = []
        for num in nums1:
            if num not in lookup:
                lookup[num] = True

        for num in nums2:
            if num in lookup:
                lookup[num] = False

        for key, val in lookup.items():
            if val is False:
                solution.append(key)

        return solution

    def intersection_dicts_slow(self, nums1, nums2):
        lookup = dict((v, False) for v in nums1)
        lookup = dict((v, True) for v in nums2 if v in lookup.keys())

        return list(lookup.keys())

    # faster
    def intersection_conv(self, arr1, arr2):
        # the & operator takes long time!
        return list(set(arr1) & set(arr2))

    # slower
    def intersection_wtf(self, arr1, arr2):
        lookup = set(arr1)
        solution = []
        for item in lookup:
            if item in arr2:
                solution.append(item)

        return solution


solution = Solution()
f = solution.intersection

assert f([1,2,2,1], [2,2]) == [2]
assert f([4,9,5], [9,4,9,8,4]) == [9,4] or f([4,9,5], [9,4,9,8,4]) == [4,9]
assert f([5,6,7,1], [1,2,3,4]) == [1]
assert f([], [9,4,9,8,4]) == []
assert f([5,6,7,8], [1,2,3,4]) == []