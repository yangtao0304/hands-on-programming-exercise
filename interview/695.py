from typing import List
import numpy as np


class Solution:
    # dfs recrusive
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= R or j >= C or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            ans = 1
            for dx, dy in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                ans += dfs(i+dx, j+dy)
            return ans

        for i in range(R):
            for j in range(C):
                ans = max(dfs(i, j), ans)

        return ans

    # dfs iterative
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])

        for i in range(R):
            for j in range(C):
                cur = 0
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    while stack:
                        tmp_x, tmp_y = stack.pop()
                        if tmp_x < 0 or tmp_y < 0 or tmp_x == R or tmp_y == C or grid[tmp_x][tmp_y] != 1:
                            continue
                        grid[tmp_x][tmp_y] = 0
                        cur += 1
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            stack.append((tmp_x+dx, tmp_y+dy))
                ans = max(ans, cur)
        return ans

    # bfs iterative

    def maxAreaOfIsland3(self, grid: List[List[int]]) -> int:
        ans = 0
        R, C = len(grid), len(grid[0])

        for i in range(R):
            for j in range(C):
                cur = 0
                if grid[i][j] == 1:
                    stack = [(i, j)]
                    while stack:
                        tmp_x, tmp_y = stack.pop(0)
                        if tmp_x < 0 or tmp_y < 0 or tmp_x == R or tmp_y == C or grid[tmp_x][tmp_y] != 1:
                            continue
                        grid[tmp_x][tmp_y] = 0
                        cur += 1
                        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                            stack.append((tmp_x+dx, tmp_y+dy))
                ans = max(ans, cur)
        return ans


s = Solution()
print(s.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                         [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))
