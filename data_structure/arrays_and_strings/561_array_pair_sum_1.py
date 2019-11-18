class Solution(object):
    def array_pair_sum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum(nums[::2])