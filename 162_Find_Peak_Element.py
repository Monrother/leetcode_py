class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        l = 1
        r = len(nums) - 2
        while (True):
            m = (l + r) / 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            if nums[m] > nums[m - 1]:
                l = m + 1
            else:
                r = m - 1
