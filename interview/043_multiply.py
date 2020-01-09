class Solution:
    # 普通竖式
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

    # 优化竖式
    # num1位数为M，num2位数为N，结果的最大位数为M+N
    # 对应位置为i+j，i+j+1
    def multiply2(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        len_1 = len(num1)
        len_2 = len(num2)
        res = [0 for _ in range(len_1+len_2)]

        for i in reversed(range(len_1)):
            digit_1 = int(num1[i])
            for j in reversed(range(len_2)):
                digit_2 = int(num2[j])
                tmp = res[i+j+1]+digit_1*digit_2
                res[i+j+1] = tmp % 10
                res[i+j] += tmp//10

        # 处理结果
        start_idx = 0
        for i in res:
            if i == 0:
                start_idx += 1
            else:
                break
        return ''.join([str(i) for i in res[start_idx:]])


if __name__ == "__main__":
    s = Solution()
    res = s.multiply2('123', '456')
    print(res)
