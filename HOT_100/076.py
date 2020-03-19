'''
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

'''


class Solution:
    # 滑动窗口
    # 我们称包含T的全部字母的窗口为可行窗口
    # 两个指针，一个指针用来延伸现有窗口的right指针，
    # 和一个用于收缩窗口的left指针

    # 首先通过right扩张窗口，当窗口包含全部字符后，如果能收缩，我们就收缩窗口直到最小窗口

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ''

        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0

        window_counts = {}
        formed = 0

        ans = float('inf'), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                if r-l+1 < ans[0]:
                    ans = r-l+1, l, r

                character = s[l]
                window_counts[character] -= 1
                l += 1

                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

            r += 1

        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
