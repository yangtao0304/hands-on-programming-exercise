class Solution:
    def printNumbers(self, n: int) -> List[int]:
        def transfer(number):
            res = number[0]
            for i in number[1:]:
                res = res*10+i
            return res

        def add_one(number):
            is_overflow = False
            carry = 0
            n = len(number)
            for i in range(n-1, -1, -1):
                nsum = number[i]-0+carry
                if i == n-1:
                    nsum += 1
                if nsum >= 10:
                    if i == 0:
                        is_overflow = True
                    else:
                        nsum -= 10
                        carry = 1
                        number[i] = nsum
                else:
                    number[i] = nsum
                    break
            return is_overflow

        number = [0]*n
        res = []
        while not add_one(number):
            res.append(transfer(number))

        return res
