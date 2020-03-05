class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def get_sum(a, b):
            res = 0
            while a:
                res += a % 10
                a //= 10
            while b:
                res += b % 10
                b //= 10
            return res

        def dfs(i, j):
            visited.add((i, j))
            nonlocal count
            count += 1

            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nx = i+dx
                ny = j+dy
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and get_sum(nx, ny) <= k:
                    dfs(nx, ny)
        count = 0
        visited = set()
        dfs(0, 0)
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.movingCount(1, 2, 1))
