# 多源广度优先搜索

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        R, C = len(grid), len(grid[0])

        queue = deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    # 这里的0指的是初始天数
                    queue.append((r, c, 0))

        def neighbor(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))

        if any(1 in row for row in grid):
            return -1

        return d
