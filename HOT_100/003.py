# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度

'''
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0

        for i in s:
            if i not in s[left:right]:
                right += 1
            else:
                left += s[left: right].index(i) + 1
                right += 1

            if right - left > max_len:
                max_len = right - left

        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        lookup = list()
        cur_len = 0
        max_len = 0

        for i in s:
            if i not in lookup:
                cur_len += 1
                lookup.append(i)
            else:
                idx = lookup.index(i)
                lookup = lookup[idx+1:] + [i]
                cur_len = len(lookup)

            if cur_len > max_len:
                max_len = cur_len

        return max_len
