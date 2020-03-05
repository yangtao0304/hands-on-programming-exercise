class Solution:
    # dp
    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        dp = [0]*(n+1)
        dp[0] = 1

        for i in range(1, n+1):
            dp[i] += dp[i-1]
            if i > 1:
                if 10 <= int(num[i-2])*10+int(num[i-1]) <= 25:
                    dp[i] += dp[i-2]
        return dp[-1]
