class Solution:
    # 暴力
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                if str1[:i]*(n1//i) == str1 and str1[:i]*(n2//i) == str2:
                    return str1[:i]
        return ''

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            # a>b
            if a < b:
                a, b = b, a
            while b:
                a, b = b, a % b
            return a

        n = gcd(len(str1), len(str2))
        candidate = str1[:n]
        if str1+str2 == str2+str1:
            return candidate
        return ''
