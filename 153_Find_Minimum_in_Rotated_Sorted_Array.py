class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if (m == len(nums) - 1 or nums[m] < nums[m+1]) and nums[m] < nums[m-1]:
                return nums[m]
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m - 1
