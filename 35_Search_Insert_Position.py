class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif nums[m] > target and (m == 0 or nums[m - 1] < target):
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
