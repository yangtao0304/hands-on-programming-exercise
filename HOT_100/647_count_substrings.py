class Solution:
    # 暴力 超时
    def countSubstrings(self, s: str) -> int:
        def valid(s):
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        res = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if valid(s[i:j+1]):
                    res += 1
        return res

    # 中心扩散法

    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        self.res = 0

        for i in range(n):
            self.count(s, i, i)
            self.count(s, i, i+1)
        return self.res

    def count(self, s, start, end):
        while start >= 0 and end <= len(s)-1 and s[start] == s[end]:
            self.res += 1
            start -= 1
            end += 1

    # dp

    def countSubstrings3(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res
