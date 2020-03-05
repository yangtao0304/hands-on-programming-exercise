class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return " "

        d = dict()
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1

        for i in d:
            if d[i] == 1:
                return i
        return " "
