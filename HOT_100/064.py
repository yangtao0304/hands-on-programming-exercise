'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        col_sum = 0
        for i in range(m):
            col_sum += grid[i][0]
            dp[i][0] = col_sum

        row_sum = 0
        for i in range(n):
            row_sum += grid[0][i]
            dp[0][i] = row_sum

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]

    # dp,直接在grid上修改
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[-1][-1]
