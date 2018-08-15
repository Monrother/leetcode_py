class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l + r) / 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                l = m
                break
            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
        if l > r:
            return False
        row = l
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            m = (l+r) / 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

