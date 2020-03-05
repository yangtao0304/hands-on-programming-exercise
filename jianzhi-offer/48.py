class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        for i in s:
            if i not in s[left:right]:
                right += 1
            else:
                left += s[left:right].index(i)+1
                right += 1
            if max_len < right-left:
                max_len = right-left
        return max_len
