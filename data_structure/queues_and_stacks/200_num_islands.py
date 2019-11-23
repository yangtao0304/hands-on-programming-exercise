from collections import deque


class Solution(object):
    # 本题如何应用BFS？
    # 我们可以把每一个陆地点当作树根，用 BFS 搜索四周的陆地并沉没它，那么这一整块的陆地都被沉没了
    # 下次我们再遇到陆地点的时候就说明发现新大陆了
    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
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
                while len(queue) != 0:
                    x, y = queue.popleft()
                    if grid[x][y] != '0':
                        grid[x][y] = '0'
                    for dx, dy in directions:
                        x_next, y_next = x+dx, y+dy
                        if (0 <= x_next < len(grid) and 0 <= y_next < len(grid[0])
                                and grid[x_next][y_next] == '1'
                                and (x_next, y_next) not in visited):
                            queue.append((x_next, y_next))
                            visited.add((x_next, y_next))
        return num
