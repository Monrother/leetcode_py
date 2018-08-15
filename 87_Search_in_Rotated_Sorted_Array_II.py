class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        def binarySearch(nums, target, l, r):
            while(l <= r):
                m = (l + r) / 2
                if nums[m] == target:
                    return True
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False

        if len(nums) == 0:
            return False
        if nums[0] < nums[-1]:
            return binarySearch(nums, target, 0, len(nums) - 1)
        l = 1
        r = len(nums) - 1
        index = 0
        
                
        if target == nums[index]:
            return True
        if target > nums[index]:
            return binarySearch(nums, target, index + 1, len(nums) - 1)
        else:
            return binarySearch(nums, target, 0, index - 1)
        
