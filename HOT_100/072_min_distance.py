# dp
# dp[i][j]表示word1前i个字符和word2的前j个字符的编辑距离
# 若word1[i]==word2[j]: dp[i][j]=dp[i-1][j-1]
# 若word1[i]！=word2[j]: 考虑三种情况
# 1.替换： dp[i-1][j-1]
# 2.插入：dp[i-1][j]
# 3.移除：dp[i][j-1]


class Solution:
    # 自底向上
    def minDistance2(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])+1
        return dp[-1][-1]

    # 自顶向下
    from functools import lru_cache

    @lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            insert = 1 + self.minDistance(word1, word2[1:])
            remove = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            return min(insert, remove, replace)

    def minDistance3(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i == len(word1):
                return len(word2)-j
            if j == len(word2):
                return len(word1)-i
            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            else:
                insert = 1 + helper(i, j+1)
                remove = 1 + helper(i+1, j)
                replace = 1 + helper(i+1, j+1)
                return min(insert, remove, replace)
        return helper(0, 0)
