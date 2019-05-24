## 解法一：参考自 Leetcode sample
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
        
    def dfs(self, candidates, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], result)