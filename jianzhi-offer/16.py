class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 and n < 0:
            return

        power = abs(n)
        res = 1
        while power:
            if power % 2 == 1:
                res *= x
            x *= x
            power //= 2
        return res if n >= 0 else 1/res
