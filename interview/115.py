class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)
        dp = [[0 for _ in range(len_s+1)] for _ in range(len_t+1)]
        for i in range(len_s+1):
            dp[0][i] = 1

        for i in range(len_t):
            for j in range(len_s):
                if s[j] == t[i]:
                    dp[i+1][j+1] = dp[i][j]+dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        return dp[-1][-1]
