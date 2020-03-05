class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, n):
            if n == len(word)-1:
                return board[r][c] == word[-1]

            if board[r][c] == word[n]:
                visited[r][c] = True
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and dfs(nr, nc, n+1):
                        return True
                visited[r][c] = False

            return False

        R, C = len(board), len(board[0])
        visited = [[False]*C for i in range(R)]
        for r in range(R):
            for c in range(C):
                if dfs(r, c, 0):
                    return True
        return False
