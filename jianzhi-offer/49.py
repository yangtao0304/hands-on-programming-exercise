class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]*n
        m2 = 0
        m3 = 0
        m5 = 0
        idx = 1
        while idx < n:
            ugly_nums[idx] = min(
                ugly_nums[m2]*2, ugly_nums[m3]*3, ugly_nums[m5]*5)
            if ugly_nums[idx] == ugly_nums[m2]*2:
                m2 += 1
            if ugly_nums[idx] == ugly_nums[m3]*3:
                m3 += 1
            if ugly_nums[idx] == ugly_nums[m5]*5:
                m5 += 1
            idx += 1
        return ugly_nums[-1]
