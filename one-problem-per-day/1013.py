class Solution:
    # 超时
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        for i in range(n-2):
            for j in range(i+1, n-1):
                if sum(A[:i+1]) == sum(A[i+1:j+1]) and sum(A[i+1:j+1]) == sum(A[j+1:]):
                    return True
        return False

    def canThreePartsEqualSum2(self, A: List[int]) -> bool:
        n = len(A)
        sum_A = sum(A)
        if n < 3:
            return False
        if sum_A % 3 != 0:
            return False
        sum_A = sum_A//3
        tmp = 0
        time = 0
        for i in A:
            tmp += i
            if tmp == sum_A:
                time += 1
                tmp = 0
        if time >= 3:
            return True
        return False
