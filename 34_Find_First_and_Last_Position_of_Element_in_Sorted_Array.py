## 34 Find First and Last Position of Element in Sorted Array
# 三次二分，第一次找到任意一个等于 target 的位置 temp，如果没有找到返回 [-1, -1]。第二次从 temp 向左找，第三次从 temp 向右找。

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        temp = -1
        while l <= r:
            m = (l + r) // 2
            cur = nums[m]
            if cur == target:
                temp = m
                break
            elif cur < target:
                l = m + 1
            else:
                r = m - 1
        if temp == -1:
            return [-1, -1]
        
        left = -1
        right = -1
        
        l = 0
        r = temp
        while l <= r:
            m = (l + r) // 2
            cur = nums[m]
            if cur == target and (m == 0 or nums[m - 1] != target):
                left = m
                break
            elif cur < target:
                l = m + 1
            elif cur == target and nums[m - 1] == target:
                r = m - 1
        
        l = temp
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            cur = nums[m]
            if cur == target and (m == len(nums) - 1 or nums[m + 1] != target):
                right = m
                break
            elif cur > target:
                r = m - 1
            elif cur == target and nums[m + 1] == target:
                l = m + 1
        
        return [left, right]
        
            