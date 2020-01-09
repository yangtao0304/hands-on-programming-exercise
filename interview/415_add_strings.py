class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        p1, p2 = len(num1)-1, len(num2)-1
        carry = 0
        while p1 >= 0 or p2 >= 0:
            n1 = int(num1[p1]) if p1 >= 0 else 0
            n2 = int(num2[p2]) if p2 >= 0 else 0
            tmp = n1 + n2+carry
            carry = tmp//10
            res = str(tmp % 10)+res
            p1 -= 1
            p2 -= 1
        if carry:
            res = '1'+res
        return res
