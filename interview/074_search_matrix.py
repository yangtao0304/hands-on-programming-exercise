class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        if col == 0:
            return False

        cur_row = -1
        for i in range(row):
            if matrix[i][col-1] >= target:
                cur_row = i
                break

        if cur_row == -1:
            return False

        for j in range(col):
            if matrix[cur_row][j] == target:
                return True

        return False
