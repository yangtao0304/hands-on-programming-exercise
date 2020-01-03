'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
'''
from typing import List


class Solution:
    # 暴力递归
    # 最坏情况：时间复杂度O(n^n)，空间复杂度O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, wordDict, start):
            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and helper(s, wordDict, end):
                    return True
            return False

        return helper(s, set(wordDict), 0)

    # 记忆化回溯
    # 对子问题通过记忆化保存 O(n^2) O(n)
    # 每当访问到已经访问过的后缀串，直接用 memo 数组中的值返回而不需要继续调用函数
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, wordDict, start, memo):
            if start == len(s):
                return True

            if memo[start]:
                return memo[start]

            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and helper(s, wordDict, end, memo):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        memo = [None for _ in range(len(s))]
        return helper(s, set(wordDict), 0, memo)

    # leetcode 测试通过
    def wordBreak3(self, s: str, wordDict: List[str]) -> bool:
        wordDict_set = set(wordDict)
        import functools

        @functools.lru_cache(None)
        def back_track(s):
            if not s:
                return True
            for i in range(1, len(s)+1):
                if s[:i] in wordDict_set:
                    if back_track(s[i:]):
                        return True
            return False

        return back_track(s)

    # dp
    def wordBreak4(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        # ''为True
        dp[0] = True

        # 遍历所有字串
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]

    # dp
    def wordBreak5(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        wordDict = set(wordDict)

        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.wordBreak5(s='leetcode', wordDict=['leet', 'code']))
