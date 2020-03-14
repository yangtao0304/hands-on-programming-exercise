class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in prices:
            if i <= min_price:
                min_price = i
            else:
                max_profit = max(max_profit, i-min_price)
        return max_profit

    # dp
    # dp[i]表示第i天的最大利润
    # dp[i] = max(dp[i-1], prices[i]-min_price)
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [0]*n
        min_price = prices[0]

        for i in range(1, n):
            min_price = min(min_price, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min_price)
        return dp[-1]
