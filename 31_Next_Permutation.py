class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        first = 0
        second = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                first = i - 1
            if nums[i] > nums[first]:
                second = i
        if second == -1:
            nums.reverse()
            return
        temp = nums[first]
        nums[first] = nums[second]
        nums[second] = temp
        nums[first+1:] = nums[first+1:][::-1]
        
# 对 list in-place 逆序

