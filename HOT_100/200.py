class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        queue = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    queue = [(i, j)]
                    visited.add((i, j))
                while queue:
                    x, y = queue.pop(0)
                    grid[x][y] = '0'
                    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nx = x+dx
                        ny = y+dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] == '1':
                            queue.append((nx, ny))
                            visited.add((nx, ny))
        return count
