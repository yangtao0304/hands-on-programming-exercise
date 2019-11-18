class Solution(object):
    def find_max_consecutive_ones(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_num = max(count, max_num)
                count = 0
        return max(count, max_num)
