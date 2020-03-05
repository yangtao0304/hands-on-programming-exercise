class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[-1][-1]
