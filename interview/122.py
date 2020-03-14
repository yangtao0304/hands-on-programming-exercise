class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        res = 0
        for i in range(1, n):
            res += max(0, prices[i]-prices[i-1])
        return res

    # dp
    # dp[i][0] 表示第i天，未持有股票的最大利润
    # 初始： dp[0][0]=0
    # dp[i][1] 表示第i天，持有股票的最大利润
    # 初始：dp[0][1]=-prices[0]
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0]*2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]
