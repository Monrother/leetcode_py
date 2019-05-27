class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        t = min(m, n) // 2             # 可以输出多少圈
        res = []
        for i in range(t):
            # 上边
            for k in range(i, m - 1 - i):
                res.append(matrix[i][k])
            # 右边
            for k in range(i, n - 1 - i):
                res.append(matrix[k][m - 1 - i])
            # 下边
            for k in range(m - 1 - i, i, -1):
                res.append(matrix[n - 1 - i][k])
            # 左边
            for k in range(n - 1 - i, i, -1):
                res.append(matrix[k][i])
        for i in range(t, n - t):
            for j in range(t, m - t):
                res.append(matrix[i][j])
        return res
        