class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def string_add(a, b):
            p1 = len(a)-1
            p2 = len(b)-1
            res = ''
            carry = 0
            while p1 >= 0 or p2 >= 0:
                n1 = int(a[p1]) if p1 >= 0 else 0
                n2 = int(b[p2]) if p2 >= 0 else 0
                tmp = n1+n2+carry
                carry = tmp//10
                res = str(tmp % 10)+res
                p1 -= 1
                p2 -= 1
            if carry:
                res = '1' + res
            return res

        def string_mul(a, digit):
            res = ''
            p = len(a)-1
            carry = 0
            digit = int(digit)
            while p >= 0:
                tmp = int(a[p])*digit+carry
                carry = tmp//10
                res = str(tmp % 10)+res
                p -= 1
            if carry:
                res = str(carry)+res
            return res

        # 特殊情况
        if num1 == '0' or num2 == '0':
            return '0'

        l1, l2 = len(num1), len(num2)

        if l1 < l2:
            num1, num2 = num2, num1
            l1, l2 = l2, l1

        num2 = num2[::-1]
        res = '0'
        for idx, digit in enumerate(num2):
            tmp = string_mul(num1, digit)+'0'*idx
            res = string_add(res, tmp)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.multiply('123', '456')
    print(res)
