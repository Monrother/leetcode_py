class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先按照左上-右下对称轴对称
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i < j:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
        # 在按照左右对称
        for i in range(n):
            for j in range(n // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n - 1 - j]
                matrix[i][n - 1 - j] = tmp
        