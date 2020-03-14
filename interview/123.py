class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0]*2 for _ in range(3)] for _ in range(n+1)]

        for i in range(n+1):
            for j in range(3):
                if i == 0 or j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = float('-inf')
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i-1])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1]
                                      [j-1][0]-prices[i-1])
        return dp[-1][-1][0]
