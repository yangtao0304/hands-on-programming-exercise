# 最长回文子串

'''
方法一： 最长公共子串
需要注意 S 与反转后的 S'，使用最长公共子串得到的结果并不一定是最长的回文子串
例如：S=“abacdfgdcaba”, S' = “abacdgfdcaba”，S S'之间的最长公共子串为 “abacd”
显然，这不是回文

'''


class Solution:
    # 暴力匹配
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(size-1):
            for j in range(i+1, size):
                if j-i+1 > max_len and self.valid(i, j, s):
                    max_len = j-i+1
                    res = s[i:j+1]
        return res

    def valid(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    # 中心扩展法
    def longestPalindrome1(self, s: str) -> str:
        res = ''
        max_len = 0

        for i in range(len(s)):
            l1, s1 = self.expand(i, i, s)
            l2, s2 = self.expand(i, i+1, s)
            tmp = s1 if l1 >= l2 else s2
            if len(tmp) > max_len:
                max_len = len(tmp)
                res = tmp
        return res

    def expand(self, start, end, s):
        left = start
        right = end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left+1, s[left+1:right]

    # dp
    # dp[i,i] = True
    # dp[i,j] = dp[i+1,j-1] and s[i]==s[j]
    def longestPalindrome2(self, s: str) -> str:
        if not s:
            return ''
        max_len = 1
        res = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        for r in range(1, len(s)):
            for l in range(r):
                if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    cur_len = r-l+1
                    if cur_len > max_len:
                        max_len = cur_len
                        res = s[l:r+1]
        import numpy as np
        print(np.array(dp))
        return res

if __name__ == "__main__":
    s = Solution()
    s.longestPalindrome2('aaaa')
