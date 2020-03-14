class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        zero = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = i, j
                elif grid[i][j] == 0:
                    zero += 1

        visited = [[False]*n for _ in range(m)]
        visited[start[0]][start[1]] = True
        zero_cnt = 0
        return self.dfs(grid, start[0], start[1], m, n, visited, zero_cnt, zero)

    def dfs(self, grid, i, j, m, n, visited, zero_cnt, zero):
        total = 0
        for x, y in self.neighbors(i, j, m, n):
            if grid[x][y] == 0 and not visited[x][y]:
                visited[x][y] = True
                zero_cnt += 1
                total += self.dfs(grid, x, y, m, n, visited, zero_cnt, zero)
                visited[x][y] = False
                zero_cnt -= 1
            elif grid[x][y] == 2 and zero_cnt == zero:
                total = 1
        return total

    def neighbors(self, i, j, m, n):
        for x, y in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
            if 0 <= x < m and 0 <= y < n:
                yield x, y
