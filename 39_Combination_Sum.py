class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        self.dfs(candidates, 0, target, cur, res)
        return res
    
    def dfs(self, candidates, n, target, cur, res):
        if target == 0:
            res.append(cur[:])
            return
        elif target < 0:
            return
        for i in range(n, len(candidates)):
            cur.append(candidates[i])
            self.dfs(candidates, i, target - candidates[i], cur, res)
            cur.pop()
