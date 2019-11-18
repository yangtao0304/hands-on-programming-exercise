class Solution(object):
    def two_sum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for idx, num in enumerate(numbers):
            if num in d:
                return [d[num], idx+1]
            else:
                d[target - num] = idx+1
