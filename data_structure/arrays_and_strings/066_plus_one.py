class Solution(object):
    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        idx = length - 1
        while idx >= 0:
            digits[idx] += 1
            if digits[idx] == 10:
                digits[idx] = 0
                idx -= 1
            else:
                return digits
        # carry
        digits.insert(0, 1)
        return digits

    def plus_one_2(self, digits):
        # 思路
        # 从后向前，找到第一个不为9的数，该位+1，后面的数均变为0
        # 未找到的话，返回[1]+len(digits)*[0]
        find_idx = -1
        for idx, x in enumerate(digits[::-1]):
            if x != 9:
                find_idx = idx
                break
        if find_idx != -1:
            digits[-(find_idx+1)] += 1
            for idx in range(find_idx):
                digits[-(idx+1)] = 0
        else:
            digits = [1] + len(digits)*[0]
        return digits
