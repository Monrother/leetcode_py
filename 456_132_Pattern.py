class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if length <= 2:
            return False
        right_min = [0 for _ in range(length)]
        stack = [nums[-1]]
        for i in range(length - 2, 0, -1):
            temp = float('inf')
            while stack and nums[i] > stack[-1]:
                temp = stack[-1]
                stack.pop()
            right_min[i] = temp
            stack.append(nums[i])
        left_min = nums[0]
        for i in range(1, length - 1):
            if left_min < right_min[i] and right_min[i] < nums[i]:
                return True
            left_min = min(left_min, nums[i])
        return False
