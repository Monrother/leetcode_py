class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        num_dict = dict()
        # count the times of each number in nums
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        nums_ele = list(num_dict.keys())
        self.dfs([], res, num_dict, nums_ele, len(nums))
        return res
        
    def dfs(self, path, res, num_dict, nums, n):
        if len(path) == n:
            res.append(path)
            return
        for num in nums:
            if num_dict[num] != 0:
                num_dict[num] -= 1
                self.dfs(path + [num], res, num_dict, nums, n)
                num_dict[num] += 1