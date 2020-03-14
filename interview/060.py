class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n):
            res = 1
            while n:
                res *= n
                n -= 1
            return res

        tokens = [str(i) for i in range(1, n+1)]
        res = ''
        k = k-1

        while n:
            n = n-1
            n_f = factorial(n)
            i, k = k//n_f, k % n_f
            res += tokens.pop(i)
        return res
