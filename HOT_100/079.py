'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
'''


class Solution:
    # 回溯
    # 涉及 DFS，状态重置

    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        # 状态
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self._is_valid(board, word, 0, i, j, visited, m, n):
                    return True
        return False

    def _is_valid(self, board, word, index, x, y, visited, m, n):
        # 递归终止条件
        if index == len(word)-1:
            return board[x][y] == word[index]

        # 判断
        if board[x][y] == word[index]:
            visited[x][y] = True
            for direction in self.directions:
                next_x = x+direction[0]
                next_y = y+direction[1]
                if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y] and self._is_valid(board, word, index+1, next_x, next_y, visited, m, n):
                    return True
            # 剪枝
            visited[x][y] = False
        return False


    # 复习 重新撸了一遍～
    def exist2(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = [[False]*C for _ in range(R)]

        def neighbors(x, y):
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < R and 0 <= ny < C:
                    yield nx, ny

        def find(i, x, y, visited):
            if i == len(word)-1:
                return word[i] == board[x][y]
            if board[x][y] == word[i]:
                visited[x][y] = True
                for nx, ny in neighbors(x, y):
                    if not visited[nx][ny] and find(i+1, nx, ny, visited):
                        return True
                visited[x][y] = False
            return False

        for i in range(R):
            for j in range(C):
                if find(0, i, j, visited):
                    return True
        return False
