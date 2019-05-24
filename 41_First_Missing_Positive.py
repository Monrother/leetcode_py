class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # 不在其位，进行调整
            if nums[i] != i + 1:
                cur = nums[i]
                while cur >= 1 and cur <= len(nums) and nums[cur - 1] != cur: # 注意设置条件
                    # 将 tmp 交换到对应的位置上
                    tmp = nums[cur - 1]           # 要覆盖的数先存起来
                    nums[cur - 1] = cur     # 归位
                    cur = tmp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
