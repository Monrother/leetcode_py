class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False for i in range(9)] for j in range(9)]
        cols = [[False for i in range(9)] for j in range(9)]
        cells = [[False for i in range(9)] for j in range(9)]
        # 对几个 valid 矩阵进行初始化
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i][num - 1] = True
                    cols[j][num - 1] = True
                    cells[i // 3 * 3 + j // 3][num - 1] = True
        self.dfs(board, 0, rows, cols, cells)
        
        
    def dfs(self, board, n, rows, cols, cells):
        if n == 81:
            return True
        i = n // 9
        j = n - 9 * i
        if board[i][j] == '.':
            for num in range(9):    # 尝试填入每一个数
                if rows[i][num] == False and cols[j][num] == False and cells[i // 3 * 3 + j // 3][num] == False:
                    # num 可行，先尝试一下
                    board[i][j] = str(num + 1)
                    rows[i][num] = True
                    cols[j][num] = True
                    cells[i // 3 * 3 + j // 3][num] = True
                    if self.dfs(board, n + 1, rows, cols, cells):
                        return True
                    else:   # 恢复
                        board[i][j] = '.'
                        rows[i][num] = False
                        cols[j][num] = False
                        cells[i // 3 * 3 + j // 3][num] = False
            return False        # 没有可行的数
        else:
            return self.dfs(board, n + 1, rows, cols, cells)
