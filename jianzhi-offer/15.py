class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count

    def hammingWeight2(self, n: int) -> int:
        count = 0
        if n < 0:
            n = n & 0x7fffffff
            count += 1
        while n:
            count += n & 1
            n >>= 1
        return count
