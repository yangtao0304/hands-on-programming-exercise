class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k == 0 or n < 2:
            return 0
        if k >= n//2:
            res = 0
            for i in range(1, n):
                tmp = prices[i]-prices[i-1]
                if tmp > 0:
                    res += tmp
            return res

        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(k+1):
                if i == 0 or j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = float('-inf')
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i-1])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i-1])
        return dp[-1][-1][0]
