class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1 or n == 2:
            return n
        f1 = 1
        f2 = 2
        for i in range(3, n+1):
            f1, f2 = f2, f1+f2
        return f2 % 1000000007
