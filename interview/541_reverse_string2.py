class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        for i in range(0, n, 2*k):
            left = i
            right = min(left+k-1, n-1)
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
