## Leetcode 33 -- Search in Rotated Sorted Array
# 基于二分法，根据 target、nums[0]、nums[m] 的关系，判断向哪个方向搜索。

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            cur = nums[m]
            if cur == target:
                return m
            if cur < target:
                if cur >= nums[0] or target < nums[0]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if cur < nums[0] or target >= nums[0]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
