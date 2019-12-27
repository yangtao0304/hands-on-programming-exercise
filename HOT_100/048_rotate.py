'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
'''

# 给定 matrix =
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
from typing import List


class Solution:
    # 先转置，然后翻转每一行
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(1, n):
            for i in range(j):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in range(n):
            left = 0
            right = n-1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))


if __name__ == "__main__":
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix)
    print(matrix)
