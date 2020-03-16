class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def valid(s):
            left = 0
            right = len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s)+1):
                if valid(s[:i]):
                    helper(s[i:], tmp+[s[:i]])
        helper(s, [])
        return res

    def partition2(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        res = []

        def helper(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    helper(j+1, tmp+[s[i:j+1]])
        helper(0, [])
        return res
