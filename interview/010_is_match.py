class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''
        match = s != '' and p[0] in (s[0], '.')
        # 如果发现有字符和'*'结合
        if len(p) >= 2 and p[1] == '*':
            # 两种情况：匹配0次 或 匹配1次
            # 匹配0次：越过p的前两个字符
            # 匹配1次：越过s的第一个字符
            return self.isMatch(s, p[2:]) or \
                match and self.isMatch(s[1:], p)
        else:
            return match and self.isMatch(s[1:], p[1:])


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch('aab', 'c*a*b'))
