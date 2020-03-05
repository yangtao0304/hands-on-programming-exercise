class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1]+dp[i-2]

        return dp[-1] % 1000000007

    # space O(1)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        f1 = 0
        f2 = 1
        for i in range(2, n+1):
            f1, f2 = f2, f1+f2

        return f2 % 1000000007
