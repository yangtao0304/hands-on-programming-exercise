# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。


class Solution:
    # 暴力, O(n^2) 会超时
    def longestValidParentheses(self, s: str) -> int:
        def is_valid(s):
            bal = 0
            for i in s:
                if i == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        max_len = 0
        size = len(s)
        for i in range(size-1):
            for j in range(i+2, size+1, 2):
                if j-i > max_len and is_valid(s[i:j]):
                    max_len = j-i

        return max_len

    # dp
    # if s[i]==')' and s[i-1]=='(':
    # dp[i] = dp[i-2] + 2
    # if s[i] == s[i-1] == ')' and s[i-dp[i-1]-1]=='(':
    # dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
    def longestValidParentheses2(self, s: str) -> int:
        max_len = 0
        dp = [0 for _ in range(len(s)+1)]
        for i in range(2, len(s)+1):
            if s[i-1] == ')' and s[i-2] == '(':
                dp[i] = dp[i-2]+2
            elif s[i-1] == s[i-2] == ')' and i-1-dp[i-1]-1 >= 0 and s[i-1-dp[i-1]-1] == '(':
                dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
            max_len = max(max_len, dp[i])

        import numpy as np
        print(np.array(dp))
        return max_len

    def longestValidParentheses2_revised(self, s: str) -> int:
        max_len = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i-2 >= 0 else 0) + 2
                elif s[i-1] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0)
                max_len = max(max_len, dp[i])

        import numpy as np
        print(np.array(dp))
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses2_revised("(()))())("))
