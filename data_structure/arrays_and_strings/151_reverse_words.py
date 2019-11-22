class Solution(object):
    def reverse_words(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

    # 遍历添加法
    def reverse_words_2(self, s):
        s = s.strip()

        res = ""
        i, j = len(s)-1, len(s)
        while i >= 0:
            if s[i] == " ":
                res += s[i+1:j] + " "
                while s[i] == " ":
                    i -= 1
                j = i + 1
            else:
                i -= 1
        return res+s[:j]
