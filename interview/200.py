from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        visited = set()
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        num = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 发现新大陆
                if grid[i][j] == '1':
                    queue.append((i, j))
                    visited.add((i, j))
                    num += 1

                # 旧大陆的消融
                while queue:
                    x, y = queue.popleft()
                    grid[x][y] = '0'
                    for dx, dy in directions:
                        x_next, y_next = x+dx, y+dy
                        if (0 <= x_next < len(grid) and 0 <= y_next < len(grid[0])
                                and grid[x_next][y_next] == '1'
                                and (x_next, y_next) not in visited):
                            queue.append((x_next, y_next))
                            visited.add((x_next, y_next))
        return num
