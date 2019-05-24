class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        valid = [False] * len(nums)
        self.dfs([], res, valid, nums)
        return res
    
    def dfs(self, path, res, valid, nums):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            if valid[i] == False:
                valid[i] = True
                self.dfs(path + [nums[i]], res, valid, nums)
                valid[i] = False
