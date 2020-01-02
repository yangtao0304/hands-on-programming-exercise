class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                s.remove(i)
        return s.pop()

    # 异或
    def singleNumber2(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
