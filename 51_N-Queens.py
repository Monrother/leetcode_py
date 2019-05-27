class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [False] * n
        left_diag = [False] * (2 * n - 1)
        right_diag = [False] * (2 * n - 1)
        path = []
        res = []
        ret = []
        self.dfs(0, path, res, cols, left_diag, right_diag, n)
        for tmp in res:
            matrix = []
            for i in range(n):
                matrix.append("." * tmp[i] + "Q" + "." * (n - 1 - tmp[i]))
            ret.append(matrix)
        return ret
        
    def dfs(self, k, path, res, cols, left_diag, right_diag, n):
        if k == n:
            res.append(path)
            return
        for i in range(n):
            b1 = cols[i]
            b2 = left_diag[n - 1 - k + i]
            b3 = right_diag[k + i]
            if not (b1 or b2 or b3):       # 可以放置棋子
                cols[i] = True
                left_diag[n - 1 - k + i] = True
                right_diag[k + i] = True
                self.dfs(k + 1, path + [i], res, cols, left_diag, right_diag, n)
                cols[i] = False
                left_diag[n - 1 - k + i] = False
                right_diag[k + i] = False
                