class Solution:
    # greedy
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n-1

        i, j = n//3, n % 3
        if j == 0:
            return pow(3, i)
        if j == 1:
            return pow(3, i-1)*2*2
        if j == 2:
            return pow(3, i)*2

    # dp
    def cuttingRope2(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[i-j]*j, (i-j)*j))

        return dp[-1]
