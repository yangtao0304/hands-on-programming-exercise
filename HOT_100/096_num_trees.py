'''给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？'''


class Solution:
    # dp
    '''
    G(n)=f(1)+f(2)+f(3)+f(4)+...+f(n)
    f(i)=G(i−1)∗G(n−i)
    Final: G(n)=G(0)∗G(n−1)+G(1)∗(n−2)+...+G(n−1)∗G(0)
    '''

    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-1-j]

        return dp[-1]
