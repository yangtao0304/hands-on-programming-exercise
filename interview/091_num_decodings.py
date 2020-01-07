class Solution:
    # 递归
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        def helper(n):
            if n <= 0:
                return 1
            cur = s[n]
            pre = s[n-1]

            sum = 0
            if cur != '0':
                sum = helper(n-1)
            if pre == '1' or (pre == '2' and int(cur) <= 6):
                sum += helper(n-2)

            return sum

        return helper(len(s)-1)

    # dp
    def numDecodings2(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0]*(len(s)+1)
        dp[0] = dp[1] = 1
        pre = s[0]
        for i in range(1, len(s)):
            if s[i] > '0':
                dp[i+1] = dp[i]
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                dp[i+1] += dp[i-1]
        print(dp)
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings2('226'))
