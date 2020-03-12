class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pos = m+n-1
        a = m-1
        b = n-1
        while pos >= 0:
            if a < 0:
                A[pos] = B[b]
                b -= 1
            elif b < 0:
                A[pos] = A[a]
                a -= 1
            elif A[a] < B[b]:
                A[pos] = B[b]
                b -= 1
            else:
                A[pos] = A[a]
                a -= 1
            pos -= 1
