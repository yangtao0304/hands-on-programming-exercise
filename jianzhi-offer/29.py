class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R = len(matrix)
        if R == 0:
            return []
        C = len(matrix[0])

        res = []
        top = 0
        down = R-1
        left = 0
        right = C-1
        while top <= down and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top+1, down+1):
                res.append(matrix[i][right])
            if top < down:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[down][i])
            if left < right:
                for i in range(down-1, top, -1):
                    res.append(matrix[i][left])
            top += 1
            down -= 1
            left += 1
            right -= 1
        return res
