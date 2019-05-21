class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 优化一些可以用位来表示，只占用 1 / 3 的空间。
        rows = [[False for i in range(9)] for i in range(9)]
        cols = [[False for i in range(9)] for i in range(9)]
        cells = [[False for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    if rows[i][num - 1] == False and cols[j][num - 1] == False and cells[i // 3 * 3 + j // 3][num - 1] == False:
                        rows[i][num - 1] = True
                        cols[j][num - 1] = True
                        cells[i // 3 * 3 + j // 3][num - 1] = True
                    else:
                        return False
        return True
                    
        