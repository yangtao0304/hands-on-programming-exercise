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
                if is_valid(s[i:j]) and j-i > max_len:
                    max_len = j-i

        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses('(()'))
