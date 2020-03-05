class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)
        if R == 0:
            return False

        C = len(matrix[0])
        r, c = 0, C-1
        while 0 <= r < R and 0 <= c < C:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True

        return False
