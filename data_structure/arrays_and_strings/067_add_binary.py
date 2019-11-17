class Solution(object):
    def add_binary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a = len(a)
        length_b = len(b)
        length = max(length_a, length_b)
        if length_a >= length_b:
            b = '0' * (length_a-length_b) + b
        else:
            a = '0' * (length_b-length_a) + a

        carry = 0
        ans = ''
        while length:
            res = int(a[length-1]) + int(b[length - 1]) + carry
            if res >= 2:
                carry = 1
                res %= 2
            else:
                carry = 0
            ans = str(res) + ans
            length -= 1

        if carry:
            ans = '1'+ans

        return ans


if __name__ == "__main__":
    s = Solution()
    a = "1111"
    b = "1111"
    ret = s.add_binary(a, b)
    print(ret)
